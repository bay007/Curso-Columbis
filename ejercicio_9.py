"""
Escribe un programa que permita al usuario ingresar una cadena. A la salida se debe imprimir en pantalla un diccionario 
que refleje la frecuencia de ocurrencia de cada letra que aparezca en la frase. Se deben si es mayuscula o minpuscula no
debe importar, el conteo debe hacerse.
"""

import string

#string.ascii_lowercase
letras_minus = string.ascii_lowercase + " "
alfabeto_minus = { x:0 for x in letras_minus }
#print(alfabeto_minus)

#string.ascii_uppercase
letras_mayus  = string.ascii_uppercase + " " 
alfabeto_mayus = { x:0 for x in letras_mayus}
#print(alfabeto_mayus)

def cuenta_caracteres(frase):  
    print(frase)    
    valor_min = 0
    valor_may = 0
    for letra_min in frase:
        if letra_min in alfabeto_minus: 
                valor_min = alfabeto_minus.get(letra_min)
                valor_min = valor_min + 1
                alfabeto_minus[letra_min] = valor_min
    for letra_may in frase:            
        if letra_may in alfabeto_mayus: 
                valor_may = alfabeto_mayus.get(letra_may)
                valor_may = valor_may + 1
                alfabeto_mayus[letra_may] = valor_may
 
    return 



    
palabra_frase = input("Escribe una palabra o frase:")
cuenta_caracteres(palabra_frase)

print(f"Minusculas:{alfabeto_minus}")
print(f"Mayusculas:{alfabeto_mayus}")



#print(letras)
#letters= dict(alphabet)
#print(letters)
