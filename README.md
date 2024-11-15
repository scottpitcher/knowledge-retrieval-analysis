# Intelligent Knowledge Retrieval and Analysis System

A tool designed to extract, connect, and analyze information from large, unstructured datasets (e.g., research papers or medical documents). 
Leveraging NLP, knowledge graphs, and machine learning, the system allows users to search for entities, discover relationships, and receive insights through continuous model fine-tuning and feedback.
The system integrates advanced tools like HuggingFace, ElasticSearch, AWS SageMaker, Neo4j, and active learning to create a responsive, scalable solution for complex information retrieval.

**Technical Tools:** ElasticSearch, Hugging Face, PyTorch, Neo4j (Cypher), py2neo, GNNs, GDS, Flask/FastAPI, Docker
**Skills:** NLP, NER, API Dev., Containerization

## Project Workflow

- **Data Ingrestion/Indexing:** Collecting unstructed data (research articles). Utilising *ElasticSearch* for indexing, and development of *search API* for querying.
- **Entity Extraction and Knowledge Graph Creation:** Use *HuggingFace* models (*NER*) to extract key entities, summarize docs, and categorize information. Store entity/relationshup in *Neo4j* as knowledge graph (e.g. Disease -> Treatment, Author -> Publication).
- **Graph Analysis and Insight Discovery:** Implement Graph Neural Networks *(GNNs)* for relationship analysis in Neo4j graph, uncovering hidden patterns (clustering, central nodes).
- Model Deployment and Scalability: Deploy the entity extraction, summarization, and recommendation models on AWS SageMaker for scalable, cloud-based processing, ensuring real-time query handling and reliable model performance.
- **Domain-Specific Fine-Tuning:** Fine-tune pre-trained models on the document dataset using HuggingFace to specialize in the domain-specific terminology, improving relevance and accuracy in the extraction and categorization processes.
- **Interactive Feedback Loop with Human-in-the-Loop Learning:** Enable users to provide feedback on search results, using this input to retrain models with Human-in-the-Loop Learning for continual system improvement based on user interactions.
- **Active Learning for Model Improvement:** Implement Active Learning techniques to identify the most informative samples for further training, prioritizing documents with low confidence scores or frequent feedback for model refinement.
-**Natural Language Querying and Summarization:** Use GPT-3 to interpret complex user queries, generate document summaries, and answer specific questions based on the indexed documents and knowledge graph, enhancing the system’s interactivity and responsiveness.

