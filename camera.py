# Operating the Raspberry Pi Camera.
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(15)
camera.stop_preview()
