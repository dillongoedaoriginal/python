from picamera import PiCamera
from time import sleep
import datetime as dt


def capture_video(path, seconds):
    with PiCamera() as camera:
        #camera.resolution = (1024, 768)
        camera.annotate_text_size = 40  # (values 6 to 160, default is 32)
        camera.annotate_text = dt.datetime.now().strftime('%b %Y %H:%M')
        camera.start_preview()
        camera.start_recording(path)
        sleep(seconds)
        camera.stop_recording()
        camera.stop_preview()


def capture_image(path):
    with PiCamera() as camera:
        camera.annotate_text = dt.datetime.now().strftime('%d %b %Y %H:%M')
        camera.capture(path)


if __name__ == '__main__':
    capture_video('/home/pi/video_door.h264', 5)
