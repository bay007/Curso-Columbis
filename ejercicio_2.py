"""
- Definir una función que calcule la longitud de una lista o una 
cadena dada. (Es cierto que python tiene la función len() 
incorporada, pero escribirla por nosotros mismos resulta un muy 
buen ejercicio.

PD:Puedes usar la funcion input para mejorar tu programa, 
También se sugiere usar el uso del método en cadenas strip()

"""

numeros_pares = [2,4,6,8,10,12,14]
elementos = 0

for numero_par in numeros_pares:
    elementos = elementos + 1

print (f"La lista tiene {elementos} números")

