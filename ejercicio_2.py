"""
- Definir una función que calcule la longitud de una lista o una 
cadena dada. (Es cierto que python tiene la función len() 
incorporada, pero escribirla por nosotros mismos resulta un muy 
buen ejercicio.

PD:Puedes usar la funcion input para mejorar tu programa, 
También se sugiere usar el uso del método en cadenas strip()

"""
cont = 0
tipo = input("Desea una Cadena(C) o una Lista (L)")
tipo = str.upper(tipo)
if tipo == 'C' or tipo == 'L':    
    if tipo == 'C':
        datos = input("Introduzca los datos: ")
        cadena = datos.strip()
        for x in cadena:
            cont = cont + 1
        print(f"La longitud de la Cadena: '{cadena}' es: {str(cont)}")
    else:
        datos = input("Introduzca la lista (los elemenos separados por espacio): ")
        lista = datos.split()
        for x in lista:
            cont = cont + 1
        print(f"La longitud de la Lista es: '{lista}' es: {str(cont)}")
else:
    print("No capturó un valor válido.")