#Python code for blinking LED in Raspberry Pi
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial = GPIO.LOW)
while True:
     GPIO.output(8, GPIO.HIGH)
     sleep(1)
     GPIO.output(8, GPIO.LOW)
     sleep(1)


#Python code for blinking Traffic Lights in Raspberry Pi
     
from gpiozero import Button, Traffic Lights, Buzzer
from time import sleep

buzzer = Buzzer(15)
button = Button(21)
lights = TrafficLights(25,8,7)

while True:
       button.wat_for_press()
       buzzer.on()
       light.green.on()
       sleep(1)
       lights.amber.on()
       sleep(1)
       lights.red.on()
       sleep(1)
       lights.off()
       buzzer.off()
