from typing import Optional

from fastapi import FastAPI, Request
from pydantic import BaseModel
import json


app = FastAPI()


@app.get("/")
def read_root():
    return {"This is an": "API"}

class user(BaseModel):
    username: str
    password: Optional[str] = None
    flag: Optional[str] = "ELI{TH1S_1S_N0T_FL3G}"

@app.post("/users/")
async def get_json_info(request: Request):
    req = await request.json()
    if req["username"] == "5wixy" and req["password"] == "gyankel":
        return {'flag': "ELI{WH4T_4_R3QU3$T}"}
    else:
        return {'error': 'wrong username or password'}

@app.get("/users/")
def error_user():
    return {'error': 'wrong request type'}