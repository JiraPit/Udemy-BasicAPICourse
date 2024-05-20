from fastapi import FastAPI, Header, HTTPException
from resource_server.models.fruit_model import FruitModel
import requests

app = FastAPI()

fruits = [
    FruitModel(name="Apple", price=20),
    FruitModel(name="Orange", price=40),
    FruitModel(name="Grapes", price=60),
]


@app.get("/fruits")
def get_fruit():
    return fruits


@app.post("/fruits")
def add_fruit(fruit: FruitModel, token: str = Header(None)):
    if token is None:
        raise HTTPException(status_code=401, detail="Token is missing")
    user_id = identify(token)
    if user_id in ["123", "321"]:
        if fruit.price is None:
            return "price is not provided"
        fruits.append(fruit)
        return "success"
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


@app.delete("/fruits")
def delete_fruit(fruit: FruitModel, token: str = Header(None)):
    if token is None:
        raise HTTPException(status_code=401, detail="Token is missing")
    user_id = identify(token)
    if user_id in ["123", "321"]:
        for f in fruits:
            if f.name.lower() is fruit.name.lower():
                fruits.remove(f)
        return "success"
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


@app.put("/fruits")
def update_fruit(fruit: FruitModel, token: str = Header(None)):
    if token is None:
        raise HTTPException(status_code=401, detail="Token is missing")
    user_id = identify(token)
    if user_id in ["123", "321"]:
        if fruit.price is None:
            return "price is not provided"
        for f in fruits:
            if f.name.lower() == fruit.name.lower():
                f.price = fruit.price
        return "success"
    else:
        raise HTTPException(status_code=401, detail="Unauthorized")


def identify(token: str):
    response = requests.post(
        "http://127.0.0.1:8000/identify",
        json={
            "token": token,
        },
    )

    if response.status_code == 200:
        return response.json()
    else:
        return None
