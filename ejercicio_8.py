"""
Se desea modelar para un casino un juego con dado, por lo qu ehay que programar un lanzador de dado.
Así  hay que generar una función que al ser ejecutada devuelva un numero aleatorio del 1 al 6.

PD: Para éste ejemplo  hay que hacer uso del módulo random
https://docs.python.org/3.7/library/random.html

"""
from random import choice

def dado():
    numeros = [1,2,3,4,5,6]
    valor= choice(numeros)
    
    return valor

print(dado())

#List Compre
"""
k=[numero for numero in range(8) if numero>3]
print(k)
"""


