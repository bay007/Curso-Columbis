"""
Se requiere generar un Json que contenga la información
de personas físicas, para cada persona hay que tener su
dirección física y su dirección postal.

Éste código deberá ser hecho en una función.
que reciba como parametro el numero de personas que 
se van a generar.

PD: Se sugiere hacer uso del paquete Faker.
En su linea de comandos ejecute
pip install Faker
"""
#pprint pprint o import jason  -- jason.dumps()


from faker import Faker
from pprint import pprint 
import json 

def obten_datos_persona(num_datos):
    num = 0
    fake = Faker('') 
    datos = ""
    
    for dato in range(int(num_datos)):
        num = num + 1
        lista_datos = {"id": num,
                        "Nombre": fake.name(),
                        "Direccion_pos":fake.address(),
                        "Direccion_fiscal":fake.address()}
        print(lista_datos)
        datos = datos + str(lista_datos)
    return datos
 

resultado =  obten_datos_persona(input("¿Cuantos datos quieres obtener?"))

print(json.dumps(resultado, indent = 3))
