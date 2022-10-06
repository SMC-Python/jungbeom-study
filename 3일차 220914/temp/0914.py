import requests

# https://controlc.com/index.php?act=submit


# psot에 사용할 paste_title, input_text를 입력받음 
title = input('제목 입력')
text = input('내용 입력')

response = requests.post(
    "https://controlc.com/index.php",
    # 파라미터
    params={
        'act' : 'submit'
    },

    # payload 에 뜨는 form data
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

    # 웹 서버에서 공격을 한다고 정한 기준을 피하기 위해
    # 브라우저에서 요청하는 것과 최대한 비슷하게 요청하기 위해 header도 작성해줌
    headers={
        'referer' : 'https://controlc.com/'
    }
)


# 사이트를 저장
with open(
    'C:/Users/user/Desktop/temp/temp.html',
    'w',
    encoding='utf-8'
)as f:
    f.write(response.text)
