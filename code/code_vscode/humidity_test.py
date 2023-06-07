from machine import Pin, ADC

adc = ADC(Pin(26, Pin.IN))

pin = Pin("LED", Pin.OUT)


def conversion_factor(value):
    return round((65535/(value) * 100) - 100)


while True:
    moisture = (adc.read_u16())
    print(f"Moisture: {conversion_factor(moisture)}")

    if conversion_factor(moisture) >= 45:
        pin.on()
    else:
        pin.off()
