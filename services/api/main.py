from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from elasticsearch import Elasticsearch
from celery import Celery

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001"],  # Next.js frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request models
class CrawlRequest(BaseModel):
    url: str

class CrawlListRequest(BaseModel):
    urls: list[str]

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
            "multi_match": {
                "query": q,
                "fields": [
                    "title^2.5",      # Boost title matches
                    "content^1.0"     # Normal content weight
                ],
                "type": "best_fields",
                "fuzziness": "AUTO",
                "operator": "or"
            }
        },
        size=size
    )

    results = []

    for hit in res["hits"]["hits"]:
        source = hit["_source"]

        results.append({
            "url": source.get("url"),
            "title": source.get("title") or source.get("url") or "Untitled",
            "snippet": source.get("content", "")[:200],  # first 200 chars
            "score": hit["_score"]
        })

    return {
        "query": q,
        "count": len(results),
        "results": results
    }

@app.post("/crawl")
def crawl(request: CrawlRequest):
    task = celery_app.send_task("tasks.crawl_and_index", args=[request.url])
    return {"task_id": task.id, "status": "queued", "url": request.url}