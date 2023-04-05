from machine import Pin, ADC
from time import sleep
from utime import ticks_ms, ticks_diff

adc = ADC(Pin(26, Pin.IN))

button = Pin(13, Pin.IN, Pin.PULL_DOWN)

rele = Pin(12, Pin.OUT)


def rele_on():
    rele.off()


def rele_off():
    rele.on()


def conversion_factor(value):
    return round((65535/(value) * 100) - 100)


def activate_bomb():
    rele_on()


def deactivate_bomb():
    start_time = ticks_ms()
    actual_time = ticks_ms()
    moisture = (adc.read_u16())
    while ((conversion_factor(moisture) >= 45) and (ticks_diff(actual_time, start_time) < 6000)):
        moisture = (adc.read_u16())
        actual_time = ticks_ms()

    rele_off()


rele_on()

while True:
    if button.value():
        activate_bomb()
        deactivate_bomb()

    sleep(0.1)
