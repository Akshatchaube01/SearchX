from bs4 import BeautifulSoup
from urllib.parse import urljoin


def extract_links(base_url, html):

    soup = BeautifulSoup(html, "html.parser")

    links = set()

    for tag in soup.find_all("a", href=True):

        href = tag["href"]

        full_url = urljoin(base_url, href)

        if full_url.startswith("http"):
            links.add(full_url)

    return links