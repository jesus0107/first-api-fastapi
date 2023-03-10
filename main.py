import json
from uuid import uuid4
from typing import List
# ------ FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import Body

# ------ Models
from models import User, UserLogin, UserRegister, Tweet


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
def singup(user: UserRegister = Body()):
    """ Register a user in the app

    Parameters: 
        - Request body parameter
            - user: UserRegister    
    Returns a json with the basic user information
        - user_is: UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - birth_date: datetime

    """
    with open("users.json", "r+", encoding="utf8") as file:
        data = json.loads(file.read())
        user_register = dict(user)
        user_register['user_id'] = str(user_register['user_id'])
        user_register['birth_date'] = str(user_register['birth_date'])
        data.append(user_register)
        file.seek(0)
        file.write(json.dumps(data))
        return user


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
    """ Show all users in the app

    Parameters: 
        -    
    Returns a json with the basic user information
        - user_is: UUID
        - email: Emailstr
        - first_name: str
        - last_name: str
        - birth_date: datetime

    """
    with open("users.json", "r", encoding="utf-8") as f:
        data = json.loads(f.read())
        return data

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
    response_model=List[Tweet],
    status_code=status.HTTP_200_OK,
    summary="Get all Tweets",
    tags=["Tweets"]
)
def home():
    """ Show all tweets in the app

    Parameters: 
        -    
    Returns a json with the basic tweet information
        tweet_id: UUID 
        content: str 
        created_at: datetime 
        updated_at: Optional[datetime]
        by: User

    """
    with open("tweets.json", "r", encoding="utf-8") as f:
        data = json.loads(f.read())
        return JSONResponse(data)


@app.post(
    path=("/post"),
    response_model=Tweet,
    status_code=status.HTTP_201_CREATED,
    summary="Post a tweet",
    tags=["Tweets"]
    )
def post(tweet: Tweet = Body()):
    """ Post a tweet in the app

    Parameters: 
        - Request body parameter
            - tweet: Tweet    
    Returns a json with the basic user information
        tweet_id: UUID 
        content: str 
        created_at: datetime 
        updated_at: Optional[datetime]
        by: User 

    """
    with open("tweets.json", "r+", encoding="utf8") as file:
        #Cargar los datos desde el archivo
        data = json.loads(file.read())
        #Convirtiendo el objeto tweet a un archivo json
        json_compatible_tweet_data = jsonable_encoder(tweet)
        #Gregando el tweet en formato json a la data
        data.append(json_compatible_tweet_data)

        #Moviendo el puntero al principio del diccionario del archivo
        file.seek(0)
        #Escribiendo la data modificada en el archivo(file), por medio del metodo dump
        json.dump(data, file, indent=4)
        #Truncar el archivo al los datos escritos
        file.truncate()
        #JSONResponse -> toma la data que es pasada por parametros y retrna un json codificado
        return JSONResponse(content=data)


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