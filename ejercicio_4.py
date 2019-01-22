"""
Escribir una función con nombre cadena_mas_amplia() 
que tome como parametro una lista de palabras o una frase
y devuelva la mas amplia. 


PD: El Método de cadena split() podrá ayudar.
"""

def cadena_mas_amplia(frase):
    palabras = frase.split()

    return (max(palabras,  key=len))

frase = input("Proporcione una frase: ")
palabra_amplia = cadena_mas_amplia(frase)
print(f"La palabra más amplia de la frase es: {palabra_amplia}")