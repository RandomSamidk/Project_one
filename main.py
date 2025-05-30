from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"output":"WELOCOME TO HOME PAGE"}


