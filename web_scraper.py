import requests
from bs4 import BeautifulSoup
from datetime import datetime

# URL of the news website
URL = "https://www.bbc.com/news"

# Set user-agent to mimic a browser
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def fetch_headlines():
    try:
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status()  # Raise error for bad responses

        soup = BeautifulSoup(response.text, "html.parser")

        # Find all h2 tags (common for headlines)
        headlines = soup.find_all("h2")

        # Extract text and clean
        titles = [title.get_text(strip=True) for title in headlines if title.get_text(strip=True)]

        # Save to a text file with timestamp
        file_name = f"headlines_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        with open(file_name, "w", encoding="utf-8") as f:
            for idx, title in enumerate(titles, start=1):
                f.write(f"{idx}. {title}\n")

        print(f"\n✅ Scraped {len(titles)} headlines and saved to '{file_name}'")

    except requests.RequestException as e:
        print("❌ Failed to fetch news:", e)

if __name__ == "__main__":
    fetch_headlines()
