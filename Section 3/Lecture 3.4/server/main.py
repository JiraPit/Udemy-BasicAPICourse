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
    if fruit.price == None:
        return "price is not provided"
    fruits.append(fruit)
    return "success"

@app.delete("/fruits")
def delete_fruit(fruit:FruitModel):
    for f in fruits:
        if f.name.lower() == fruit.name.lower():
            fruits.remove(f)
    return "success"

@app.put("/fruits")
def update_fruit(fruit:FruitModel):
    if fruit.price == None:
        return "price is not provided"
    for f in fruits:
        if f.name.lower() == fruit.name.lower():
            f.price = fruit.price
    return "success"