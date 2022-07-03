from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


while True:
    try:
        conn = psycopg2.connect(host='localhost',
                                port=49153,
                                database='fastapi',
                                user='postgres',
                                password='postgrespw',
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesful")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error:", error)
        time.sleep(2)


@ app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post)
    return{"data": "new post"}


@ app.get("/")
async def root():
    return {"message": "welcome 1"}
