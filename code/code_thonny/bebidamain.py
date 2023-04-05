import machine
import time

# Configurando os pinos GPIO que as bombas estão conectadas
pump1_pin = machine.Pin(25, machine.Pin.OUT)
pump2_pin = machine.Pin(26, machine.Pin.OUT)
pump3_pin = machine.Pin(27, machine.Pin.OUT)

# Configurando os pinos GPIO que os botões estão conectados
button1_pin = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
button2_pin = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)
button3_pin = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    # Aguardando o botão 1 ser pressionado
    while button1_pin.value() == 0:
        pass
    
    # Bombando o líquido 1
    pump1_pin.value(1)
    time.sleep(3)
    pump1_pin.value(0)

    # Bombando o líquido 2
    pump2_pin.value(1)
    time.sleep(3)
    pump2_pin.value(0)

    # Aguardando o botão 2 ser pressionado
    while button2_pin.value() == 0:
        pass
    
    # Bombando o líquido 2
    pump2_pin.value(1)
    time.sleep(3)
    pump2_pin.value(0)

    # Bombando o líquido 3
    pump3_pin.value(1)
    time.sleep(3)
    pump3_pin.value(0)

    # Aguardando o botão 3 ser pressionado
    while button3_pin.value() == 0:
        pass
    
    # Bombando o líquido 1
    pump1_pin.value(1)
    time.sleep(3)
    pump1_pin.value(0)

    # Bombando o líquido 3
    pump3_pin.value(1)
    time.sleep(3)
    pump3_pin.value(0)