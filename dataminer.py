
import requests
from bs4 import BeautifulSoup
import pandas as pd

#  Define the target website
url = "http://quotes.toscrape.com/"

#  Send a request to fetch the webpage content
response = requests.get(url)
if response.status_code == 200:
    html_content = response.text
else:
    print("Failed to fetch the webpage")
    exit()

#  Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

#  Extract relevant data (quotes and authors)
quotes_data = []
quotes = soup.find_all("div", class_="quote")

for quote in quotes:
    text = quote.find("span", class_="text").get_text()
    author = quote.find("small", class_="author").get_text()
    quotes_data.append({"Quote": text, "Author": author})

#  Save data into CSV using pandas
df = pd.DataFrame(quotes_data)
df.to_csv("quotes.csv", index=False)

print("Data has been scraped and saved to quotes.csv")
