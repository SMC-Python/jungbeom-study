from urllib import response
import requests
# https://dict.naver.com/search.dict?dicQuery=test&query=test&target=dic&ie=utf8&query_utf=&isOnlyViewEE=
response  = requests.get(
    "https://dict.naver.com/search.dict",

    params = {
        'dicQuery': 'test',
        'query' : 'test',
        'target' : 'dic',
        'ie' : 'utf8',
        'query_utf' : '',
        'isOnlyViewEE' : ''
    }
)

print(response.status_code)
