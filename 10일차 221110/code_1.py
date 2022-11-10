import json
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

def _get_auctions() -> list :
    # auctions.json 파일 내용을 반환
    with open('./auctions.json', 'r', encoding='utf-8') as f :
        return json.loads(f.read())

def _save_acutions(auctions : list) :
    # auctions 인자를 auctions.json에 저장
    with open('./auctions.json', 'w', encoding='utf-8') as f :
        f.write(json.dumps(auctions, ensure_ascii=False))

app = FastAPI()

# uvicorn code_1:app --reload


@app.get('/apis/auctions')
def get_auctions() :
    return _get_auctions()

@app.get('/auctions')
def auctions() :
    with open('./auctions.html', 'r', encoding='utf-8') as f :
        return HTMLResponse(f.read())
