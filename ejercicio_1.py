"""
Escribe un programa que pida dos palabras y diga si riman o no.
Si coinciden las tres últimas letras tiene que decir que riman.
Si coinciden sólo las dos últimas tiene que decir que riman un
poco y si no, que no riman.

PD: investiga el uso de la función input(), con ella podrás mejorar 
tu programa

"""

def riman(palabra1, palabra2):
    if palabra1[-3::].upper() in palabra2[-3::].upper():
        return "Las palabras si riman"
    elif palabra1[-2::].upper() in palabra2[-2::].upper():
        return "Las palabras casi riman"
    else:
        return "Las palabras no riman"

palabra_1 = input("Proporcione la primer palabra: ")
palabra_2 = input("Proporcione la segunda palabra: ")

print (riman(palabra_1, palabra_2))
