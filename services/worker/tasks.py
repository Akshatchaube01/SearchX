from celery import shared_task
import requests
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch

def clean_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()

@shared_task
def crawl_and_index(url):
    html = requests.get(url).text
    text = clean_html(html)

    es = Elasticsearch("http://es:9200")

    es.index(
        index="documents",
        document={
            "url": url,
            "content": text
        }
    )

    return {"status": "indexed", "url": url}