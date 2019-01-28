"""
Declaremos una funcion llamada promedio que tome
como parametros una cantidad indefinida de numeros
promedio(1,2,3,8,5,4,1,4,7,8)
y nos regrese el promedio
"""

'''numeros = [1, 2, 3]

def promedio(*args):
    #input("Escribe la lista de numeros separados por un espacio y se obtendrá el promedio")
    #lista = args.split()
    #return sum([ int(_) for _ in args.split(",")]) / len(args.split(","))
    lista = args.split(",")
    return sum([ int(_) for _ in lista]) / len(lista)

promedio(1,2,3)'''

def promedio(*args):
    #z = 1
    suma = 0
    print(args.item(1))
    '''for _ in args:
        suma += args
    print(suma)'''

promedio(4, 5, 6)
