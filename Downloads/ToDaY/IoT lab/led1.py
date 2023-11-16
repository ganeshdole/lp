import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

while True:
    GPIO.output(3,True)
    print("LED ON..")
    time.sleep(0.5)

    GPIO.output(3,False)
    print("LED OFF..")
    time.sleep(0.5)

    GPIO.output(13,True)
    print("LED ON..")
    time.sleep(0.5)

    GPIO.output(13,False)
    time.sleep(0.5)

GPIO.cleanup()   


or 



import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
while True:
    GPIO.output(5,True)
    time.sleep(2)
    GPIO.output(5,False)
    time.sleep(2)
    GPIO.output(3,True)
    time.sleep(2)
    GPIO.output(3,False)
    time.sleep(2)
    GPIO.cleanup()
