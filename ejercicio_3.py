"""
Escribir una función que tome un carácter y devuelva True si es una vocal,
de lo contrario devuelve False


PD: Es importante consultar una tabla ASCII, 
seguramente la función ord() y char() serán de ayuda.
"""
print("Ingrese un caracter...")
letra = input()

def vocales (letra_ingresada):

    valor_ascii = ord(letra_ingresada)

    #valor de vocales
    lista_vocales = [65,69,73,79,85,97,101,105,111,117]

    if valor_ascii in lista_vocales:
        return "true"
    else:
        return "false"

print(vocales(letra))


