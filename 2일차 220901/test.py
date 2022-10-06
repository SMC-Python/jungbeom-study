import requests
#  protocol   domain name    path           parameters
# https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=가나다

# requests 결과 값을 response에 저장
response = requests.get(
    # protocol
    "https://search.naver.com/search.naver",

    #parameters
    params={
        'where' : 'nexearch',
        'sm' : 'top_hty',
        'fbm' : '1',
        'ie' : 'uft8',
        'query' : '가나다'
    }
)

print(response.text)