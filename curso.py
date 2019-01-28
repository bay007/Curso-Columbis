#EXCEPTIONS
'''
numeros = [0, 1, 2, 3]


try:
    ar = open("log'log", "a")
    1/0
    dict_={"a":3}
    dict_["b"]
    numeros[0]
    numeros[10]
except Exception as error:
    print(f"El error es:  {error}")
    ar.write(f"El error es: {error}\n")
    ar.close()
else:
    pass
finally:
    print("Cerrando archivo")
    ar.close()
    '''

# CLASES
# Por convensión se pone en mayúsculas
# Debe de ser un __init__ por clase, lo cual es el constructor con ayuda de los atributos definidos
# Después se definen los métodos o modelasods del objeto / clase
# la palabra reservada "self" debe de ir en los métodos y sirve para hacerlo disponibles a todos los métodos
# Una instacia es utilizar la clase, es decir utilizar el objeto con atributos definidos

# Operadores ternarios "if en una linea"

class Coche:

    def __init__(self, gasolina):
        self.gasolina = gasolina
        self.encendido = False
        print(f"Tenemos {gasolina} litros")

    def arrancar(self):
        if self.gasolina > 0:
            self.encendido = not self.encendido
            print("Arranca") if self.encendido else print("Apagado")
        else:
            self.encendido = False
            print("No Arranca")

    def conducir(self):
        if self.gasolina > 0 and self.encendido == True:
            self.gasolina -= 1
            print(f"Quedan {self.gasolina} litros")
        else:
            print("No se mueve")

coche_juan = Coche(20)
coche_juan.arrancar()
coche_juan.conducir()


from random import randint

class Dado:

    def __init__(self, num_caras = 6):
        self.numero_caras = num_caras
        self.valor = None
    
    def tirar_dado(self):
        self.valor = randint(1, self.numero_caras)
        #return self.valor

    # Magic Methods
    def __repr__(self):
        return f"Valor {self.valor}"

'''
dado_1 = Dado(18)
print(dado_1)
print(dado_1.tirar_dado())
print(dado_1.valor)
'''

class Tablero:

    def __init__(self, numero_dados = 2):
        self.numero_dados = numero_dados
        self.dados = []
        for _ in range(self.numero_dados):
            self.dados.append(Dado())

    def tirar(self):
        for dado in self.dados:
            dado.tirar_dado()

tbl = Tablero()
tbl.tirar()
# for dado in tbl.dados:
#     print(dado.valor)
print(tbl.dados)

class Calculadora:
    '''DOCSTRINGS format
    Esta clase sirve para calcular el perímetro y área de un cuadrado/rectángulo.
    Calculadora(base, altura)
    '''

    def __init__(self, base = 0, altura = 0):
        self.base = base
        self.altura = altura
        self.valor_area = 0
        self.valor_perimetro = 0
    
    def area(self):
        '''
        Cálculo de área
        '''
        self.valor_area = self.base * self.altura

    def perimetro(self):
        self.valor_perimetro = 2 * (self.base + self.altura)
    
    def __repr__(self):
        return f"El valor del área corresponde a {self.valor_area} y el valor del perímetro corresponde a {self.valor_perimetro}"

calc = Calculadora(base = 4, altura = 2)
print(calc)
print(calc.area())
print(calc.valor_area)
print(calc.perimetro())
print(calc.valor_perimetro)
print(calc.__repr__())