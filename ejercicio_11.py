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
from pprint import pprint
import json

fake = Faker('es_MX')
fake2 = Faker('es_MX')

def pf(numeros_pf = 1):
    personas_json = []
    for contador in range(numeros_pf):
        name = fake.name()
        address = fake.address()
        address2 = fake.address()
        personas = {'nombre': name,
                    'direccion_fisica': address,
                    'direccion_postal': address2}
        personas_json.append(personas)
        #print(personas)
    print(len(personas_json))
    print(json.dumps(personas_json, indent=4))
    return(pf)

pf()

