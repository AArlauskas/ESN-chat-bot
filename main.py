import botReceiver
import eventsChecker
import heartbeatService
from env import HEARTBEAT_ON

def main():
    botReceiver.initTelegram()
    eventsChecker.initEventChecker()
    if HEARTBEAT_ON:
        heartbeatService.initialiseBeating()
main()