import camera
import AZ.storage as storage
import AZ.base as base

account = base.get_account()


def handle_video_capture():
    print('Capturing Video...')
    path = 'vid.h264'
    camera.capture_video(path, 5)
    container_name = 'pythonsdk'
    print('Uploading Video...')
    storage.upload(account, container_name, path, path)


def handle_unknown(message):
    print('Unknown message received: ' + message)
