import requests
import re
from bs4 import BeautifulSoup

a = int(input())
url = "https://minfin.com.ua/currency/chernigov/usd/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

title = soup.find("div", class_="sc-1x32wa2-9 bKmKjX")

if title:
    text = title.get_text("", strip=True)

    match = re.search(r"\d+,\d+", text)

    if match:
          number = round(float(match.group().replace(",", ".")))

          print(a/number)


