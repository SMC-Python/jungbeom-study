import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

response = requests.get(
    'https://auction.realestate.daum.net/ajax/main_list.php',

    params={
        'addr1': '서울',
        'result': '99',
        'yongdo': '99',
        'yongdo_detail': '99',
        'sort': '13D'
    },

    data={
        'total': '1304',
        'block': '2',
        'start': '',
        'next': '',
        'addr1': '서울',
        'addr2': '',
        'addr3': '',
        'bubcd': '',
        'kye': '',
        'local_num': '',
        'var_period': '',
        'result': '99',
        'var_kind': '',
        'yuchalcnt': '',
        'gamprice': '',
        'lowprice': '',
        'bdarea': '',
        'daejiarea': '',
        'ipchaltype': '',
        'bdname': '',
        'special': '',
        'addshow': '',
        'sort': '13D',
        'subMenuIdx': '1'
    },

    headers={
        'Origin': 'https://auction.realestate.daum.net',
        'Referer': 'https://auction.realestate.daum.net/v15/'
    }
)

soup =  BeautifulSoup(response.text, 'html.parser')
trs = soup.select('#frm_myreg > table > tbody > tr')
# print(len(trs))

datas = []
for tr in trs : 
    data={
        "사건번호 : ": tr.select_one('td:nth-child(1) a').get_text(),
        "물건용도 : ": tr.select_one('td:nth-child(2) > div:nth-child(2) > a > p:nth-child(1)').get_text(),
        "소재지   : ": tr.select_one('td:nth-child(2) > div:nth-child(2) > a > p:nth-child(2)').get_text(),
        "면적(㎡) : ": tr.select_one('td:nth-child(2) > div:nth-child(2) > p > span').get_text(),
        "감정     : ": tr.select_one('td:nth-child(3) > div:nth-child(1) > p').get_text(),
        "최저     : ": tr.select_one('td:nth-child(3) > div:nth-child(2) > p').get_text()
    }
    datas.append(data)
# pprint(datas)

with open('./code_1.json', 'w', encoding='utf-8') as f :
    f.write(json.dumps(datas, ensure_ascii=False))
    

