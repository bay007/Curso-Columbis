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


for dato in range(3):
    datos = {'nombre': fake.name(), 
        'dirección_postal': fake.address() ,
        'direccion_fiscal': fake.address()
        }

json1 = json.dumps(datos)

print ("[" +json1 +"]")



