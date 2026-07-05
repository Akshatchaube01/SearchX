from elasticsearch import Elasticsearch
from datetime import datetime
from search.mappings import DOCUMENTS_MAPPING

es = Elasticsearch("http://es:9200")

INDEX_NAME = "documents"

def create_index_if_not_exists():
    """Create index with BM25 optimized mapping"""
    if not es.indices.exists(index=INDEX_NAME):
        es.indices.create(index=INDEX_NAME, body=DOCUMENTS_MAPPING)
        print(f"Index '{INDEX_NAME}' created with BM25 tuning")
    else:
        print(f"Index '{INDEX_NAME}' already exists")

def index_document(url, title, content):
    """Index document with title and content"""
    create_index_if_not_exists()
    
    es.index(
        index=INDEX_NAME,
        id=url,
        document={
            "url": url,
            "title": title or "Untitled",
            "content": content,
            "crawl_timestamp": datetime.now()
        }
    )