import ctypes
import time

mouse_event = ctypes.windll.user32.mouse_event
contador = 0

MOUSE_LEFTDOWN = 0x02
MOUSE_LEFTUP = 0x04

temporizador = int(input("Digite quantos minutos deseja rodar o programa: "))

while temporizador > 0:
    print("\033[H\033[J", end="")
    print("-=-=-=-=- \033[92mSempre Online\033[0m -=-=-=-=-")
    print(f"\033[92m{temporizador}\033[0m minuto(s) restante(s)")
    print(f"\033[92m{contador}\033[0m clique(s) efetuado(s)")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    time.sleep(60)
    mouse_event(MOUSE_LEFTDOWN, 0, 0, 0, 0)
    mouse_event(MOUSE_LEFTUP, 0, 0, 0, 0)
    contador += 1
    temporizador -= 1

print("Programa encerrado, obrigado pela preferência!")
