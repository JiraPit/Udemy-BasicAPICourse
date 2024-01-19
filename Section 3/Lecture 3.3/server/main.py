from fastapi import FastAPI
from server.models.fruit_model import FruitModel

app = FastAPI()

fruits = [
    FruitModel(name="Apple",price=20),
    FruitModel(name="Orange",price=40),
    FruitModel(name="Grapes",price=60),
]

@app.get("/fruits")
def get_fruit():
    return fruits

@app.post("/fruits")
def add_fruit(fruit:FruitModel):
    fruits.append(fruit)
    return "success"