from machine import Pin, ADC


class Humidity():

    def read_humidity(self, adc):
        moisture = ADC(Pin(adc, Pin.IN)).read_u16()
        return self.conversion_factor(moisture)

    def conversion_factor(self, value):
        return round((65535/(value) * 100) - 100)
