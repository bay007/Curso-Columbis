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

numeros_romanos = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}

lista_decimal = [0]
decimal_anterior = 0
decimal = 0

cadena_romano = "MCMXC"

for romano in cadena_romano:
    decimal   = numeros_romanos.get(romano, 0)
    
    if decimal_anterior >= decimal:
        lista_decimal.append(decimal)
    else:
        lista_decimal.pop()
        lista_decimal.append(decimal - decimal_anterior)
    decimal_anterior = decimal

valor_decimal = sum(lista_decimal)

print(f"El número romano {cadena_romano} equivale en decimal a: {valor_decimal}")