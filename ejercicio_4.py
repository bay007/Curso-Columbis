"""
Escribir una función con nombre cadena_mas_amplia() 
que tome como parametro una lista de palabras o una frase
y devuelva la mas amplia. 


PD: El Método de cadena split() podrá ayudar.
"""

def cadena_mas_amplia():
    lista = input("Escriba una lista de palabras (separado por una "","") o una frase: ")
    if not isinstance(lista, str) or not isinstance(lista, list):
        print("Favor de escribir str o list")
    elif isinstance(lista, list):
        lista = list.split(",")
        print(lista)


cadena_mas_amplia()