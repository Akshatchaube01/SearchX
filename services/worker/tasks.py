import requests
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch
from celery import Celery

celery_app = Celery(
    "worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0"
)

es = Elasticsearch("http://es:9200")


def clean_html(html):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript", "header", "footer", "nav", "aside"]):
        tag.decompose()
    text = soup.get_text(separator=" ")
    return " ".join(text.split())


def extract_links(base_url, html):
    soup = BeautifulSoup(html, "html.parser")
    links = set()

    for tag in soup.find_all("a", href=True):
        href = tag["href"]
        full_url = requests.compat.urljoin(base_url, href)
        if full_url.startswith("http"):
            links.add(full_url)

    return links


@celery_app.task(name="tasks.crawl_and_index")
def crawl_and_index(start_url, max_depth=2):
    visited = set()
    queue = [(start_url, 0)]

    while queue:
        url, depth = queue.pop(0)

        if url in visited or depth > max_depth:
            continue

        visited.add(url)

        try:
            response = requests.get(url, timeout=5)
            html = response.text

            text = clean_html(html)
            es.index(
                index="documents",
                document={
                    "url": url,
                    "content": text
                }
            )

            print(f"Indexed: {url}")
            links = extract_links(url, html)

            for link in links:
                if link not in visited:
                    queue.append((link, depth + 1))

        except Exception as e:
            print(f"Failed: {url}, error: {e}")

    return {"status": "done", "pages_crawled": len(visited)}