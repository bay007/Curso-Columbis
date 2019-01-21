"""
Escribir una función que tome un carácter y devuelva True si es una vocal,
de lo contrario devuelve False


PD: Es importante consultar una tabla ASCII, 
seguramente la función ord() y char() serán de ayuda.
"""


def es_vocal(letra):
    lista = {"a","A","e","E","i","I","o","O","u","U"}
    if letra in lista:
        valor = "True"
    else:
        valor = "False"
    return valor
    
resultado = es_vocal(input("Capture la letra: "))
print(resultado)