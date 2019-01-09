"""
- Definir una función que calcule la longitud de una lista o una 
cadena dada. (Es cierto que python tiene la función len() 
incorporada, pero escribirla por nosotros mismos resulta un muy 
buen ejercicio.

PD:Puedes usar la funcion input para mejorar tu programa, 
También se sugiere usar el uso del método en cadenas stip()

"""
contador = 0
lista = [1,2,3,4,5,8,4,5,7,3,4,5,1]
for elemento in lista:
    contador = contador + 1

print(f"El numero de elementos en tu lista es {contador}")
