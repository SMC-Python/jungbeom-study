from fastapi import FastAPI, HTTPException, Path
import json

# 새로운 유저 만들기
# 유저 1의 정보 가져오기        POST/users
# 유저 1 삭제하기               GET/users/1
# 유저 1의 글들 가져오기        DELETE/users/1
# 유저 1의 글들 중 글 1 삭제하기 GET/users/posts
# 유저 1의 글들 중 글 1 삭제하기 DELETE/users/1/posts/1

# 경매 목록 가져오기               GET/autions
# 경매 목록 중 두분째 경매 가져오기 GET/autions/2
# 경매 목록 중 두번째 경매 삭제하기 DELETE/auctions/2

app = FastAPI()

def _get_auctions() -> list:
    # auctions.js
    with open('./auctions.json', encoding='utf-8') as f :
        return json.loads(f.read())

def _save_auctions(auctions: list) :
    with open('./auctions.json', 'w', encoding='utf-8') as f :
        f.write(json.dumps(auctions, ensure_ascii = False))

@app.get('/')
def ok() :
    return {'status' : 'ok'}

@app.get('/auctions')
def get_auctions() :
    return _get_auctions()

@app.get('/auctions/{id}')
def get_auction(id: int = Path(gt=0)) :
    try : 
        return _get_auctions()[id - 1]
    except IndexError :
        raise HTTPException(404)

# uvicorn code_1:app --reload

# 1. json에거 전체 경매 목록을 불러온다
# 2. 전체 경매 목록에서 n번째 삭제
# 3. 삭제되고 남은 나머지 목록을 json에 저장한다

@app.get('/delete/{id}')
def delete_auction(id: int = Path(gt=0)) :
    try : 
        auction_list = _get_auctions()
        auction_list.pop(id - 1)
        _save_auctions(auction_list)
    except IndexError :
        raise HTTPException(404)