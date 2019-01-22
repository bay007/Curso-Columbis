"""
Se desea modelar para un casino un juego con dado, por lo qu ehay que programar un lanzador de dado.
Así  hay que generar una función que al ser ejecutada devuelva un numero aleatorio del 1 al 6.

PD: Para éste ejemplo  hay que hacer uso del módulo random
https://docs.python.org/3.7/library/random.html

"""
import random

def tira_dado():
    dado = random.randint(1,6)
    return dado


resultado = tira_dado()
print(resultado) 