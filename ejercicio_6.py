"""
Cree una función que tome un número romano como argumento
y devuelva su valor como un entero decimal numérico.
No es necesario validar la forma del número romano. 
Los números romanos modernos se escriben expresando cada dígito decimal del número que se va a codificar 
por separado, comenzando con el dígito que se encuentra más a la izquierda y omitiendo los 0s.
Así que 1990 se traduce como "MCMXC" (1000 = M, 900 = CM, 90 = XC) y 
2008 se traduce como "MMVIII" (2000 = MM, 8 = VIII). 
El número romano de 1666, "MDCLXVI", usa cada letra en orden descendente.

Ayuda:
Símbolo    Valor
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
"""

dicionario_romano = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

lista_menos = ("CM", "XC", "IX")

numeros_romanos = input("Escriba un número romano:")
numero_romano_decimal = 0
suma_decimal = 0
numero_anterior = ""

for numero_romano in numeros_romanos:

    numero = numeros_romanos[numero_romano_decimal]
    numero_decimal = dicionario_romano.get(numero)
    numero_anterior = numero_anterior+numero
    print(numero_anterior)
    #print(numero_decimal)
    if numero_anterior in lista_menos: 
    #if numero_anterior == "IX": 
        suma_decimal = numero_decimal - suma_decimal
    else:
        suma_decimal = numero_decimal + suma_decimal
    #print(suma_decimal)
    numero_romano_decimal = numero_romano_decimal + 1
    numero_anterior = f"{numero}"
    
print(suma_decimal)