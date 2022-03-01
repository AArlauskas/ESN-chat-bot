import sched, time
import eventsService
from event import Event
import repository
import botSender

s = sched.scheduler(time.time, time.sleep)

def checkEvents(): 
    print("Checking events")
    eventsResponse = eventsService.getNowEvents()
    for item in eventsResponse:
        event = Event(item)
        if not repository.eventExists(event):
            repository.addEvent(event)
            botSender.sendNewEventMessage(event)
    s.enter(10, 1, checkEvents)

def initEventChecker():
    s.enter(10, 1, checkEvents)
    s.run()