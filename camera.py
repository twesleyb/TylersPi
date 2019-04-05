# Operating the Raspberry Pi Camera.
# Working from example here: https://projects.raspberrypi.org/en/projects/getting-started-with-picamera
# PiCamera documentation is here: https://picamera.readthedocs.io/en/release-1.13/index.html
from picamera import PiCamera
from time import sleep

camera = PiCamera()

# Record for given duration:
camera.start_preview()
sleep(3)
camera.stop_preview()

# Rotation of the camera
camera.rotation = 180
camera.start_preview()
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

# Loop to take n pictures.
n = 1
path = '/home/pi/Documents/GitHub/TylersPi/'
camera.rotation = 45
camera.start_preview()
for i in range(n):
    sleep(5)
    camera.capture(path + 'image%s.jpg' % i)
camera.stop_preview()

# Recording videos.
camera.start_preview()
camera.start_recording(path + 'video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()

# Play the video from the terminal.
$ cd Documents/GitHub/TylersPi
$ omxplayer video.h264

# Note that the playback speed is accelrated.
# This is due to omxplayer’s fast frame rate.

# Changing the resolution.
# Max still res = 2592 x 1944; FR should be 15.
# Max video res = 1920 x 1080
camera.resolution = (2592, 1944)
camera.framerate = 15
camera.start_preview()
sleep(5)
camera.capture(path + 'max.jpg')
camera.stop_preview()

# Min resolution is 64 x 64.
camera.resolution = (64,64)
camera.start_preview()
sleep(5)
camera.capture(path + 'min.jpg')
camera.stop_preview()

# Annotate with text.
# Text size range from 6 to 160. The default is 32.
# Change brightness [0,100; default = 50]
camera.start_preview()
camera.resolution = (2592,1944)
camera.framerate = 15
camera.brightness = 50
camera.annotate_text_size = 160
camera.annotate_text = "Potato!"
sleep(5)
camera.capture(path + 'text.jpg')
camera.stop_preview()

# Adding color to text annotation.
from picamera import PiCamera, Color
camera.framerate =
camera.start_preview()
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text = " Hello world "
sleep(5)
camera.stop_preview()

# Other settings.
camera.METER_MODES
camera.EXPOSURE_MODES
camera.FLASH_MODES
camera.AWB_MODES
camera.IMAGE_EFFECTS
camera.DRC_STRENGTHS
camera.STEREO_MODES
camera.CLOCK_MODES
