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

Ejemplos:
print(fake.address())
print(fake.text())

for x in range(10):
  print(fake.name())

  def genera_info(num_personas):
    for x in range(num_personas):
        directorio.update({"nombre_" + str(x+1): fake.name()})
        directorio.update({"direccion_fisica_" + str(x+1): fake.address()})
        directorio.update({"direccion_postal_" + str(x+1): fake.address()})
"""
from faker import Faker
import pprint

pp = pprint.PrettyPrinter(indent=4)

fake = Faker('es_MX')
directorio = []

def genera_info(num_personas):
    for x in range(num_personas):
        persona = {}
        persona.update({"nombre": fake.name()})
        persona.update({"direccion_fisica" : fake.address()})
        persona.update({"direccion_postal": fake.address()})
        directorio.append(persona)

personas = int(input("Proporcione el número de personas: "))
genera_info(personas)
print(f"La información generada es : ")
pp.pprint(directorio)
