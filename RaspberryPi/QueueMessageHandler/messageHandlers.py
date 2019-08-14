import camera
import AZ.storage as storage
import AZ.base as base
import subprocess
import ip_mailer
import videoConverter

account = base.get_account()
container_name = 'pythonsdk'


def handle_video_capture():
    print('Capturing Video...')
    path = 'vid.h264'
    mp4_path = 'vid.mp4'
    camera.capture_video(path, 5)
    print('Converting Video')
    videoConverter.convert(path, mp4_path)
    print('Uploading Video...')
    storage.upload(account, container_name, mp4_path, mp4_path)

def handle_image_capture():
    path = 'img.jpg'
    print('Capturing Image')
    camera.capture_image(path)
    print('Uploading Image...')
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
