from fastapi import FastAPI, HTTPException
from jose import jwt
from auth_server.model.auth_model import AuthModel
from auth_server.model.token_model import TokenModel


app = FastAPI()
SECRET = "112233"

users = {
    "123": "password1",
    "321": "password2",
}


@app.post("/login")
def login(auth: AuthModel):
    if auth.user_id not in users.keys():
        raise HTTPException(status_code=401, detail="Invalid user_id")

    if auth.password == users[auth.user_id]:
        payload = {"user_id": auth.user_id}
        token = jwt.encode(payload, SECRET)
        return token
    else:
        raise HTTPException(status_code=401, detail="Invalid password")


@app.post("/identify")
def identify(token: TokenModel):
    try:
        user = jwt.decode(token.token, SECRET)
        return user["user_id"]
    except:  # noqa: E722
        raise HTTPException(status_code=401, detail="Invalid token")
