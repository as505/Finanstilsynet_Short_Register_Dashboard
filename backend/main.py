from fastapi import FastAPI, HTTPException
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
	# for hosting on the web this needs to be changed to point to the frontend host
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_root(q: str | None = None):
	return{"Welcome"}

# Helper function to check if ID is within bounds
def confirm_idx(id:int, list, errorMessage):
	if (id >= len(list)):
		raise HTTPException(status_code=404, detail=errorMessage)
	return


# Returns an instrument item by id,
INSTRUMENT_ID_PATH = "/instrument/{id}"
@app.get(INSTRUMENT_ID_PATH)
def get_instrument_id(id: int):	
	confirm_idx(id, INSTRUMENT_DATA, "Instrument ID not found")
	return INSTRUMENT_DATA[id]


@app.get(INSTRUMENT_ID_PATH + "/events")
# event index needs to be a string instead of an int, otherwise event=0 would be considered None
def get_instrument_events(id: int, event: str | None = None, p: bool = False):
	instrument = get_instrument_id(id)
	eventList = instrument['events']
	if event:
		# Convert from string to int to index list
		event = int(event)
		if p:
			positionList = eventList[event]['activePositions']
			return positionList
		return eventList[event]
	else:
		return eventList




@app.get("/instruments")
def get_all_instruments():
	return INSTRUMENT_DATA


@app.get("/num_instruments")
def get_num_instruments():
	return {'count' : len(INSTRUMENT_DATA)}