# Blink an LED on and off with alternative blink rates
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)  #LED output
GPIO.setup(24,GPIO.IN)  #Blink rate button

while True:
    status = GPIO.input(24)
    if status:
        GPIO.output(17,True)
        sleep(0.25)
        GPIO.output(17,False)
        sleep(0.25)
    else:
        GPIO.output(17,True)
        sleep(1.0)
