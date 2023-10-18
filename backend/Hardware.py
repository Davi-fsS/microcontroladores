from machine import Pin, ADC
from time import sleep
from utime import ticks_ms, ticks_diff


class Hardware():

    def __init__(self, rele1, rele2, adc1, adc2):
        self.rele1 = Pin(rele1, Pin.OUT)
        self.rele2 = Pin(rele2, Pin.OUT)

        self.adc1 = ADC(Pin(adc1, Pin.IN))
        self.adc2 = ADC(Pin(adc2, Pin.IN))

        self.rele_off_general()

    def rele_on(self, rele):
        rele.off()

    def rele_off(self, rele):
        rele.on()

    def rele_off_general(self):
        self.rele_off(self.rele1)
        self.rele_off(self.rele2)

    def conversion_factor(self, value):
        return round((65535/(value) * 100) - 100)

    def activate_bomb(self, rele):
        self.rele_on(rele)

    def deactivate_bomb(self, rele_number, adc):
        start_time = ticks_ms()
        actual_time = ticks_ms()
        moisture = adc.read_u16()

        while ((self.conversion_factor(moisture) >= 45) and (ticks_diff(actual_time, start_time) < 5000)):
            moisture = (adc.read_u16())
            actual_time = ticks_ms()

        self.rele_off(rele_number)

        if ticks_diff(actual_time, start_time) < 5000:
            return False

        return True

    def make_drink(self):
        self.activate_bomb(self.rele1)
        self.deactivate_bomb(self.rele1, self.adc1)
        if self.deactivate_bomb(self.rele1, self.adc1) == True:
            sleep(0.5)
            self.activate_bomb(self.rele2)
            self.deactivate_bomb(self.rele2, self.adc2)
