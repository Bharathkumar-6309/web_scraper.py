# web_scraper.py
Scrape top news headlines from a public news website (e.g., BBC News).

Use requests to fetch the HTML content.

Use BeautifulSoup to parse <h2> tags (or similar).

Save the extracted headlines into a .txt file with a timestamp.

Python 3.x installed

Install required libraries:

bash
pip install requests beautifulsoup4
Requests is used to fetch live web page content.

BeautifulSoup is used to extract all <h2> tag contents.

Headlines are cleaned and written into a .txt file.

Connects to https://www.bbc.com/news

Parses all <h2> tags for headlines

Saves them in a file like headlines_2025-07-19_17-30-00.txt
A .txt file with numbered news headlines.

Example:
1. Wildfire spreads rapidly in Greece
2. Global markets fall amid inflation fears
   
