"""
Escribe un generador de contraseñas en Python. Sea creativo con la forma en que genera las contraseñas:
las contraseñas seguras tienen una combinación de letras minúsculas, mayúsculas, números y símbolos, además por lo menos 
una longitud de 8 caracteres.
"""
from random import randrange
from random import choice
from random import shuffle

caracteres =["#","$","%","&","?","¡","!","=","a","b","c","d","e","f","g","h","i","j"]

def gen_pass():
    nuevo_pass = ""
    for pwd in range(4):
        caracter = str(randrange(10)) + choice(caracteres)
        nuevo_pass = nuevo_pass+caracter   
    
    return nuevo_pass


print(gen_pass())





