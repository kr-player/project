import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=%EB%89%B4%EC%8A%A4"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    title_elements = soup.find_all("div", class_="n0jPhd ynAwRc MBeuO nDgy9d")

    for title_element in title_elements:
        title_text = title_element.text
        print(title_text)
