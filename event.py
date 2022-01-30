from datetime import datetime

class Event(object):
    def __init__(self, event):
        if "id" in event:
            self.id = event["id"]
            self.name = event["name"]
            self.date = event["date"]
            self.price = event["price"]
            self.seats = event["seats"]
            self.seatsRemaining = event["seatsRemaining"]
        else:
            self.id = event["_id"]
            self.name = event["name"]
            self.date = datetime.utcfromtimestamp(float(event["datetime"]) / 1000)
            self.price = event["regularPrice"]
            self.seats = event["seats"]
            self.seatsRemaining = event["seatsRemaining"]

    def toString(self):
        return "Event's name: {}\nDate: {}\nPrice: {}\nSeats: {} \nRemaining seats: {}".format(self.name,
                                                                   self.date,
                                                                   self.price,
                                                                   self.seats,
                                                                   self.seatsRemaining)