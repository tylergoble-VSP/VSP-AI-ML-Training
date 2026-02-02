# VSP AI/ML Training Pipeline

A comprehensive training pipeline organized as self-contained modules, taking participants from core Python skills through advanced machine learning and AI techniques.

## Overview

This repository contains **46 self-contained Jupyter notebooks** designed for intermediate developers with some programming background. Each module can be run independently to learn a specific topic, and all modules follow software engineering best practices with modular, well-documented code.

The notebooks are organized into:
- **12 foundational notebooks** (01-12): Python fundamentals, ML introduction, and core topics
- **25 algorithm-specific notebooks** (13-37): Deep dives into individual ML algorithms with theory, implementation, validation, benchmarking, and traceability
- **9 GenerativeAI notebooks** (01-09): Advanced Generative AI frameworks and concepts including Hugging Face, llama.cpp, Ollama, LoRA/PEFT, Chain-of-Thought, Tool Calling, RAG, Neo4j, and Graph RAG

This repository also includes interview-ready materials under `Interview/` for Traditional ML and Generative AI implementation assessments.

## Target Audience

Intermediate developers with some programming background who want to:
- Strengthen Python fundamentals
- Learn machine learning algorithms and techniques
- Explore advanced AI topics including embeddings and generative models
- Gain hands-on experience with popular ML libraries

## Repository Structure

```
VSP-AI-ML-Training/
├── notebooks/                          # All Jupyter notebooks organized by category
│   ├── foundations/                    # Foundational notebooks (01-12)
│   │   ├── 01_Beginning_Python.ipynb
│   │   ├── 02_Intermediate_Python.ipynb
│   │   ├── 03_Advanced_Python.ipynb
│   │   ├── 04_Machine_Learning_Algorithms.ipynb
│   │   ├── 05_Supervised_Learning.ipynb
│   │   ├── 06_Classifier_Algorithms.ipynb
│   │   ├── 07_Unsupervised_Learning.ipynb
│   │   ├── 08_Clustering_Algorithms.ipynb
│   │   ├── 09_Survival_Analysis.ipynb
│   │   ├── 10_Embedding_Models.ipynb
│   │   ├── 11_Generative_Models.ipynb
│   │   └── 12_Analytics_Performance.ipynb
│   ├── supervised/                     # Supervised learning algorithms (01-07)
│   │   ├── 01_Supervised_Linear_Regression.ipynb
│   │   ├── 02_Supervised_Logistic_Regression.ipynb
│   │   ├── 03_Supervised_Decision_Trees.ipynb
│   │   ├── 04_Supervised_Support_Vector_Machine.ipynb
│   │   ├── 05_Supervised_KNearest_Neighbors.ipynb
│   │   ├── 06_Supervised_Naive_Bayes.ipynb
│   │   └── 07_Supervised_Linear_Discriminant_Analysis.ipynb
│   ├── ensemble/                       # Ensemble learning algorithms (01-04)
│   │   ├── 01_Ensemble_Random_Forest.ipynb
│   │   ├── 02_Ensemble_AdaBoost.ipynb
│   │   ├── 03_Ensemble_Gradient_Boosting.ipynb
│   │   └── 04_Ensemble_XGBoost.ipynb
│   ├── unsupervised/                   # Unsupervised learning algorithms (01-07)
│   │   ├── 01_Unsupervised_KMeans_Clustering.ipynb
│   │   ├── 02_Unsupervised_Hierarchical_Clustering.ipynb
│   │   ├── 03_Unsupervised_DBSCAN.ipynb
│   │   ├── 04_Unsupervised_Gaussian_Mixture_Models.ipynb
│   │   ├── 05_Unsupervised_Principal_Component_Analysis.ipynb
│   │   ├── 06_Unsupervised_TSNE.ipynb
│   │   └── 07_Unsupervised_Apriori.ipynb
│   ├── reinforcement/                  # Reinforcement learning algorithms (01-02)
│   │   ├── 01_Reinforcement_QLearning.ipynb
│   │   └── 02_Reinforcement_Policy_Gradient.ipynb
│   └── neural_networks/                # Neural networks and deep learning (01-05)
│       ├── 01_NeuralNetworks_Perceptron_MLP.ipynb
│       ├── 02_NeuralNetworks_Convolutional_Neural_Networks.ipynb
│       ├── 03_NeuralNetworks_Recurrent_Neural_Networks_LSTM.ipynb
│       ├── 04_NeuralNetworks_Generative_Adversarial_Networks.ipynb
│       └── 05_NeuralNetworks_Transformers.ipynb
│   └── generative_ai/                  # Generative AI frameworks and concepts (01-09)
│       ├── 01_GenerativeAI_HuggingFace_Transformers.ipynb
│       ├── 02_GenerativeAI_LlamaCPP_Local_Models.ipynb
│       ├── 03_GenerativeAI_Ollama_Model_Serving.ipynb
│       ├── 04_GenerativeAI_LoRA_PEFT_FineTuning.ipynb
│       ├── 05_GenerativeAI_ChainOfThought_Reasoning.ipynb
│       ├── 06_GenerativeAI_Tool_Calling_Agents.ipynb
│       ├── 07_GenerativeAI_Retrieval_Augmented_Generation.ipynb
│       ├── 08_GenerativeAI_Neo4j_Knowledge_Graphs.ipynb
│       └── 09_GenerativeAI_Graph_RAG.ipynb
│   └── interview/                      # Interview exercise notebooks (01-03)
│       ├── 01_GenAI_Implementation_Junior.ipynb
│       ├── 02_GenAI_Implementation_Mid.ipynb
│       └── 03_GenAI_Implementation_Senior.ipynb
├── Interview/                          # Interview materials (anonymized)
│   ├── Generative/
│   │   └── Generative_AI_Implementation_Section.md
│   └── Machine_Learning/
│       └── Traditional_ML_Interview_Section.md
├── config/                             # YAML configs (no hard-coded model IDs)
│   └── llm_interview.yaml
├── requirements.txt                   # Python dependencies
├── README.md                          # This file
├── pytest.ini                         # Pytest configuration
├── src/                               # Helper functions and utilities
│   ├── data/                          # Data loading utilities
│   ├── processing/                    # Data preprocessing
│   ├── models/                        # ML model utilities
│   ├── llm/                           # LLM and embedding utilities
│   │   ├── embeddings.py              # Embedding utilities
│   │   ├── config.py                  # LLM config parsing
│   │   ├── tokenization.py            # Tokenizer utilities
│   │   ├── model_loading.py           # Model loading utilities
│   │   ├── generation.py              # Generation wrapper
│   │   ├── eval.py                    # Golden prompt evaluation
│   │   ├── telemetry.py               # Token/timing telemetry
│   │   ├── transformers_utils.py     # Hugging Face utilities
│   │   ├── llama_cpp_utils.py        # llama.cpp utilities
│   │   ├── ollama_utils.py           # Ollama utilities
│   │   ├── peft_utils.py             # LoRA/PEFT utilities
│   │   ├── chain_of_thought.py       # Chain-of-Thought utilities
│   │   ├── tool_calling.py           # Tool calling utilities
│   │   ├── rag_utils.py              # RAG utilities
│   │   ├── neo4j_utils.py            # Neo4j utilities
│   │   └── graph_rag_utils.py        # Graph RAG utilities
│   └── utils/                         # General utilities (paths, timing)
├── tests/                             # Unit tests
│   ├── test_paths.py
│   ├── test_timing.py
│   ├── test_regression.py
│   ├── test_classification.py
│   ├── test_ensemble.py
│   ├── test_validation.py
│   ├── test_supervised.py
│   ├── test_unsupervised.py
│   └── test_generative_ai/            # GenerativeAI utility tests
│       ├── test_transformers_utils.py
│       ├── test_llama_cpp_utils.py
│       ├── test_ollama_utils.py
│       ├── test_peft_utils.py
│       ├── test_chain_of_thought.py
│       ├── test_tool_calling.py
│       ├── test_rag_utils.py
│       ├── test_neo4j_utils.py
│       └── test_graph_rag_utils.py
├── outputs/                           # Generated outputs
│   ├── logs/                          # Timing and execution logs
│   ├── processed/                     # Processed data files
│   └── results/                      # Analysis results
└── scripts/                           # Setup and utility scripts
```

## Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### 2. Create Virtual Environment

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# On Linux/Mac:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Notebooks

Open the notebooks in VS Code (recommended) or Jupyter:

```bash
# In VS Code, simply open any .ipynb file
# Or use Jupyter:
jupyter notebook
```

## Interview Notebooks (Generative AI)

Three interview exercises are available under `notebooks/interview/`:
- `01_GenAI_Implementation_Junior.ipynb`
- `02_GenAI_Implementation_Mid.ipynb`
- `03_GenAI_Implementation_Senior.ipynb`

Configuration is stored in `config/llm_interview.yaml`. Update model IDs, device strategy, and generation defaults there (no hard-coded IDs in code).

## Module Descriptions

### Python Fundamentals (Modules 01-03)

**01_Beginning_Python**: Introduces fundamental Python concepts including syntax, data types, data structures (lists, tuples, dictionaries, sets), control flow, and basic functions.

**02_Intermediate_Python**: Covers list/dict comprehensions, lambda functions, file I/O, advanced function features (*args, **kwargs), error handling, basic OOP, and standard library modules.

**03_Advanced_Python**: Explores iterators, generators, decorators, context managers, and introduces NumPy and Pandas for numerical computing and data manipulation.

### Machine Learning Introduction (Module 04)

**04_Machine_Learning_Algorithms**: Provides a high-level introduction to ML, distinguishing between supervised and unsupervised learning, and demonstrates basic classification and clustering examples.

### Supervised Learning (Modules 05-06)

**05_Supervised_Learning**: Dives into supervised learning with regression and classification techniques, cross-validation, and hyperparameter tuning using real datasets.

**06_Classifier_Algorithms**: In-depth study of classification algorithms including Logistic Regression, SVM, Decision Trees, Random Forest, Naive Bayes, and KNN, with performance comparison.

### Unsupervised Learning (Modules 07-08)

**07_Unsupervised_Learning**: Covers unsupervised learning concepts and dimensionality reduction techniques like Principal Component Analysis (PCA).

**08_Clustering_Algorithms**: Detailed study of clustering techniques including K-Means, Hierarchical Clustering, and DBSCAN, with evaluation metrics.

### Specialized Topics (Modules 09-11)

**09_Survival_Analysis**: Introduces survival analysis for time-to-event data, including Kaplan-Meier estimation and Cox Proportional Hazards models.

**10_Embedding_Models**: Explores embedding models for representing text and other data in vector spaces, including Word2Vec, BERT, and sentence transformers.

**11_Generative_Models**: Covers generative models including Variational Autoencoders (VAE) and Generative Adversarial Networks (GANs) for creating new data samples.

### Analytics (Module 12)

**12_Analytics_Performance**: Reads timing logs and visualizes performance metrics across all modules.

## Algorithm-Specific Notebooks (Modules 13-37)

Each algorithm notebook includes:
- **Theory & Mechanics**: Mathematical foundations and how the algorithm works
- **Implementation**: Working code examples with scikit-learn and/or PyTorch
- **Validation & Testing**: In-notebook assertions, cross-validation, and output validation
- **Performance Benchmarking**: Training and prediction time measurements
- **Traceability**: Feature importance, decision paths, and model interpretability
- **Visualization**: Plots, charts, and diagnostic visualizations
- **Real-World Application**: Practical examples and hyperparameter tuning

### Supervised Learning Algorithms (`notebooks/supervised/`)

**01_Supervised_Linear_Regression**: Linear regression for continuous target prediction with residual analysis and assumption checking.

**02_Supervised_Logistic_Regression**: Logistic regression for binary and multiclass classification with ROC curves and confusion matrices.

**03_Supervised_Decision_Trees**: Decision trees for classification and regression with tree visualization and feature importance.

**04_Supervised_Support_Vector_Machine**: SVM with different kernels (linear, polynomial, RBF) for classification and regression.

**05_Supervised_KNearest_Neighbors**: K-NN algorithm with distance metrics and optimal k selection.

**06_Supervised_Naive_Bayes**: Naive Bayes variants (Gaussian, Multinomial, Bernoulli) with text classification examples.

**07_Supervised_Linear_Discriminant_Analysis**: LDA for classification and dimensionality reduction.

### Ensemble Learning Algorithms (`notebooks/ensemble/`)

**01_Ensemble_Random_Forest**: Random Forest with feature importance and out-of-bag error analysis.

**02_Ensemble_AdaBoost**: Adaptive Boosting with weak learner analysis and learning rate effects.

**03_Ensemble_Gradient_Boosting**: Gradient Boosting Machines with learning curves and overfitting detection.

**04_Ensemble_XGBoost**: XGBoost with early stopping, regularization, and performance optimization.

### Unsupervised Learning Algorithms (`notebooks/unsupervised/`)

**01_Unsupervised_KMeans_Clustering**: K-Means clustering with elbow method and silhouette analysis.

**02_Unsupervised_Hierarchical_Clustering**: Hierarchical clustering with dendrogram visualization and linkage methods.

**03_Unsupervised_DBSCAN**: Density-based clustering with k-distance graphs and noise detection.

**04_Unsupervised_Gaussian_Mixture_Models**: GMM with AIC/BIC model selection and covariance types.

**05_Unsupervised_Principal_Component_Analysis**: PCA with explained variance analysis and component selection.

**06_Unsupervised_TSNE**: t-SNE for dimensionality reduction with perplexity tuning and comparison with PCA.

**07_Unsupervised_Apriori**: Apriori algorithm for frequent itemset mining and association rules.

### Reinforcement Learning Algorithms (`notebooks/reinforcement/`)

**01_Reinforcement_QLearning**: Q-Learning with epsilon-greedy exploration, Q-table visualization, and grid world examples.

**02_Reinforcement_Policy_Gradient**: Policy gradient methods (REINFORCE) with policy visualization and learning curves.

### Neural Networks and Deep Learning (`notebooks/neural_networks/`)

**01_NeuralNetworks_Perceptron_MLP**: Perceptron and Multilayer Perceptron with decision boundary visualization and architecture comparison.

**02_NeuralNetworks_Convolutional_Neural_Networks**: CNNs with filter visualization, feature maps, and image classification.

**03_NeuralNetworks_Recurrent_Neural_Networks_LSTM**: RNNs and LSTMs for sequence prediction with time series examples.

**04_NeuralNetworks_Generative_Adversarial_Networks**: GANs with generator/discriminator training and sample generation.

**05_NeuralNetworks_Transformers**: Transformer architecture with self-attention, multi-head attention, and positional encoding.

### Generative AI Frameworks and Concepts (`notebooks/generative_ai/`)

**01_GenerativeAI_HuggingFace_Transformers**: Hugging Face Transformers library for text generation, classification, and NLP tasks with Pipeline API and AutoModel usage.

**02_GenerativeAI_LlamaCPP_Local_Models**: Running LLMs locally with llama.cpp, including quantization, CPU optimization, and performance benchmarking.

**03_GenerativeAI_Ollama_Model_Serving**: Ollama platform for easy local model management, serving, and Python API integration with streaming responses.

**04_GenerativeAI_LoRA_PEFT_FineTuning**: Parameter-efficient fine-tuning with LoRA (Low-Rank Adaptation) and PEFT library for adapting large models with minimal resources.

**05_GenerativeAI_ChainOfThought_Reasoning**: Chain-of-Thought prompting techniques for improving reasoning capabilities, including self-consistency decoding.

**06_GenerativeAI_Tool_Calling_Agents**: Building LLM agents that can call external tools, including OpenAI function calling, ReAct pattern, and agent loops.

**07_GenerativeAI_Retrieval_Augmented_Generation**: RAG architecture combining vector embeddings, FAISS similarity search, and document chunking for grounded LLM responses.

**08_GenerativeAI_Neo4j_Knowledge_Graphs**: Working with Neo4j graph database, Cypher queries, and knowledge graph creation for structured information storage.

**09_GenerativeAI_Graph_RAG**: Graph RAG combining knowledge graphs with LLMs for multi-hop reasoning and hybrid vector + graph retrieval.

## Standard Datasets Used

The modules use standard datasets from scikit-learn and other libraries:

- **Iris** - Classification (3 flower species)
- **Digits** - Classification (handwritten digits)
- **California Housing** - Regression (house prices)
- **Breast Cancer** - Classification (medical diagnosis)
- **Wine** - Clustering (wine characteristics)
- **MNIST** - Classification/Generative (handwritten digits)
- **Survival datasets** - Survival analysis (from lifelines)

## Key Features

- **Modular Design**: Each notebook is self-contained and can be run independently
- **Helper Functions**: All reusable code is organized in `/src` directories
- **Best Practices**: Follows software engineering best practices with proper documentation
- **Timestamped Outputs**: All outputs use timestamped filenames for versioning
- **Performance Tracking**: Built-in timing utilities for performance analysis
- **Standard Libraries**: Uses up-to-date, popular Python libraries
- **Comprehensive Testing**: Unit tests for all helper functions using pytest
- **Deep Dives**: Each algorithm notebook includes theory, implementation, validation, benchmarking, and traceability
- **Visualization**: Rich plots and diagnostic visualizations in every notebook
- **Real-World Examples**: Practical applications and hyperparameter tuning guidance

## Development Environment

- **IDE**: Visual Studio Code (recommended) with Jupyter extension
- **Python**: 3.8+
- **Notebook Format**: Jupyter Notebook (.ipynb)

## Output Management

All outputs are automatically written to `/outputs/` with timestamped filenames:
- **CSV/Parquet/JSON**: Written to `/outputs/results/`
- **Logs**: Written to `/outputs/logs/`
- **Processed Data**: Written to `/outputs/processed/`

## Notebook Import Bootstrap

All notebooks must start with a repo-root bootstrap cell so `import src...` works
regardless of the working directory. Keep this as the first code cell:

```python
# stdlib pathlib (filesystem paths)
from pathlib import Path

# src/utils/pathing.py
from src.utils.pathing import ensure_repo_root_on_sys_path  # src/utils/pathing.py

ensure_repo_root_on_sys_path(Path.cwd())
```

For Generative AI interview notebooks, logs follow:
- `outputs/logs/llm_tokens_<YYYYMMDD_HHMMSSZ>.jsonl`
- `outputs/logs/llm_timing_<YYYYMMDD_HHMMSSZ>.jsonl`

## Testing

Run unit tests using pytest:

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_regression.py

# Run with verbose output
pytest -v
```

All helper functions in `/src` have corresponding unit tests in `/tests` covering:
- Function correctness
- Edge cases
- Error handling
- Expected behavior

## Contributing

This is a training repository. When working with the notebooks:
- Keep notebooks clean - all functions should be in `/src` scripts
- Use timestamped outputs for all file writes
- Follow the existing code style and documentation standards
- Test your code before committing
- Add unit tests for any new helper functions
- Keep the bootstrap import cell as the first code cell in each notebook

## License

This training material is provided for educational purposes.

## Algorithm Index

### By Category

**Foundations** (`notebooks/foundations/`)
- Python fundamentals (01-03), ML introduction (04), Supervised/Unsupervised overview (05-08), Specialized topics (09-11), Analytics (12)

**Supervised Learning** (`notebooks/supervised/`)
- Linear Regression (01), Logistic Regression (02), Decision Trees (03), SVM (04), K-NN (05), Naive Bayes (06), LDA (07)

**Ensemble Methods** (`notebooks/ensemble/`)
- Random Forest (01), AdaBoost (02), Gradient Boosting (03), XGBoost (04)

**Unsupervised Learning** (`notebooks/unsupervised/`)
- K-Means (01), Hierarchical Clustering (02), DBSCAN (03), GMM (04), PCA (05), t-SNE (06), Apriori (07)

**Reinforcement Learning** (`notebooks/reinforcement/`)
- Q-Learning (01), Policy Gradient Methods (02)

**Neural Networks** (`notebooks/neural_networks/`)
- Perceptron/MLP (01), CNNs (02), RNNs/LSTM (03), GANs (04), Transformers (05)

### By Complexity

**Beginner**: `supervised/01-03, 05-07`, `unsupervised/01, 05`
**Intermediate**: `supervised/04`, `ensemble/01-03`, `unsupervised/02-04, 06-07`, `neural_networks/01`
**Advanced**: `ensemble/04`, `reinforcement/01-02`, `neural_networks/02-05`

## References

- [scikit-learn Documentation](https://scikit-learn.org/)
- [PyTorch Documentation](https://pytorch.org/docs/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/)
- [XGBoost Documentation](https://xgboost.readthedocs.io/)
- [Transformers (Hugging Face)](https://huggingface.co/docs/transformers/)

## Support

For questions or issues, please refer to the module-specific documentation within each notebook.
