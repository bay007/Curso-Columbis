"""
Escribe un programa que pida dos palabras y diga si riman o no.
Si coinciden las tres últimas letras tiene que decir que riman.
Si coinciden sólo las dos últimas tiene que decir que riman un
poco y si no, que no riman.

PD: investiga el uso de la función input(), con ella podrás mejorar 
tu programa

"""
print("Ingrese la 1er palabra")
primer_palabra = input()

print("Ingrese la 2a palabra")
segunda_palabra = input()

def riman (palabra1,palabra2):
    if palabra1[-3:] == palabra2[-3:]:
        es_rima = "Riman."
    elif palabra1[-2:] == palabra2[-2:] :
        es_rima = "Riman un poco."
    else:
        es_rima = " No riman"

    return es_rima

rima = riman(primer_palabra,segunda_palabra)

print (f"Las palabras:  {primer_palabra} y {segunda_palabra} {rima}")

