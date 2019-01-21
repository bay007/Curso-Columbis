"""
Escribir una función con nombre cadena_mas_amplia() 
que tome como parametro una lista de palabras o una frase
y devuelva la mas amplia. 


PD: El Método de cadena split() podrá ayudar.
"""

def cadena_mas_amplia(parrafo):
    cont = 1
    palabra_max = ""
    palabra_ant = ""
    for palabra in parrafo.split():
        if len(palabra) > len(palabra_ant):
            palabra_max = palabra
        elif len(palabra) < len(palabra_ant):
            palabra_max = palabra_ant
        
        palabra_ant = palabra_max
        cont = cont +1

    return palabra_max

palabra_res = cadena_mas_amplia(input("Capture una frase o un párrafo: "))
print(f"La palabra más amplia del párrafo proporcionado es : {palabra_res}")