from elasticsearch import Elasticsearch

es = Elasticsearch("http://es:9200")


def index_document(url, content):

    es.index(
        index="documents",
        id=url,
        document={
            "url": url,
            "content": content
        }
    )