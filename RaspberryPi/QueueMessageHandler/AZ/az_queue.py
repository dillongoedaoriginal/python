"""This is a wrapper library for azure storage queue"""
__author__ = "Dillon Goeda"


def enqueue(account, queuename, message):
    queue_service = account.create_queue_service()
    queue_service.put_message(queuename, message)


def create_queue(account, queuename):
    queue_service = account.create_queue_service()
    queue_service.create_queue(queuename)


def dequeue(account, queuename, callback):
    queue_service = account.create_queue_service()
    messages = queue_service.get_messages(queuename)
    for message in messages:
        callback(message.content)
        queue_service.delete_message(
            queuename, message.id, message.pop_receipt)
