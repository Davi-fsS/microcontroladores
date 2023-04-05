import machine
import time

# Define o pino que o botão está conectado
botao_pin = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Define o pino que o relé está conectado
rele_pin = machine.Pin(14, machine.Pin.OUT)

# Define a função para ligar a bomba por 1 segundo
def acionar_bomba():
    # Liga o relé
    rele_pin.value(1)
    # Espera 1 segundo
    time.sleep(1)
    # Desliga o relé
    rele_pin.value(0)

# Loop principal do programa
while True:
    # Verifica se o botão foi pressionado
    if botao_pin.value() == 1:
        # Aciona a bomba
        acionar_bomba()

