from colorama import Fore
import random
import os

def generarPalabra():
  palabras = ['murcelielago','huerfano','programacion','software','hardware']
  return random.choice(palabras)

def imprimirVidas(vidas:int):
  print(Fore.WHITE,'Vidas:',Fore.RED,end='')
  for i in range(vidas):
    print('❤',end=' ')
  print()

def imprimirPalabra(palabra:str, letras:list):
  linea = ''
  for letra in palabra:
    if letra in letras:
      linea += f'{letra} '
    else:
      linea += '_ '
  print(f'Palabra: {linea}')
def colorAletorio():
  colores = [Fore.BLUE, Fore.YELLOW, Fore.MAGENTA, Fore.CYAN, Fore.GREEN, Fore.WHITE]
  return random.choice(colores)

def dibujarAhorcado(vidas:int):
  print(colorAletorio())
  if vidas == 5:
    print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
    print('█  ▄▀        █')
    print('█▄▀        ▄▀▀▀▄')
    print('█          ▀▄▄▄▀')
    print('█        ▬▬▬▬█▬▬▬▬')
    print('█            █')
    print('█          ▄▀ ▀▄')
    print('█')
    print('█')
  elif vidas == 4:
    print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
    print('█  ▄▀        █')
    print('█▄▀        ▄▀▀▀▄')
    print('█          ▀▄▄▄▀')
    print('█        ▬▬▬▬█▬▬▬▬')
    print('█            █')
    print('█             ▀▄')
    print('█')
    print('█')
  elif vidas == 3:
    print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
    print('█  ▄▀        █')
    print('█▄▀        ▄▀▀▀▄')
    print('█          ▀▄▄▄▀')
    print('█        ▬▬▬▬█▬▬▬▬')
    print('█            █')
    print('█             ')
    print('█')
    print('█')
  elif vidas == 2:
    print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
    print('█  ▄▀        █')
    print('█▄▀        ▄▀▀▀▄')
    print('█          ▀▄▄▄▀')
    print('█            █▬▬▬▬')
    print('█            █')
    print('█             ')
    print('█')
    print('█')
  elif vidas == 1:
    print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
    print('█  ▄▀        █')
    print('█▄▀        ▄▀▀▀▄')
    print('█          ▀▄▄▄▀')
    print('█            █')
    print('█            █')
    print('█')
    print('█')
    print('█')
  elif vidas == 0:
    print(Fore.RED)
    print('▄▄▄▄▄▄▄▄▄▄▄▄▄▄')
    print('█  ▄▀        █')
    print('█▄▀        ▀▄ ▄▀')
    print('█           ▄▀▄')
    print('█          ▀   ▀')
    print('█')
    print('█')
    print('█')
    print('█')

def palabraAdivinada(palabra:str, letrasIngresadas:list):
  for letra in palabra:
    if letra not in letrasIngresadas:
      return False
  return True
  
def letraAdivinada(palabra:str,letras:list,letra:str):

  if letra not in letras and letra in palabra and len(letra) == 1:
    return True

  return False

def jugar():
  palabra = generarPalabra()
  letras = []
  vidas = 5
  while palabraAdivinada(palabra, letras) == False and vidas > 0:
    os.system('cls')
    imprimirVidas(vidas)
    dibujarAhorcado(vidas)
    imprimirPalabra(palabra,letras)
    print(Fore.WHITE)

    letra = input('Adivine una letra: ').lower()
    if letraAdivinada(palabra,letras,letra) == False:
      vidas -= 1

    if letra not in letras and len(letra) == 1:
      letras.append(letra)

  if palabraAdivinada(palabra, letras):
    print(Fore.GREEN)
    print('✔ Felicidades ganó!')
  else:
    os.system('cls')
    imprimirVidas(vidas)
    dibujarAhorcado(vidas)
    imprimirPalabra(palabra, letras)
    print('❌ Vuelva a intentarlo perdio!')
  
opcion = 1
while opcion != 2:
  print(Fore.WHITE)
  print('=== JUEGO AHORCADO ===')
  print('[1] Jugar')
  print('[2] Salir')
  opcion = int(input('Opcion: '))

  if opcion == 1:
    jugar()
  else:
    print('✌ Adios!')