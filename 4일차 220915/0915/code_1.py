import requests

title  = input("제목 입력 : ")
text = input("텍스트 입력 : ")

response = requests.post(
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

with open('./result1.html', 'w', encoding='utf-8') as f :
    f.write(response.text)