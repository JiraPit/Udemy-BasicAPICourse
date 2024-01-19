from fastapi import FastAPI, Query

app = FastAPI()

fruits = ["Apple", "Banana", "Orange", "Mango", "Blueberry", 
          "Strawberry", "Pineapple", "Watermelon", "Grapes"]

@app.get("/fruits")
def get_fruit():
    return fruits

@app.get("/fruits/{number}")
def get_fruit_with_number(number: int):
    return fruits[number]

@app.get("/search-fruit")
def search_fruit(search: str = Query("")):
    result = []
    for fruit in fruits:
        if search.lower() in fruit.lower():
            result.append(fruit)
    return result


