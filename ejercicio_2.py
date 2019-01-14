"""
- Definir una función que calcule la longitud de una lista o una 
cadena dada. (Es cierto que python tiene la función len() 
incorporada, pero escribirla por nosotros mismos resulta un muy 
buen ejercicio.

PD:Puedes usar la funcion input para mejorar tu programa, 
También se sugiere usar el uso del método en cadenas strip()

"""
def conteo():
    #definir una variable para guardar la longitud

    materias = ["Español","Matematicas","Historia","Geografia", "Quimica", "Fisica"]

    no_materias = 0

    for materia in materias:
        no_materias = no_materias +1

    return no_materias

print("El número de materias es:", conteo())