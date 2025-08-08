import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find and print all the heading tags (h1, h2, h3)
        headings = soup.find_all(['h1', 'h2', 'h3'])
        
        print(f"Headings found on {url}:")
        for heading in headings:
            print(heading.get_text())

    except requests.exceptions.RequestException as e:
        print(f"Error during web request: {e}")

# Scrape a hypothetical website
url_to_scrape = "http://example.com"
scrape_website(url_to_scrape)