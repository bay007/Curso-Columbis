"""
- Definir una función que calcule la longitud de una lista o una 
cadena dada. (Es cierto que python tiene la función len() 
incorporada, pero escribirla por nosotros mismos resulta un muy 
buen ejercicio.

PD:Puedes usar la funcion input para mejorar tu programa, 
También se sugiere usar el uso del método en cadenas strip()

"""
lista_paises = ["Corea del sur","Londres","Japón","Italia","Grecia"]

print(f"Los paises son: {lista_paises}")
conteo = 0
for lista_pais in lista_paises:
    conteo = conteo + 1

print(f"Tienes  {conteo}  elementos" )