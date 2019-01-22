"""
Escribir una función que tome un carácter y devuelva True si es una vocal,
de lo contrario devuelve False


PD: Es importante consultar una tabla ASCII, 
seguramente la función ord() y char() serán de ayuda.
"""

def es_vocal(letra):
    unicode = ord(letra.upper())
    if unicode in (65, 69, 73, 79, 85):
        return True
    else:
        return False

letra = input("Proporcione una letra del abecedario: ")
letra_vocal = es_vocal(letra)

if letra_vocal == True:
    print(f"La letra {letra} si es una vocal")
else:
    print(f"La letra {letra} no es una vocal")