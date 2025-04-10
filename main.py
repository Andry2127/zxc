import re

from bs4 import BeautifulSoup
from aiohttp import ClientSession
import asyncio
from requests_html import HTMLSession,AsyncHTMLSession
from fastapi import FastAPI, Path, Query, HTTPException, status
from fastapi.responses import JSONResponse





async def fetch_url_with_aiohttp(url: str) -> str:
    async with ClientSession() as session :
        response = await session.get(url)
        if response.status == 200:
            return await response.text(encoding="utf-8")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    

async def fetch_url_with_request_html(url: str) -> str:
        session = AsyncHTMLSession()
        response = await session.get(url)
        if response.status_code == 200:
            return response.html
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
       



def get_html(url: str) -> str:
    session = HTMLSession()
    response = session.get(url)
    return response.text



url = "https://naruto.wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0"
tag = "div"
found_text = "Добро пожаловать в Нарутопедию"



# ----------------------------------------------------------------------------------

# html = asyncio.run(fetch_url_with_aiohttp(url))

# soup = BeautifulSoup(html, "lxml")
# text = soup.find(string=re.compile(found_text)).find_parent(tag)

# if text:
#      print("text=", text.text)
#      print("get_text=", text.get_text())
# else:
#      print("not found")

# ----------------------------------------------------------------------------------

html = asyncio.run(fetch_url_with_request_html(url))

strings = html.xpath(f'//{tag}[contains(., "{found_text}")]//text()')

if strings :
     text = "".join(strings).replace("\n","")
     print(f"{text=}")
else:
     print("not found")

# ----------------------------------------------------------------------------------




# html = asyncio.run(fetch_url(url))
# html = get_html(url)
# soup = BeautifulSoup(html, "lxml")

# text = soup.div.p.text
# strings = soup.table.find_all_next("li")
# for text in strings:
#     print(text.text)


# text = soup.div(class_="main_hello")
# text = "".join([string.text for string in text])

# print(text)








