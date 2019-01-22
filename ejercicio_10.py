"""
Escribe un generador de contraseñas en Python. Sea creativo con la forma en que genera las contraseñas:
las contraseñas seguras tienen una combinación de letras minúsculas, mayúsculas, números y símbolos, además por lo menos 
una longitud de 8 caracteres.
"""
#import os 
#os_urandom(65) #criptografica

def genera_contrasenia():
    import random
    import string

    lista_caracteres = "@"
    caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    arma_password =random.sample(caracteres,8)
    password = ''.join(map(str,arma_password)) 
    return password





print(genera_contrasenia())