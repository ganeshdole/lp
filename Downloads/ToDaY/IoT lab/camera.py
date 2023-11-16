from picamera import PiCamera
from time import sleep

camera=PiCamera()
camera.rotation=180

camera.start_preview()

for i in range(2):
    sleep(5)
    camera.capture('/home/pi/Desktop/img%s.jpg' %i)
    
camera.stop_preview()