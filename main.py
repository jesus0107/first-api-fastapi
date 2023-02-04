# ------ Models
from models import User, UserLogin, Tweet

# ------ FastAPI
from fastapi import FastAPI


app = FastAPI()


@app.get(path="/")
def home():
    return {"Twitter api": "Working"}