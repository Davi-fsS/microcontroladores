
from machine import Pin
from time import sleep

pin = Pin("LED", Pin.OUT)
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(14, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(15, Pin.IN, Pin.PULL_DOWN)

while True:
    print(button1.value() and button2.value())
    if button1.value() and button2.value():
        pin.on()
    else:
        pin.off()
    sleep(0.1)
