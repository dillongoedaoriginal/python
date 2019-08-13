import camera
import AZ.storage as storage
import AZ.base as base
import subprocess
import ip_mailer

account = base.get_account()


def handle_video_capture():
    print('Capturing Video...')
    path = 'vid.h264'
    camera.capture_video(path, 5)
    container_name = 'pythonsdk'
    print('Uploading Video...')
    storage.upload(account, container_name, path, path)


def handle_reboot():
    subprocess.run(['sudo', 'reboot'])


def handle_shutdown():
    subprocess.run(['sudo', 'shutdown'])


def handle_send_ip():
    print('Sending ip address')
    ip_mailer.send_ip()


def handle_unknown(message):
    print('Unknown message received: ' + message)
