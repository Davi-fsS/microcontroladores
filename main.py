from machine import Pin, ADC
from time import sleep
from utime import ticks_ms, ticks_diff

adc = ADC(Pin(26, Pin.IN))
adc2 = ADC(Pin(27, Pin.IN))
adc3 = ADC(Pin(28, Pin.IN))

button = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(15, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(14, Pin.IN, Pin.PULL_DOWN)

rele = Pin(12, Pin.OUT)
rele2 = Pin(11, Pin.OUT)
rele3 = Pin(10, Pin.OUT)


def rele_on(pino):
    Pin(pino, Pin.OUT).off()


def rele_off():
    rele.on()


def rele2_on():
    rele2.off()


def rele2_off():
    rele2.on()


def rele3_on():
    rele3.off()


def rele3_off():
    rele3.on()


def conversion_factor(value):
    return round((65535/(value) * 100) - 100)


def activate_bomb(pino):
    rele_on(pino)


def activate_bomb2():
    rele2_on()


def activate_bomb3():
    rele3_on()


def read_humidity(pino):
    moisture = ADC(Pin(pino, Pin.IN)).read_u16()
    # aumentar para prever que falte bebida
    return conversion_factor(moisture) > 62


def read_humidity2():
    moisture2 = adc2.read_u16()
    return conversion_factor(moisture2) > 62


def read_humidity3():
    moisture3 = adc3.read_u16()
    return conversion_factor(moisture3) > 62


def deactivate_bomb():
    start_time = ticks_ms()
    actual_time = ticks_ms()
    moisture = (adc.read_u16())

    while ((conversion_factor(moisture) >= 45) and (ticks_diff(actual_time, start_time) < 5000)):
        moisture = (adc.read_u16())
        actual_time = ticks_ms()

    rele_off()

    if ticks_diff(actual_time, start_time) < 5000:
        return False

    return True


def deactivate_bomb2():
    start_time = ticks_ms()
    actual_time = ticks_ms()
    moisture = (adc2.read_u16())
    while ((conversion_factor(moisture) >= 45) and (ticks_diff(actual_time, start_time) < 5000)):
        moisture = (adc2.read_u16())
        actual_time = ticks_ms()

    rele2_off()

    if ticks_diff(actual_time, start_time) < 5000:
        return False

    return True


def deactivate_bomb3(pino, doses):
    start_time = ticks_ms()
    actual_time = ticks_ms()
    moisture = ADC(Pin(pino, Pin.IN)).read_u16()
    while ((conversion_factor(moisture) >= 45) and (ticks_diff(actual_time, start_time) < 3000 * doses)):
        moisture = (adc3.read_u16())
        actual_time = ticks_ms()

    rele3_off()

    if ticks_diff(actual_time, start_time) < 5000:
        return False

    return True


# COMEÇAR INATIVO SEMPRE
rele_off()
rele2_off()
rele3_off()

while True:

    #     print(conversion_factor(adc.read_u16()))

    if (conversion_factor(adc3.read_u16())) < 62:
        print('sem liquido na bomba 3')
    if (conversion_factor(adc2.read_u16())) < 62:
        print('sem liquido na bomba 2')
    if (conversion_factor(adc.read_u16())) < 62:
        print('sem liquido na bomba 1')

    # Combinação Bebida 1 e 2
    pino = 12

    if button.value():
        if read_humidity2():
            activate_bomb(pino)
            deactivate_bomb()
            if deactivate_bomb() == True:
                sleep(0.5)
                activate_bomb2()
                deactivate_bomb2()

    # Combinação Bebida 2 e 3
    if button2.value():
        if read_humidity3():
            activate_bomb2()
            deactivate_bomb2()
            if deactivate_bomb2() == True:
                sleep(0.5)
                activate_bomb3()
                deactivate_bomb3()

    # Combinação Bebida 3 e 1
    if button3.value():
        if read_humidity():
            activate_bomb3()
            deactivate_bomb3()
            if deactivate_bomb3() == True:
                sleep(0.5)
                activate_bomb()
                deactivate_bomb()

    sleep(0.1)
