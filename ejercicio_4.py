"""
Escribir una función con nombre cadena_mas_amplia() 
que tome como parametro una lista de palabras o una frase
y devuelva la mas amplia. 


PD: El Método de cadena split() podrá ayudar.
"""
palabra = "La palabra mas amplia"

def cadena_mas_amplia(cadena):
    list_cadena = cadena.split(" ")
    amplia = max(list_cadena)
    return amplia

print("La palabra mas amplia es: " + cadena_mas_amplia(palabra) )






