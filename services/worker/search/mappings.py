# BM25 tuned index mapping
DOCUMENTS_MAPPING = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0,
        "analysis": {
            "analyzer": {
                "text_analyzer": {
                    "type": "standard",
                    "stopwords": "_english_"
                }
            }
        },
        "index": {
            "similarity": {
                "bm25_tuned": {
                    "type": "BM25",
                    "k1": 1.2,      # Controls term saturation point
                    "b": 0.75       # Controls length normalization
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "url": {
                "type": "keyword"  # Not analyzed, for exact matching
            },
            "title": {
                "type": "text",
                "analyzer": "text_analyzer",
                "similarity": "bm25_tuned",
                "boost": 2.5  # Title matches weighted higher
            },
            "content": {
                "type": "text",
                "analyzer": "text_analyzer",
                "similarity": "bm25_tuned",
                "boost": 1.0
            },
            "crawl_timestamp": {
                "type": "date"
            }
        }
    }
}
