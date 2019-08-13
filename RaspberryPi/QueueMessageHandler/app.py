import AZ.base as base
import AZ.az_queue as az_queue
from time import sleep
import datetime as dt
import messageConfigs
import messageHandlers


def callback(message):

    if message in messageConfigs.supportedMessages:
        messageConfigs.supportedMessages[message]()
    else:
        messageHandlers.handle_unknown(message)

    print('Message Processed!')


if __name__ == '__main__':
    account = base.get_account()
    que_name = 'testqueue'
    print('starting %s' % dt.datetime.now().strftime('%d-%m-%Y %H:%M'))
    while True:
        try:
            print('Dequeue')
            az_queue.dequeue(account, que_name, callback)
            sleep(5)
        except KeyboardInterrupt:
            print('Queue Interrupted by user')
