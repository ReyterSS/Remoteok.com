import re
import requests
from bs4 import BeautifulSoup
import json
from collections import OrderedDict

from lxml import etree
from selenium.webdriver.common.by import By

# data = {
#     'authority': 'remoteok.com',
#     'method': 'GET',
#     'path': '/',
#     'scheme': 'https',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#     'Cache-Control':'max-age=0',
#     'Cookie': 'ref=https%3A%2F%2Fwww.google.com%2F; new_user=false; visits=3; visit_count=3; adShuffler=1',
#     'Sec-Ch-Ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
#     'Sec-Ch-Ua-Mobile': '?0',
#     'Sec-Ch-Ua-Platform': '"Windows"',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'none',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
# }
url = 'https://remoteok.com/'
HOST = 'https://remoteok.com'

for i in range(0,1000, 20):
    url2 = f'https://remoteok.com/?&action=get_jobs&offset={i}'
    data2 = {
        'authority': 'remoteok.com',
        'method': 'GET',
        'path': f'/?&action=get_jobs&offset={i}',
        'scheme': 'https',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': 'ref=https%3A%2F%2Fwww.google.com%2F; new_user=false; cf_clearance=sbfm.ApPOqyh9GMeBZsd2ct57SIq_Tgh_I1U7T8QwjU-1696583544-0-1-4dc2ac5.2e45a725.53dd7525-250.0.0; logged_in_token=reyter_a8fce7b9b82a6596036a25637a0d0182; PHPSESSID=hqbpmqdcc4ujcespri5pcbmi1d; visit_count=9; visits=18; adShuffler=0',
        'Referer': 'https://remoteok.com/',
        'Sec-Ch-Ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest`'
        }
    try:
        r = requests.get(url2, headers=data2)
        soup = BeautifulSoup(r.text, 'html.parser')
        all_data = []

        title2 = soup.find_all(attrs={'itemprop': 'title'})
        for a in title2:
            title = a.text.strip()
            all_data.append(title)
        company2 = soup.find_all(attrs={'itemprop':'name'})#[1:2]
        for b in company2:
            company = b.text.strip()
        salary2 = soup.find_all('div', class_='location')  # [1]
        for i in salary2:
            if i and re.search(r'💰', str(i)):
                salary = i.text.strip()
                all_data.append(salary)
            else:
                pass
        direction2 = soup.find_all('td', class_='tags')
        for i in direction2:
            direction = i.text.strip()
            all_data.append(direction)
        vacation_url1 = soup.find_all(attrs={'itemprop':"url"})
        for d in vacation_url1:
            vacation_url = HOST + d.get('href')
            all_data.append(vacation_url)

        post_days2 = soup.find_all('td', class_='time')#.text
        for i in post_days2:
            post_days = i.text.strip()
            all_data.append(post_days)
        print(all_data)

    except:
        pass
