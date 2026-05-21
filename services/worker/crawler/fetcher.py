import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def fetch_page(url):
    session = requests.Session()
    
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504]
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    
    headers = {
        "User-Agent": "SearchX-Bot/1.0"
    }
    
    response = session.get(url, timeout=10, headers=headers)

    response.raise_for_status()

    return response.text