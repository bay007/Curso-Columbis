"""
Escribir una función con nombre cadena_mas_amplia() 
que tome como parametro una lista de palabras o una frase
y devuelva la mas amplia. 


PD: El Método de cadena split() podrá ayudar.
"""


def cadena_mas_amplia(frase_palabra):
    lista_palabras = frase_palabra.split()
    lista_palabras_tam = {}
    for palabra in lista_palabras:
        tamanio = len(palabra)
        lista_palabras_tam.update({tamanio:palabra})
    
    mayor_tamanio = max(lista_palabras_tam.keys())  
    palabra_grande = lista_palabras_tam.get(mayor_tamanio) 
    return palabra_grande


resultado = cadena_mas_amplia(input("Dame una frase: ")) 


print(f"La cadena mas grande es: {resultado}" )
