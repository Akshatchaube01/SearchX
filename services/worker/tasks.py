from celery_app import celery_app

from crawler.fetcher import fetch_page
from crawler.cleaner import clean_html
from crawler.link_extractor import extract_links

from search.elastic import index_document


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

            html = fetch_page(url)

            text = clean_html(html)

            index_document(url, text)

            print(f"Indexed: {url}")

            links = extract_links(url, html)

            for link in links:

                if link not in visited:
                    queue.append((link, depth + 1))

        except Exception as e:

            print(f"Failed: {url}, error: {e}")

    return {
        "status": "done",
        "pages_crawled": len(visited)
    }