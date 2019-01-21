"""
Escribe un programa que pida dos palabras y diga si riman o no.
Si coinciden las tres últimas letras tiene que decir que riman.
Si coinciden sólo las dos últimas tiene que decir que riman un
poco y si no, que no riman.

PD: investiga el uso de la función input(), con ella podrás mejorar 
tu programa

"""
print("Vamos a jugar un juego, el juego de las rimas")
p1= input("¿Dime la primer palabra? ")
p2= input("¿Dime la segunda palabra? ")

p1_3lt = p1[-3:]
p1_2lt = p1[-2:]
p2_3lt = p2[-3:]
p2_2lt = p2[-2:]

if p1_3lt == p2_3lt:
    print("las palabras SI riman")
elif p1_2lt == p2_2lt:
    print("las palabras CASI riman")
else:
    print("las palabras NO riman ")