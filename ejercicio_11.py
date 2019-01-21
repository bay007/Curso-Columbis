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

---para impresion
pprint= Modulo, pprint= Funcion
import jason


"""
from faker import Faker
from pprint import pprint
import json

fake=Faker('es_MX')


personas = {}
lista = []
persona = 0
id = 1
#myDict json

for persona in range(5):
    personas.update({"id": persona,"nombre":fake.name(),"direccion":fake.address()})
    lista.append(personas)
    #myDict['dict'].append({personas})
    #myDict['dict'].append(({"id": persona,"nombre":fake.name(),"direccion":fake.address()}))
    #test = json.dumps(lista)

"""
myDict['dict'].append(({'a': 'aaaa', 'b': 'aaaa', 'c': 'aaaa'}))
test = json.dumps(myDict)
print(test)  
"""  
#test = json.dumps(lista)
#print(len(personas.items()))
#print(len(lista))
print(len(lista))
test = json.dumps(lista)
print(len(test))
#pprint(lista)
pprint(test)

