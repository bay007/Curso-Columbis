"""
- Definir una función que calcule la longitud de una lista o una 
cadena dada. (Es cierto que python tiene la función len() 
incorporada, pero escribirla por nosotros mismos resulta un muy 
buen ejercicio.

PD:Puedes usar la funcion input para mejorar tu programa, 
También se sugiere usar el uso del método en cadenas strip()

"""
def suma_numeros(*numeros):
        suma = 0
        for numero in numeros:
                suma = suma + numero                
        return(suma)

print(suma_numeros(1,4,8,10,25))
#print (f"La lista tiene {elementos} números")