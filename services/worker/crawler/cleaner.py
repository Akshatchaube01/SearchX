from bs4 import BeautifulSoup


def clean_html(html):
    soup = BeautifulSoup(html, "html.parser")

    for tag in soup([
        "script",
        "style",
        "noscript",
        "header",
        "footer",
        "nav",
        "aside"
    ]):
        tag.decompose()

    text = soup.get_text(separator=" ")

    return " ".join(text.split())


def extract_title(html):
    """Extract page title from HTML"""
    soup = BeautifulSoup(html, "html.parser")
    
    # Try to get title tag first
    title_tag = soup.find("title")
    if title_tag:
        return title_tag.get_text().strip()
    
    # Fallback to h1
    h1_tag = soup.find("h1")
    if h1_tag:
        return h1_tag.get_text().strip()
    
    return ""