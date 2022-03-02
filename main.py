import botReceiver
import eventsChecker
import heartbeatService
from env import HEARTBEAT_ON

def main():
    botReceiver.initTelegram()
    if HEARTBEAT_ON:
        heartbeatService.initialiseBeating()
    eventsChecker.initEventChecker()
main()