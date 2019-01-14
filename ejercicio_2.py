"""
- Definir una función que calcule la longitud de una lista o una 
cadena dada. (Es cierto que python tiene la función len() 
incorporada, pero escribirla por nosotros mismos resulta un muy 
buen ejercicio.

PD:Puedes usar la funcion input para mejorar tu programa, 
También se sugiere usar el uso del método en cadenas strip()

"""
def longitud_lista(lista):
    elementos = 0

    for numero_par in lista:
        elementos = elementos + 1

    return elementos


numeros_pares = [2,4,6,8,10,12,14]
longitud = longitud_lista(numeros_pares)

print (f"La lista tiene {longitud} elementos")

