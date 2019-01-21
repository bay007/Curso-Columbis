"""
Declaremos una funcion llamada promedio que tome
como parametros una cantidad indefinida de numeros
promedio(1,2,3,8,5,4,1,4,7,8)
y nos regrese el promedio
"""
def promedio(args):
    lista = args.split()
    cont = 0
    suma = 0
    for valor in lista:
        suma = suma + int(valor)
        cont = cont + 1
    prom = suma/cont    
    return(prom)

print(promedio(input("Proporcione los numeros enlistados por espacio: ")))