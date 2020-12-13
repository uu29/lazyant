from clien import get_url, get_last_page, get_contents
from db import insert_item_many

SEARCH_WORD = "테슬라"
url = get_url(SEARCH_WORD)
last_page = get_last_page(url)
contents = get_contents(url, SEARCH_WORD, last_page)
insert_item_many(contents, 'clien', 'tesla')