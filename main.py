from typing import List
# ------ FastAPI
from fastapi import FastAPI
from fastapi import status

# ------ Models
from models import User, UserLogin, Tweet


app = FastAPI()

# Path operations
## Users
@app.post(
    path="/singup",
    response_model=User,
    status_code=status.HTTP_201_CREATED,
    summary="Register a user",
    tags=["User"]
    )
def singup():
    return 0

@app.post(
    path="/login",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Login a user",
    tags=["User"]
    )
def login():
    return 0

@app.get(
    path="/users",
    response_model=List[User],
    status_code=status.HTTP_200_OK,
    summary="Get all users",
    tags=["User"]
    )
def get_users():
    return 0

@app.get(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Get a user",
    tags=["User"]
    )
def get_user():
    return 0

@app.delete(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Delete a user",
    tags=["User"]
    )
def delete_user():
    return 0

@app.put(
    path="/users/{user_id}",
    response_model=User,
    status_code=status.HTTP_200_OK,
    summary="Update a user",
    tags=["User"]
    )
def update_user():
    return 0

## Tweets

@app.get(
    path="/",
    # response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Get all Tweets",
    tags=["Tweets"]
)
def home():
    return {"Twitter api": "Working"}

@app.post(
    path=("/post"),
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["Tweets"]
)
def post():
    return 0

@app.get(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Get a Tweet",
    tags=["Tweets"]
)
def get_tweet():
    return 0

@app.delete(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Delete a tweet",
    tags=["Tweets"]
    )
def delete_tweet():
    return 0

@app.put(
    path="/tweets/{tweet_id}",
    response_model=Tweet,
    status_code=status.HTTP_200_OK,
    summary="Update a tweet",
    tags=["Tweets"]
    )
def update_tweet():
    return 0