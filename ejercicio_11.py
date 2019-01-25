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
from faker import Faker
import pprint
import json

fake = Faker('es_MX')

#print(fake.name())

#print(fake.address())

def genera_info(num_personas):
    pp = pprint.PrettyPrinter(indent=4)
    directorio = []
    for x in range(num_personas):
        persona = {}
        persona.update({"nombre": fake.name()})
        persona.update({"direccion_fiscal" : fake.address()})
        persona.update({"direccion_postal": fake.address()})
        directorio.append(persona)
        
        return directorio


if __name__ == "__main__":
    personas = int(input("Proporcione el número de personas: "))
    print(genera_info(personas))




