from datetime import datetime

class Event(object):
    def __init__(self, event):
        if "id" in event:
            self.id = event["id"]
            self.name = event.get("name", "Not Provided")
            self.date = event.get("date", "Not Provided")
            self.price = event.get("regularPrice", "Not Provided")
            self.seats = event.get("seats", "Not Provided")
            self.seatsRemaining = event.get("seatsRemaining", "Not provided")
            self.location = event.get("location", "Not provided")
        else:
            self.id = event["_id"]
            self.name = event.get("name", "Not Provided")
            self.date = datetime.utcfromtimestamp(float(event["datetime"]) / 1000)
            self.price = event.get("regularPrice", "Not Provided")
            self.seats = event.get("seats", "Not Provided")
            self.seatsRemaining = event.get("seatsRemaining", "Not provided")
            self.location = event.get("location", "Not provided")

    def toString(self):
        return "Event's name: {}\nDate: {}\nPrice: {} Eur\nLocation: {} \nSeats: {} \nRemaining seats: {}".format(self.name,
                                                                   self.date,
                                                                   self.price,
                                                                   self.location,
                                                                   self.seats,
                                                                   self.seatsRemaining)