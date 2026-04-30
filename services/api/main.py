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
def search(q: str):
    res = es.search(
        index="documents",
        query={"match": {"content": q}}
    )
    return res

@app.post("/crawl")
def crawl(url: str):
    task = celery_app.send_task("tasks.crawl_and_index", args=[url])
    return {"task_id": task.id}