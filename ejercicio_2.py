"""
- Definir una función que calcule la longitud de una lista o una 
cadena dada. (Es cierto que python tiene la función len() 
incorporada, pero escribirla por nosotros mismos resulta un muy 
buen ejercicio.

PD:Puedes usar la funcion input para mejorar tu programa, 
También se sugiere usar el uso del método en cadenas stip()

"""

def contador_palabras():
  listas = input("Escriba un texto:")
  total = 0
  for lista in listas:
      total = total + 1
  print(total)

contador_palabras()
