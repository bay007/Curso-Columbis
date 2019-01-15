"""
Se desea modelar para un casino un juego con dado, por lo qu ehay que programar un lanzador de dado.
Así  hay que generar una función que al ser ejecutada devuelva un numero aleatorio del 1 al 6.

PD: Para éste ejemplo  hay que hacer uso del módulo random
https://docs.python.org/3.7/library/random.html

"""

from random import *

def dado():
    numero_dado = randint(1,6)
    #print(numero_dado)
    return numero_dado

print(dado())