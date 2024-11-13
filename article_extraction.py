# article_extraction.py
# Purpose: extract research articles to store locally as a .json file

import requests
from bs4 import BeautifulSoup
import json

# Fetch the article in XML format
pmcid = "PMC11475376"  # Replace with the actual PMCID
url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id={pmcid}&retmode=xml"
response = requests.get(url)

# Parse XML response
soup = BeautifulSoup(response.content, "lxml")

# Extract specific parts
title = soup.find("article-title").text if soup.find("article-title") else "No title"
abstract = soup.find("abstract").text if soup.find("abstract") else "No abstract"
body = " ".join([p.text for p in soup.find_all("p")])

# Structure data in JSON format
article_data = {
    "title": title,
    "abstract": abstract,
    "body": body
}

# Save the data to a JSON file
with open(f"article_data/{pmcid}.json", "w") as file:
    json.dump(article_data, file, indent=4) 