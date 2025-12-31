"""
Used in: 09_GenerativeAI_Graph_RAG.ipynb
Purpose:
    Provide utilities for Graph RAG (Retrieval-Augmented Generation with Knowledge Graphs),
    including graph-based retrieval, graph-to-text conversion, and hybrid retrieval.
    
Educational Context:
    Graph RAG combines knowledge graphs with RAG for better retrieval.
    
    How Graph RAG Works:
    1. Extract entities and relationships from documents
    2. Build knowledge graph (nodes = entities, edges = relationships)
    3. When query comes in:
       a. Find relevant entities in graph
       b. Traverse graph to find related entities (multi-hop)
       c. Retrieve connected subgraph
       d. Convert graph to text context
       e. Pass to LLM for generation
    
    Advantages over Vector RAG:
    - Multi-hop reasoning (A → B → C)
    - Explicit relationships (not just similarity)
    - Structured knowledge (not just text chunks)
    - Better for complex queries
    
    Hybrid Approach:
    - Combine vector search (semantic similarity)
    - With graph traversal (structured relationships)
    - Best of both worlds
"""

# Import type hints
from typing import List, Dict, Any, Optional, Tuple

# Import NumPy: For array operations
import numpy as np


def graph_rag_retrieve(
    driver: Any,
    query: str,
    entity_labels: Optional[List[str]] = None,
    max_hops: int = 2,
    limit: int = 10
) -> List[Dict[str, Any]]:
    """
    Retrieve relevant subgraph from Neo4j based on query.

    Args:
        driver: Neo4j driver object.
        query: Natural language query.
        entity_labels: Optional list of node labels to search (e.g., ["Person", "Company"]).
        max_hops: Maximum graph traversal depth.
        limit: Maximum number of results to return.

    Returns:
        List of dictionaries containing retrieved graph data.
    """
    from src.llm.neo4j_utils import query_neo4j

    # Simple entity extraction (in practice, use NER or LLM)
    query_lower = query.lower()
    entities = []

    # Try to find entity names in query
    if entity_labels:
        for label in entity_labels:
            # Simple pattern: look for capitalized words that might be entity names
            import re
            # This is simplified - in practice, use proper NER
            pattern = rf"\b([A-Z][a-z]+)\b"
            matches = re.findall(pattern, query)
            entities.extend(matches)

    # Build Cypher query to find relevant subgraph
    if entities:
        # Query for nodes matching entities
        entity_filters = " OR ".join([f"n.name CONTAINS '{e}'" for e in entities[:3]])
        cypher = f"""
        MATCH path = (n)-[*..{max_hops}]-(m)
        WHERE {entity_filters}
        RETURN path, n, m
        LIMIT {limit}
        """
    else:
        # Generic query: return some connected nodes
        cypher = f"""
        MATCH (n)-[r]-(m)
        RETURN n, r, m
        LIMIT {limit}
        """

    # Execute query
    results = query_neo4j(driver, cypher)

    return results


def format_graph_context(
    graph_results: List[Dict[str, Any]],
    format_style: str = "natural"
) -> str:
    """
    Convert graph query results into text context for LLM.

    Args:
        graph_results: List of graph query results from Neo4j.
        format_style: Format style ("natural", "triples", "structured").

    Returns:
        Formatted text context string.
    """
    context_parts = []

    if format_style == "natural":
        # Convert to natural language sentences
        for result in graph_results:
            # Extract nodes and relationships
            nodes = []
            relationships = []

            for key, value in result.items():
                if isinstance(value, dict):
                    if "labels" in value:  # Node
                        nodes.append(value)
                    elif "type" in value:  # Relationship
                        relationships.append(value)

            # Format as sentences
            for rel in relationships:
                # Find connected nodes (simplified)
                if nodes:
                    context_parts.append(
                        f"{nodes[0].get('properties', {}).get('name', 'Entity')} "
                        f"{rel.get('type', 'RELATED_TO').lower().replace('_', ' ')} "
                        f"{nodes[1].get('properties', {}).get('name', 'Entity') if len(nodes) > 1 else 'something'}."
                    )

    elif format_style == "triples":
        # Format as subject-predicate-object triples
        for result in graph_results:
            for key, value in result.items():
                if isinstance(value, dict) and "type" in value:  # Relationship
                    rel_type = value.get("type", "RELATED_TO")
                    # Extract subject and object from result
                    context_parts.append(f"(Entity) -[{rel_type}]-> (Entity)")

    else:  # structured
        # Structured format with details
        for i, result in enumerate(graph_results, 1):
            context_parts.append(f"Graph fact {i}:")
            context_parts.append(str(result))

    return "\n".join(context_parts)


def multi_hop_graph_query(
    driver: Any,
    start_entity: str,
    start_label: str,
    target_label: Optional[str] = None,
    relationship_types: Optional[List[str]] = None,
    max_hops: int = 3
) -> List[Dict[str, Any]]:
    """
    Perform multi-hop graph traversal query.

    Args:
        driver: Neo4j driver object.
        start_entity: Starting entity identifier (e.g., name or ID).
        start_label: Label of starting node.
        target_label: Optional target node label to find.
        relationship_types: Optional list of relationship types to traverse.
        max_hops: Maximum number of hops to traverse.

    Returns:
        List of paths found in the graph.
    """
    from src.llm.neo4j_utils import query_neo4j

    # Build relationship filter
    rel_filter = ""
    if relationship_types:
        rel_types_str = "|".join(relationship_types)
        rel_filter = f":{rel_types_str}"

    # Build target filter
    target_filter = ""
    if target_label:
        target_filter = f":{target_label}"

    # Construct Cypher query for multi-hop traversal
    cypher = f"""
    MATCH path = (start:{start_label} {{name: $start_name}})-[*1..{max_hops}{rel_filter}]-(end{target_filter})
    RETURN path, start, end
    LIMIT 20
    """

    results = query_neo4j(driver, cypher, {"start_name": start_entity})

    return results


def hybrid_rag_retrieve(
    vector_index: Any,
    vector_chunks: List[Dict[str, Any]],
    graph_driver: Any,
    query: str,
    query_embedding: np.ndarray,
    top_k_vector: int = 3,
    top_k_graph: int = 3,
    combine_strategy: str = "union"
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    """
    Perform hybrid retrieval combining vector search and graph queries.

    Args:
        vector_index: FAISS vector index.
        vector_chunks: List of vector document chunks.
        graph_driver: Neo4j driver object.
        query: Natural language query.
        query_embedding: Query embedding vector.
        top_k_vector: Number of vector results to retrieve.
        top_k_graph: Number of graph results to retrieve.
        combine_strategy: How to combine results ("union", "intersection", "weighted").

    Returns:
        Tuple of (vector_results, graph_results).
    """
    from src.llm.rag_utils import retrieve_relevant_docs
    from src.llm.graph_rag_utils import graph_rag_retrieve

    # Vector retrieval
    vector_results = retrieve_relevant_docs(
        vector_index,
        vector_chunks,
        query_embedding,
        top_k=top_k_vector
    )

    # Graph retrieval
    graph_results = graph_rag_retrieve(
        graph_driver,
        query,
        limit=top_k_graph
    )

    # Combine based on strategy
    if combine_strategy == "union":
        # Return both (no deduplication)
        return vector_results, graph_results
    elif combine_strategy == "intersection":
        # Find common entities (simplified - would need entity matching)
        # For now, just return both
        return vector_results, graph_results
    else:  # weighted
        # Could apply weights to scores
        return vector_results, graph_results


def format_hybrid_context(
    vector_results: List[Dict[str, Any]],
    graph_results: List[Dict[str, Any]],
    query: str
) -> str:
    """
    Format combined vector and graph results into context for LLM.

    Args:
        vector_results: Results from vector retrieval.
        graph_results: Results from graph retrieval.
        query: Original query.

    Returns:
        Formatted context string.
    """
    context_parts = []

    # Add vector-based context
    if vector_results:
        context_parts.append("Relevant text passages:")
        for i, doc in enumerate(vector_results, 1):
            context_parts.append(f"{i}. {doc['text']}")

    # Add graph-based context
    if graph_results:
        context_parts.append("\nRelevant graph facts:")
        graph_text = format_graph_context(graph_results, format_style="natural")
        context_parts.append(graph_text)

    # Combine into full prompt
    context = "\n".join(context_parts)
    prompt = f"""Context:
{context}

Question: {query}

Answer based on the context above:"""

    return prompt

