"""
Used in: 08_GenerativeAI_Neo4j_Knowledge_Graphs.ipynb
Purpose:
    Provide utilities for working with Neo4j graph database,
    including connection management, node/relationship creation, and Cypher query execution.
"""

from typing import Optional, Dict, List, Any
import os  # For environment variables


def connect_neo4j(
    uri: Optional[str] = None,
    user: Optional[str] = None,
    password: Optional[str] = None
) -> Any:
    """
    Connect to a Neo4j database.

    Args:
        uri: Neo4j connection URI (default: bolt://localhost:7687).
        user: Username (default: from NEO4J_USER env var or "neo4j").
        password: Password (default: from NEO4J_PASSWORD env var or "test").

    Returns:
        Neo4j driver object.
    """
    try:
        from neo4j import GraphDatabase
    except ImportError:
        raise ImportError(
            "neo4j driver is not installed. Install with: pip install neo4j"
        )

    # Get connection details from environment or defaults
    if uri is None:
        uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    if user is None:
        user = os.getenv("NEO4J_USER", "neo4j")
    if password is None:
        password = os.getenv("NEO4J_PASSWORD", "test")

    # Create driver
    driver = GraphDatabase.driver(uri, auth=(user, password))

    # Test connection
    try:
        with driver.session() as session:
            session.run("RETURN 1")
    except Exception as e:
        raise ConnectionError(f"Failed to connect to Neo4j: {str(e)}")

    return driver


def create_graph_nodes(
    driver: Any,
    label: str,
    properties: List[Dict[str, Any]],
    unique_key: Optional[str] = None
) -> int:
    """
    Create nodes in Neo4j graph.

    Args:
        driver: Neo4j driver object.
        label: Node label (e.g., "Person", "Company").
        properties: List of property dictionaries for each node.
        unique_key: Optional unique property key for MERGE operation.

    Returns:
        Number of nodes created.
    """
    created_count = 0

    with driver.session() as session:
        for props in properties:
            if unique_key and unique_key in props:
                # Use MERGE to avoid duplicates
                query = f"""
                MERGE (n:{label} {{{unique_key}: $value}})
                SET n += $props
                RETURN n
                """
                result = session.run(query, value=props[unique_key], props=props)
            else:
                # Use CREATE
                query = f"""
                CREATE (n:{label} $props)
                RETURN n
                """
                result = session.run(query, props=props)

            if result.single():
                created_count += 1

    return created_count


def create_graph_relationships(
    driver: Any,
    from_label: str,
    from_key: str,
    from_value: Any,
    to_label: str,
    to_key: str,
    to_value: Any,
    rel_type: str,
    rel_properties: Optional[Dict[str, Any]] = None
) -> bool:
    """
    Create a relationship between two nodes.

    Args:
        driver: Neo4j driver object.
        from_label: Label of source node.
        from_key: Property key to match source node.
        from_value: Property value to match source node.
        to_label: Label of target node.
        to_key: Property key to match target node.
        to_value: Property value to match target node.
        rel_type: Type of relationship (e.g., "FRIEND_OF", "WORKS_AT").
        rel_properties: Optional properties for the relationship.

    Returns:
        True if relationship created successfully.
    """
    with driver.session() as session:
        if rel_properties:
            query = f"""
            MATCH (a:{from_label} {{{from_key}: $from_val}})
            MATCH (b:{to_label} {{{to_key}: $to_val}})
            CREATE (a)-[r:{rel_type} $props]->(b)
            RETURN r
            """
            result = session.run(
                query,
                from_val=from_value,
                to_val=to_value,
                props=rel_properties or {}
            )
        else:
            query = f"""
            MATCH (a:{from_label} {{{from_key}: $from_val}})
            MATCH (b:{to_label} {{{to_key}: $to_val}})
            CREATE (a)-[r:{rel_type}]->(b)
            RETURN r
            """
            result = session.run(
                query,
                from_val=from_value,
                to_val=to_value
            )

        return result.single() is not None


def query_neo4j(
    driver: Any,
    cypher_query: str,
    parameters: Optional[Dict[str, Any]] = None
) -> List[Dict[str, Any]]:
    """
    Execute a Cypher query and return results.

    Args:
        driver: Neo4j driver object.
        cypher_query: Cypher query string.
        parameters: Optional query parameters.

    Returns:
        List of result dictionaries.
    """
    results = []

    with driver.session() as session:
        result = session.run(cypher_query, parameters or {})

        # Convert records to dictionaries
        for record in result:
            # Convert record to dict
            record_dict = {}
            for key in record.keys():
                value = record[key]
                # Handle Neo4j Node and Relationship objects
                if hasattr(value, "__class__"):
                    if value.__class__.__name__ == "Node":
                        record_dict[key] = {
                            "id": value.id,
                            "labels": list(value.labels),
                            "properties": dict(value)
                        }
                    elif value.__class__.__name__ == "Relationship":
                        record_dict[key] = {
                            "id": value.id,
                            "type": value.type,
                            "properties": dict(value)
                        }
                    else:
                        record_dict[key] = value
                else:
                    record_dict[key] = value

            results.append(record_dict)

    return results


def nl_to_cypher(
    natural_language: str,
    available_labels: Optional[List[str]] = None
) -> Optional[str]:
    """
    Simple natural language to Cypher query conversion (basic implementation).

    Args:
        natural_language: Natural language query.
        available_labels: Optional list of known node labels in the graph.

    Returns:
        Cypher query string, or None if conversion not possible.
    """
    # This is a simplified implementation
    # In practice, you might use an LLM to generate Cypher from natural language

    nl_lower = natural_language.lower()

    # Pattern: "find all X"
    if "find all" in nl_lower or "list all" in nl_lower:
        # Extract label
        words = natural_language.split()
        if "person" in nl_lower:
            return "MATCH (p:Person) RETURN p"
        elif "company" in nl_lower:
            return "MATCH (c:Company) RETURN c"

    # Pattern: "find friends of X"
    if "friends of" in nl_lower or "friend of" in nl_lower:
        # Extract person name
        import re
        match = re.search(r"(?:friends? of|friend of)\s+(\w+)", nl_lower)
        if match:
            name = match.group(1)
            return f'MATCH (p:Person {{name: "{name}"}})-[:FRIEND_OF]->(friend:Person) RETURN friend'

    # Pattern: "how are X and Y related"
    if "related" in nl_lower and "and" in nl_lower:
        import re
        match = re.search(r"(\w+)\s+and\s+(\w+)", natural_language)
        if match:
            name1, name2 = match.group(1), match.group(2)
            return f'''MATCH path = shortestPath((a:Person {{name: "{name1}"}})-[*..5]-(b:Person {{name: "{name2}"}}))
                      RETURN path'''

    return None

