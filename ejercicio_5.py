"""
Declaremos una funcion llamada promedio que tome
como parametros una cantidad indefinida de numeros
promedio(1,2,3,8,5,4,1,4,7,8)
y nos regrese el promedio
"""


def promedio(*numeros):
    suma = 0

    for n in numeros:
        suma = suma + n
    
    promedio = suma/len(numeros)
    return promedio

valor = promedio(2,4,6,8)
print(f"El promedio es: {valor}")
