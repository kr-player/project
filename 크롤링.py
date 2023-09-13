import requests
from bs4 import BeautifulSoup

# Google 검색 결과 페이지의 URL
url = "https://www.google.com/search?q=%EB%89%B4%EC%8A%A4"

# HTTP GET 요청을 보내서 페이지 내용을 가져옵니다.
response = requests.get(url)

# 요청이 성공했는지 확인합니다.
if response.status_code == 200:
    # BeautifulSoup를 사용하여 페이지의 HTML 내용을 파싱합니다.
    soup = BeautifulSoup(response.text, "html.parser")

    # 특정 클래스 이름을 가진 요소를 모두 찾습니다.
    title_elements = soup.find_all("div", class_="n0jPhd ynAwRc MBeuO nDgy9d")

    # 제목 텍스트를 추출하고 출력합니다.
    for title_element in title_elements:
        title_text = title_element.text
        print(title_text)
