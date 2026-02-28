from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import json
import pathlib

app = FastAPI()
# Not exposed to the frontend
DATASET_URL = "https://ssr.finanstilsynet.no/api/v2/instruments"
# Get and store dataset in memory when server is started
INSTRUMENT_DATA = list()
data = requests.get(DATASET_URL).json()
for inst in data:
	INSTRUMENT_DATA.append(inst)

app.add_middleware(
	# We allow all origins since this runs on localhost, 
	# for hosting on the web this needs to be changed to point to the actual frontend
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_root():
	return{"Welcome"}

@app.get("/instrument/{id}/")
def get_instrument_id(id):	
	return[INSTRUMENT_DATA[int(id)]]


@app.get("/instruments")
def get_all_instruments():
	return[INSTRUMENT_DATA]