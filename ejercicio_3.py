"""
Escribir una función que tome un carácter y devuelva True si es una vocal,
de lo contrario devuelve False


PD: Es importante consultar una tabla ASCII, 
seguramente la función ord() y char() serán de ayuda.
"""

vocales = ["A", "E", "I", "O", "U"]

def func_vocal():
    letra = input("Escriba un carácer: ")
    letra = letra.upper()
    if letra in vocales:
        print(True)
    else:
        print(False)

func_vocal()