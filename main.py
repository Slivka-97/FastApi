from fastapi import FastAPI
from schema import Book

app = FastAPI()


@app.get('/')
def home():
    return {
        "key": "hello",
        "value": "Word"
    }


@app.get('/{pk}')
def get_item(pk: int, q=None):
    return {
        'key': pk,
        'q': q
    }


@app.get('/user/{pk}/items/{items}/')
def get_user_item(pk: int, items: str):
    return {
        'user': pk,
        'item': items
    }


@app.post('/book')
def create_book(item: Book):
    return item
