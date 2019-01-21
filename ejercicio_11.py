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

    lista_datos = []
    
    for dato in range(int(num_datos)):
        num = num + 1
        
        numero = "{id:"+ str(num)
        lista_datos.append(numero)
        nombre = "Nombre:" + fake.name()
        lista_datos.append(nombre) 
        dir_pos = "Direccion_pos:"+fake.address()
        lista_datos.append(dir_pos)
        dir_fis = "Direccion_fiscal:"+fake.address()         
        lista_datos.append(dir_fis)
        lista_datos.append("}")
    return lista_datos
 

resultado =  obten_datos_persona(input("¿Cuantos datos quieres obtener?"))


print(json.dumps(resultado, indent = 3))
