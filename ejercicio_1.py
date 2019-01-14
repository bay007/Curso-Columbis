"""
Escribe un programa que pida dos palabras y diga si riman o no.
Si coinciden las tres últimas letras tiene que decir que riman.
Si coinciden sólo las dos últimas tiene que decir que riman un
poco y si no, que no riman.

PD: investiga el uso de la función input(), con ella podrás mejorar 
tu programa

"""
"""hola_commit1"""

primera_palabra = input("Escriba la primera palabra a comparar: ")
segunda_palabra = input("Escriba la segunda palabra a comparar: ")

slicing_primera = primera_palabra[-3:]
slicing_segunda = segunda_palabra[-3:]

#print(slicing_primera)
#print(slicing_segunda)

if slicing_primera == slicing_segunda:
    print("Riman")
else:
    print("No riman")