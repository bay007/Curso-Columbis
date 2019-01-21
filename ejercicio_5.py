"""
Declaremos una funcion llamada promedio que tome
como parametros una cantidad indefinida de numeros
promedio(1,2,3,8,5,4,1,4,7,8)
y nos regrese el promedio
"""

"""
def promedio(*args): 
    print(args)
    resultado = sum(args)/len(args)
    return resultado
"""
def promedio(*args):
    print (args)
    for numero in args:
        print (numero) 
    #resultado = sum(args)/len(args)
    #return resultado

resultado = promedio(3,5,6,7,12)
print(f"El promedio es: {resultado}")



entrada_numero = input("Dame numeros separados por comas: ") 
#lista_numeros = entrada_numero.split(",")
#print(lista_numeros)

resultado = promedio(entrada_numero)
print(f"El promedio es: {resultado}")


"""
numeros = entrada_numero
continua = 'S' 


if len(numeros) <= 1 :
    entrada_numero = print("Escribe un numero: ")
    numeros = entrada_numero

while continua == 'S':
    respuesta_mas_numeros = input("¿Deseas agregar mas numeros S/N?")
    if respuesta_mas_numeros == 'S':
        entrada_numero = input("Escribe un otro numero: ")
        numeros = entrada_numero
    elif respuesta_mas_numeros != 'S' and  respuesta_mas_numeros != 'N':
        print("Valor no valido")
        continue
    elif respuesta_mas_numeros == 'N':
        break
    


    resultado = promedio(entrada_numeros)
    print(f"El resultado es {resultado}")
"""