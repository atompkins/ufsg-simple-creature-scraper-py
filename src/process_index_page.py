from bs4 import BeautifulSoup

from .get_html import get_html
from src.sqlite_writer import sql_writer
from urllib.parse import urlparse, parse_qs

async def process_index_page(session, url):
  html = await get_html(session, url)
  soup = BeautifulSoup(html, 'html.parser')
  items = soup.find_all('td', height='20')
  trs = [item.find_parent('tr').find_all('td') for item in items]
  sql_writer([
    tuple([
      parse_qs(urlparse(tds[0].find('a').get('href')).query)['creature_id'][0],
      tds[0].get_text(),
      tds[1].get_text(),
      tds[2].get_text(),
      tds[3].get_text(),
      tds[4].get_text(),
      tds[5].get_text(),
      tds[6].get_text(),
      tds[7].get_text(),
    ]) for tds in trs
  ])
  return soup.find('font', color='#FF0000').parent.find_next('a')
