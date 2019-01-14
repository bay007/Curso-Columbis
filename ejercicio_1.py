"""
Escribe un programa que pida dos palabras y diga si riman o no.
Si coinciden las tres últimas letras tiene que decir que riman.
Si coinciden sólo las dos últimas tiene que decir que riman un
poco y si no, que {no riman.

PD: investiga el uso de la función input(), con ella podrás mejorar 
tu programa

""" 
numero = 0
palabras_uno = [] 
palabras_dos = [] 


parte = []

for solicita_palabras in range(2):
    numero = numero +1
    if numero == 1:
        palabra = input(f"Dame palabra {numero}:") 
        palabras_uno.append(palabra)
    else:
        palabra = input(f"Dame palabra {numero}:") 
        palabras_dos.append(palabra)
 

for elemento_uno in palabras_uno: 
    for elemento_dos in palabras_dos: 
        if elemento_uno in elemento_dos:
            print("Son palabras iguales")
        elif elemento_uno[-3:] == elemento_dos[-3:]: 
            print("Riman")
        elif elemento_uno[-2:] == elemento_dos[-2:]:
            print("Casi riman")
        else:
            print("No riman") 
