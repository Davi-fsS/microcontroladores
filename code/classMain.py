from machine import Pin, ADC
from time import sleep
from utime import ticks_ms, ticks_diff


class MainProgram:
    def __init__(self):
        self.adc = ADC(Pin(26, Pin.IN))
        self.button = Pin(13, Pin.IN, Pin.PULL_DOWN)
        self.rele = Pin(12, Pin.OUT)

    def get_adc(self):
        return self.adc

    def get_button(self):
        return self.button

    def get_rele(self):
        return self.rele

    def get_button_value(self):
        return self.button.value()

    def rele_on(self):
        self.rele.off()

    def rele_off(self):
        self.rele.on()

    def conversion_factor(self, value):
        return round((65535/(value) * 100) - 100)

    def activate_bomb(self):
        self.rele_on()

    def deactivate_bomb(self):
        start_time = ticks_ms()
        actual_time = ticks_ms()
        moisture = (self.adc.read_u16())
        while ((self.conversion_factor(moisture) >= 45) and (ticks_diff(actual_time, start_time) < 6000)):
            moisture = (self.adc.read_u16())
            actual_time = ticks_ms()

        self.rele_off()


main = MainProgram()
main.rele_off()
while True:
    if main.get_button_value():
        main.activate_bomb()
        main.deactivate_bomb()
    sleep(0.1)
