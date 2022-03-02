from tinydb import TinyDB, where

db = TinyDB("./database.json")

def addToken(token):
    table = db.table("tokens")
    table.insert({"token": token})

def removeToken(token):
    table = db.table("tokens")
    table.remove(where("token") == token)
    
def tokenExists(token):
    table = db.table("tokens")
    return len(table.search(where("token") == token)) > 0

def getAllTokens():
    table = db.table("tokens")
    result = map(lambda x: x["token"], table.all())
    return list(result)

def addEvent(event):
    table = db.table("events")
    eventResult = {
        "id": event.id,
        "name": event.name,
        "date": event.date.strftime("%m/%d/%Y, %H:%M"),
        "price": event.price,
        "seats": event.seats,
        "seatsRemaining": event.seatsRemaining,
        "location": event.location
    }
    table.insert(eventResult)
    
def getAllEvents():
    table = db.table("events")
    return table.all()

def eventExists(event):
    table = db.table("events")
    return len(table.search(where("id") == event.id)) > 0