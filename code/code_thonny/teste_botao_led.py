# import machine
# import utime

# led_onboard = machine.Pin(25, machine.Pin.OUT)
# button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

# while True:
#     if button.value() == 1:
#         led_onboard.value(1) # Liga o LED onboard
#     else:
#         led_onboard.value(0) # Desliga o LED onboard
#     utime.sleep(0.1) # Pequena pausa para evitar leituras incorretas do botão

## Led liga se apertar 3 simultaneos

import machine
import utime

led_onboard = machine.Pin(25, machine.Pin.OUT)
button_1 = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_2 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_3 = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if button_1.value() and button_2.value() == 1:
        led_onboard.value(1) # Liga o LED onboard
    else:
        led_onboard.value(0) # Desliga o LED onboard
    utime.sleep(0.1) # Pequena pausa para evitar leituras incorretas do botão