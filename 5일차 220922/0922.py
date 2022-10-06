from bs4 import BeautifulSoup
import requests

title = input('제목 입력:')
content = input('내용 입력:')

response = requests.post(
    'https://controlc.com/index.php',
    params={
        'act' : 'submit'
    },

    data={
        'subdomain' : '',
        'antispam' : '1',
        'website' : '',
        'paste_title' : title,
        'input_text' : content,
        'timestamp' : '1503c4774cf81847fce13669ff49bc90',
        'paste_password' : '',
        'code' : '0'
    },

    headers={
        'referer' : 'https://controlc.com/'
    }
)

soup1 = BeautifulSoup(response.text, 'html.parser')
url_element = soup1.select_one('#wrapper > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > form > input')
url = url_element.attrs['value']

print('생성된 url은',url,'입니다')

response2 = requests.get(url)
soup2 = BeautifulSoup(response2.text, 'html.parser')
title_element =soup2.select_one('#pastecontainer > div:nth-child(1) > div:nth-child(2)')
title = title_element.get_text()

print('생성된 제목은',title,'입니다')