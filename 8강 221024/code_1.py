from fastapi import FastAPI

app = FastAPI()


@app.get('/hello') #: 행위 / 자원
def hello() :
    return {'test' : 'hello'} #: 표현

@app.get('/users') #: 행위 / 자원
def create_user(username: str):
    return {'username' : username}

@app.post('/users') #: 행위 / 자원
def get_user(username: str):
    return {'username' : username}

@app.get('/users/{username}')
def get_user(username: str):
    return {'username' : username}

#/docs
#/redoc
# activate = uvicorn code_1:app --reload