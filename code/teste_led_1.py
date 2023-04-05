import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)

while True:
    led_onboard.value(1) # Liga o LED
    utime.sleep(1) # Espera 1 segundo
    led_onboard.value(0) # Desliga o LED
    utime.sleep(1) # Espera 1 segundo