# entity_extraction_and_kg_creation.py
from transformers import pipeline
from py2neo import Graph, Node, Relationship
import json
from dotenv import load_dotenv
import os

# Step 1: Load the article data from ElasticSearch or JSON file
pmcid = "PMC11475376"
with open(f"article_data/{pmcid}.json") as file:
    article_data = json.load(file)

# Combine text fields for entity extraction
text = article_data.get("title", "") + " " + article_data.get("abstract", "") + " " + article_data.get("body", "")

# Step 2: Set up the HuggingFace NER pipeline
ner_pipeline = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", grouped_entities=True)

# Step 3: Extract entities using NER
entities = ner_pipeline(text)

# Filter and organize entities into categories
entities_dict = {"PERSON": [], "ORG": [], "LOC": [], "MISC": []}
for entity in entities:
    entity_type = entity["entity_group"]
    entity_text = entity["word"]
    if entity_type in entities_dict:
        entities_dict[entity_type].append(entity_text)

print("Extracted Entities:", entities_dict)

# Step 4: Connect to Neo4j and create nodes/relationships
load_dotenv()
# Set up your Neo4j connection details
NEO4J_URL = os.getenv(NEO4J_URL)            # Replace with your Neo4j instance URL
NEO4J_USERNAME = os.getenv(NEO4J_USERNAME)  # Replace with your Neo4j username
NEO4J_PASSWORD = os.getenv(NEO4J_PASSWORD)  # Replace with your Neo4j password

# Connect to Neo4j
graph = Graph(NEO4J_URL, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

# Create nodes for each unique entity
for entity_type, names in entities_dict.items():
    for name in set(names):  # Use set to avoid duplicate nodes
        node = Node(entity_type, name=name)
        graph.merge(node, entity_type, "name")  # Merge avoids duplication

# Step 5: Example relationships
# Here we create simple relationships between entities, assuming they're related.
# For example, every "PERSON" entity is "RELATED_TO" every "ORG" entity in the text.
# Adjust this logic as needed for your data and project.

for person in set(entities_dict["PERSON"]):
    person_node = graph.nodes.match("PERSON", name=person).first()
    for org in set(entities_dict["ORG"]):
        org_node = graph.nodes.match("ORG", name=org).first()
        if person_node and org_node:
            relation = Relationship(person_node, "RELATED_TO", org_node)
            graph.merge(relation)

print("Entities and relationships successfully added to Neo4j.")