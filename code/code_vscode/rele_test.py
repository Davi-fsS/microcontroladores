from machine import Pin
from time import sleep

button = Pin(13, Pin.IN, Pin.PULL_DOWN)

rele = Pin(12, Pin.OUT)


def activate_bomb():
    rele.off()
    sleep(3)
    rele.on()


while True:
    print(button.value())
    if button.value():
        activate_bomb()

    sleep(0.1)
