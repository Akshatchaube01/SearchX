from fastapi import FastAPI
from elasticsearch import Elasticsearch
from celery import Celery

app = FastAPI()

# Elasticsearch
es = Elasticsearch("http://es:9200")

# Celery
celery_app = Celery(
    "api",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/search")
def search(q: str, size: int = 5):
    res = es.search(
        index="documents",
        query={
            "match": {
                "content": {
                    "query": q,
                    "fuzziness": "AUTO"
                }
            }
        },
        size=size
    )

    results = []

    for hit in res["hits"]["hits"]:
        source = hit["_source"]

        results.append({
            "url": source.get("url"),
            "snippet": source.get("content", "")[:200],  # first 200 chars
            "score": hit["_score"]
        })

    return {
        "query": q,
        "count": len(results),
        "results": results
    }

@app.post("/crawl")
def crawl(url: str):
    task = celery_app.send_task("tasks.crawl_and_index", args=[url])
    return {"task_id": task.id}