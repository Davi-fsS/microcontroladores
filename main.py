from machine import Pin, ADC
from time import sleep
from utime import ticks_ms, ticks_diff

adc = ADC(Pin(26, Pin.IN))
adc2 = ADC(Pin(27, Pin.IN))

button = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(15, Pin.IN, Pin.PULL_DOWN)

rele = Pin(12, Pin.OUT)
rele2 = Pin(11, Pin.OUT)


def rele_on():
    rele.off()


def rele_off():
    rele.on()


def rele2_on():
    rele2.off()


def rele2_off():
    rele2.on()


def conversion_factor(value):
    return round((65535/(value) * 100) - 100)


def activate_bomb():
    rele_on()


def activate_bomb2():
    rele2_on()


def deactivate_bomb():
    start_time = ticks_ms()
    actual_time = ticks_ms()
    moisture = (adc.read_u16())
    while ((conversion_factor(moisture) >= 45) and (ticks_diff(actual_time, start_time) < 6000)):
        moisture = (adc.read_u16())
        actual_time = ticks_ms()

    rele_off()


def deactivate_bomb2():
    start_time = ticks_ms()
    actual_time = ticks_ms()
    moisture = (adc2.read_u16())
    while ((conversion_factor(moisture) >= 45) and (ticks_diff(actual_time, start_time) < 6000)):
        moisture = (adc2.read_u16())
        actual_time = ticks_ms()

    rele2_off()

# def deactivate_bomb_general(adc_option, rele_option):
#     start_time = ticks_ms()
#     actual_time = ticks_ms()
#     moisture = (adc_option.read_u16())
#     while ((conversion_factor(moisture) >= 45) and (ticks_diff(actual_time, start_time) < 6000)):
#         moisture = (adc_option.read_u16())
#         actual_time = ticks_ms()

#     rele_option()


# Always starts off
rele_off()
rele2_off()

while True:
    if button.value():
        activate_bomb()
        deactivate_bomb()
        sleep(1)
        activate_bomb2()
        deactivate_bomb2()

    if button2.value():
        activate_bomb2()
        deactivate_bomb2()
        sleep(1)
        activate_bomb()
        deactivate_bomb()

    sleep(0.1)
