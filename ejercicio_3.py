"""
Escribir una función que tome un carácter y devuelva True si es una vocal,
de lo contrario devuelve False


PD: Es importante consultar una tabla ASCII, 
seguramente la función ord() y char() serán de ayuda.
"""


def esvocal(vocal):
    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    if vocal in vocales:
        mensaje = "Es una vocal"
    else:
        mensaje = "No es una vocal"
    return mensaje

 

resultado = esvocal(input("Dame un caracter: "))

print(resultado)

