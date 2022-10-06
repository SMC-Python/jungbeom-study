# 제목만 출력하기

from bs4 import BeautifulSoup
import requests

# controlc.com 에 post
title  = input("제목 입력 : ")
text = input("텍스트 입력 : ")

response_post = requests.post(
    'https://controlc.com/index.php',

    params={
        'act'  : 'submit'
    },

    data={
        'subdomain' : '',
        'antispam' : '1',
        'website' : '',
        'paste_title' : title,
        'input_text' : text,
        'timestamp' : '1503c4774cf81847fce13669ff49bc90',
        'paste_password' : '',
        'code' : '0'
    },

    headers={
        'referer' : 'https://controlc.com/'
    }
)

url = response_post.text
soup = BeautifulSoup(url, 'html.parser')
get_link = soup.select_one('#wrapper > div.rounded10.whiteBG.pad20 > div.successfull > div.input-copy > form > input[type=text]')['value']

print('당신의 메모 url : ', get_link)

response_get = requests.get(get_link)

html = response_get.text
soup = BeautifulSoup(html, 'html.parser')
title_get = soup.select_one('#pastecontainer > div.whiteBG.rounded10.pad10 > div:nth-child(2)').text

print("제목 : ", title_get)