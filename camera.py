# Operating the Raspberry Pi Camera.
# Working from example here: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera
from picamera import PiCamera
from time import sleep

camera = PiCamera()

# Record for given duration:
camera.start_preview()
sleep(3)
camera.stop_preview()

# Rotation of the camera
camera.start_preview()
camera.rotation = 180
sleep(3)
camera.stop_preview()

# Transparency
camera.start_preview(alpha=200)
sleep(3)
camera.stop_preview()

# Take a still picture.
camera.start_preview()
camera.stop_preview()
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()

