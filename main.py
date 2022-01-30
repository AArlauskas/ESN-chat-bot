import botReceiver
import eventsChecker
import heartbeatService

def main():
    botReceiver.initTelegram()
    eventsChecker.initEventChecker()
    heartbeatService.initialiseBeating()
main()