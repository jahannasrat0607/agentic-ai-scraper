from Helpers.config import API_KEY
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup

def get_scrapeops_url(url, country="us"):
    payload = {
        "api_key": API_KEY,
        "url": url,
        "country": country,
        "render_js": "true",
        "device_type": "desktop"
    }
    return "https://proxy.scrapeops.io/v1/?" + urlencode(payload)

# Target URL
target_url = "https://www.amazon.com/s?k=headphones"
scrape_url = get_scrapeops_url(target_url)

# Make the request
response = requests.get(scrape_url)
print(scrape_url)
print(response.status_code)

# Print part of the raw HTML response
print(response.text[:1500])  # Print first 1500 chars to inspect structure

# Now try to extract product listings
soup = BeautifulSoup(response.text, "html.parser")
products = soup.select("div.s-main-slot div.s-result-item")

if not products:
    print("No product results found — check if selectors are correct or JS rendering is working.")
else:
    print(f"\nFound {len(products)} products. Showing top 5:\n")
    count = 0
    for product in products:
        title = product.select_one("h2 span.a-text-normal")
        price = product.select_one("span.a-price span.a-offscreen")
        if title and price:
            print(f"{title.get_text(strip=True)} - {price.get_text(strip=True)}")
            count += 1
        if count == 5:
            break
        