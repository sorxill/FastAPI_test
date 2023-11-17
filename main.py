import uvicorn
from fastapi import FastAPI
from pydantic import EmailStr, BaseModel

app = FastAPI()


class CreateUser(BaseModel):
    email: EmailStr


@app.get('/hello/')
def say_hello(name: str = "World"):
    name = name.strip().title()
    return {
        "Message": f"Hello, {name}"
    }


@app.post('/users/')
def create_user(user: CreateUser):
    return {
        "message": "success",
        "email": user.email
    }


@app.get('/item/latest/')
def get_latest_item():
    return {
        "id": 0,
        "message": "latest"
    }


@app.get('/item/{item_id}/')
def get_items(item_id: int):
    return {
        "item": {
            "id": item_id
        },
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
