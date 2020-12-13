import requests
from bs4 import BeautifulSoup
import urllib

URL = "https://www.clien.net/service/search?sort=recency&boardCd=cm_stock&isBoard=true"

def get_url(search_word):
  encoding_search_word = urllib.parse.quote(search_word)
  url = f"{URL}&q={encoding_search_word}"
  return url

def get_last_page(url):
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  pages = soup.find("div", {"class": "board-nav-area"}).find_all("a")
  last_page = pages[-1].string
  return int(last_page)

def get_content(html):
  title = html.find("span", {"class": "list_subject"}).find("a")["title"]
  preview = html.find("div", {"class": "preview"}).find("span").string
  post_id = html["data-board-sn"]
  link_url = "https://www.clien.net/service/board/cm_stock"
  return {"title": title, "preview": preview, "link": f"{link_url}/{post_id}"}

def get_contents(url, search_word, last_page):
  contents = []
  for page in range(last_page):
    print(f"Scrapping Clien page: {page}")
    result = requests.get(f"{url}&p={page-1}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"data-role":"list-row"})
    for result in results:
      content = get_content(result)
      if search_word in content['title']:
        contents.append(content)
  return contents