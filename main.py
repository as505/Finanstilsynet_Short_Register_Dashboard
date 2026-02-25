from fastapi import FastAPI
import requests

API_ROOT_URL = "https://ssr.finanstilsynet.no/api/v2/"

app = FastAPI()

@app.get("/")
def get_root():
	return{"Welcome"}

@app.get("/instruments")
def get_instruments():
	data = requests.get(API_ROOT_URL+"instruments").json()
	return[data]