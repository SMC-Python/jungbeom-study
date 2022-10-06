from bs4 import BeautifulSoup
import requests


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
        'total': '1293',
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
        'Referer': 'https://auction.realestate.daum.net/v15/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

)

soup = BeautifulSoup(response.text, 'html.parser')
trs = soup.select('#frm_myreg > table > tbody > tr')

for tr in trs : 
    print(tr.select_one('td:nth-child(1) a').get_text())

print(len(trs))