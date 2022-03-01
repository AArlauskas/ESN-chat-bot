import requests
import json

from env import ALL_URL, NOW_URL
from repository import getAllEvents

def getNowEvents():
    response = requests.get(NOW_URL)
    return json.loads(response.text)

def getAllEvents():
    response = requests.get(ALL_URL)
    return json.loads(response.text)

def getPostedEventsCount():
    return len(getAllEvents())
