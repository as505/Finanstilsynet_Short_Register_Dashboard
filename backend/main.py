from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests


app = FastAPI()
# Not exposed to the frontend
DATASET_URL = "https://ssr.finanstilsynet.no/api/v2/instruments"
# Get and store dataset in memory when server is started
INSTRUMENT_DATA = list()
INSTRUMENT_NAMES = list()
data = requests.get(DATASET_URL).json()
for inst in data:
	INSTRUMENT_DATA.append(inst)
	INSTRUMENT_NAMES.append(inst['issuerName'])



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
def confirm_valid_idx(id:int, list, errorMessage):
	if (id >= len(list)):
		raise HTTPException(status_code=404, detail=errorMessage)


# Returns an instrument item by id,
@app.get("/instrument/{id}")
def get_instrument(id: int):	
	confirm_valid_idx(id, INSTRUMENT_DATA, "Instrument not found")
	return INSTRUMENT_DATA[id]	


@app.get("/instrument/{id}/events")
def get_instrument_event_list(id: int):
	# Index is checked for validity in 'get_instrument_id()'
	instrument = get_instrument(id)
	return instrument['events']


@app.get("/instrument/{id}/{eventID}")
def get_instrument_event(id:int, eventID:int):
	eventList = get_instrument_event_list(id)
	confirm_valid_idx(eventID, eventList, "Event not found in instrument")
	return eventList[eventID]


@app.get("/instrument/{id}/{eventID}/positions")
def get_event_position_list(id:int, eventID:int):
	event = get_instrument_event(id, eventID)
	return event['activePositions']

@app.get("/instrument/{id}/{eventID}/positionCount")
def get_event_positions_count(id:int, eventID:int):
	event = get_instrument_event(id, eventID)
	return len(event['activePositions'])


@app.get("/instrument/{id}/{eventID}/{positionID}")
def get_event_position(id:int, eventID:int, positionID:int):
	positionList = get_event_position_list(id, eventID)
	confirm_valid_idx(positionID, positionList, "Position not found in event")
	return positionList[positionID]


@app.get("/instruments")
def get_all_instruments():
	return INSTRUMENT_NAMES


@app.get("/num_instruments")
def get_num_instruments():
	return len(INSTRUMENT_DATA)