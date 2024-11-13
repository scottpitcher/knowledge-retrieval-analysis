# es_indexing.py
# Purpose: index .json files and index in elastic search in Docker
from elasticsearch import Elasticsearch
import json

# Initialize ElasticSearch
es = Elasticsearch("http://localhost:9200")

# Load the article data from the saved JSON file
pmcid = "PMC11475376"  # Use the same PMCID as JSON filename
with open(f"article_data/{pmcid}.json") as file:
    article_data = json.load(file)

# Index the article in ElasticSearch
response = es.index(index="articles", id=pmcid, document=article_data)
print("Indexing Response:", response)

