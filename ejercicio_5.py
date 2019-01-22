"""
Declaremos una funcion llamada promedio que tome
como parametros una cantidad indefinida de numeros
promedio(1,2,3,8,5,4,1,4,7,8)
y nos regrese el promedio
"""

lista_numeros = [1,2,3,8,5,4,1,4,7,8]

def promedio(lista):
    no_elementos = len(lista)
    suma_elementos = sum(lista)
    promedio_tot = (suma_elementos/no_elementos)
    return promedio_tot

print(promedio(lista_numeros))
