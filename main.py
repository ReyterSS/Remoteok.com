import re
import requests
from bs4 import BeautifulSoup

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

for i in range(0,20, 20):
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
        all_blocks = soup.find_all('tr')
        all_data = []
        for i in all_blocks:
            title2 = i.find_all(attrs={'itemprop': 'title'})
            for a in title2:
                title = a.text.strip()
                all_data.append(title)
            company2 = i.find_all(attrs={'itemprop':'name'})
            for b in company2:
                company = b.text.strip()
                all_data.append(company)
            region2 = i.find_all('div', class_='location')
            # for c in region2:
            # regions = re.findall(r"💰 (.*) 💰", region2, re.DOTALL)
            #     # each_string = i.find_all(string=re.compile('💃'| '🌏'| '🇪🇺'))
            #     each_string = re.search(r' 💰 ', c)
            salary_=[]
            salary2 = i.find('div', class_='location')#[1]
            # for i in salary2:
            #     salary_.append(i)
            # salary_clear = re.sub(r"[;,\s]", ' ', str(salary2))
            # print(salary2)
                # between = re.findall(r"💰(.*)💰", i, re.DOTALL)
                # print(between)
                # if i and re.search(r'💰', str(i)):
                #     # prev = i.find_previous_siblings()
                #     salary = i.text.strip()
                #     print()
                #     all_data.append(salary)
                # else:
                #     pass
            direction2 = i.find_all('td', class_='tags')
            for e in direction2:
                direction = e.text.split()
                all_data.append(direction)
            post_days2 = i.find_all('td', class_='time')#.text
            for f in post_days2:
                post_days = f.text.strip()
                all_data.append(post_days)
    except:
        pass

abracadabra5






        # print(all_blocks)
        #
        # title2 = soup.find_all(attrs={'itemprop':'title'})
        # for i in title2:
        #     title = i.text.strip()
        #     all_data.append(title)
        # company2 = soup.find_all(attrs={'itemprop':'name'})
        # for i in company2:
        #     company = i.text.strip()
        #     all_data.append(company)
        # region2 = soup.find_all('div', class_='location')
        # for i in region2:
        #     print(i)
        #     # for b in i:
        #     #     region=
        # #     r = re.search(r'💰(.*)$', i)
        # #
        # #     region1 = i.find_previous_siblings(r)
        #     # region = i.text.strip()
        #     # all_data.append(region)
        # # print(region2)
        # salary2 = soup.find_all('div', class_='location')#[1]
        # for i in salary2:
        #     if i and re.search(r'💰', str(i)):
        #         salary = i.text.strip()
        #         all_data.append(salary)
        #     else:
        #         pass
        # direction2 = soup.find_all('td', class_='tags')
        # for i in direction2:
        #     direction = i.text.strip()
        #     all_data.append(direction)
        # post_days2 = soup.find_all('td', class_='time')#.text
        # for i in post_days2:
        #     post_days = i.text.strip()
        #     all_data.append(post_days)
        # print(all_data)



        # print(title, company, region, salary, direction, post_days)

        # dom = etree.HTML(soup)
        # job = dom.xpath('//*[contains(@tr, "data-offset")]')"a::attr(href)").getall()
        # job = soup.select('attr~=data-offset')#[attr~=value]
        # job = re.search(r"job job", str(soup))
        # print(soup
        # print(job)
    #         # dom = etree.HTML(str(soup))
    #         # main_block = soup.find('div', class_='page')
    #         # a_b = (dom.xpath('//*[contains(@id, "job")]'))
    #         # a_b = re.findall(r'data-offset', soup, re.DOTALL)
    #         # a_b = re.findall(r'job', soup)
    #         # a_b = re.findall(r'data-offset', soup, flags = re.DOTALL)
    #         job_urls_block = soup.find_all('a',class_='preventLink')
    #         # job_urls2 = []
    #         # job_urls = []
    #         for i in job_urls_block:
    #             job_url2 =  i.get('href')
    #             job_url = HOST + job_url2
    #         #     job_urls2.append(job_url)
    #         # for i in job_urls2:
    #         #     if i not in job_urls:
    #         #         job_urls.append(i)

# data3 = {
#     ':authority': 'remoteok.com',
#     ':method':'GET',
#     ':path': '/remote-jobs/remote-mid-senior-developer-laravel-php-ai-startup-for-wordpress-codewp-416968',
#     # 'path': f'{job_url2}',
#     ':scheme': 'https',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'ru - RU, ru; q = 0.9, en - US;q = 0.8, en;q = 0.7',
#     'Cache-Control': 'max - age = 0',
#     'Cookie': 'ref=https%3A%2F%2Fwww.google.com%2F; new_user=false; cf_clearance=sbfm.ApPOqyh9GMeBZsd2ct57SIq_Tgh_I1U7T8QwjU-1696583544-0-1-4dc2ac5.2e45a725.53dd7525-250.0.0; logged_in_token=reyter_a8fce7b9b82a6596036a25637a0d0182; PHPSESSID=hqbpmqdcc4ujcespri5pcbmi1d; visit_count=9; visits=27; adShuffler=1',
#     'Sec - Ch - Ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
#     'Sec - Ch - Ua - Mobile': '?0',
#     'Sec - Ch - Ua - Platform': '"Windows"',
#     'Sec - Fetch - Dest': 'document',
#     'Sec - Fetch - Mode': 'navigate',
#     'Sec - Fetch - Site': 'none',
#     'Sec - Fetch - User': '?1',
#     'Upgrade - Insecure - Requests': '1',
#     'User - Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 117.0.0.0Safari / 537.36'
# }
# r =requests.get('https://remoteok.com/remote-jobs/remote-mid-senior-developer-laravel-php-ai-startup-for-wordpress-codewp-416968',data = data3)
# soup3 = BeautifulSoup(r.text, 'lxml')
# print(r.text)


        # all_blocks.append(a_b)
        # title = a_b.find(attrs={'itemprop':'title'}).text
        # company = a_b.find(attrs={'itemprop':'name'}).text
        # region = a_b.find('div', class_='location').text
        # salary =a_b.find_all('div', class_='location')[1].text
        # direction =a_b.find('td', class_='tags').text
        # post_days = a_b.find('td', class_='time').text
        # print(title, company, region, salary, direction, post_days)



# for i in all_blocks:
#     block = i.find('data0offset')
# all_blocks = re.findall(r'data-offset', main_block)
# (r'of(.*)titles', main_block, re.DOTALL)
# for i, num in enumerate(main_block, start=1):
# for i in all_blocks:
#     name = i.find('a', class_="preventLink").find('title').text
#     #'@##=By.XPATH, '//*[@class="preventLink"]//*[@*="title"]')
#     print(i)


