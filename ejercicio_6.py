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

numeros_base = {    "I":1,
                    "V":5,
                    "X":10,
                    "L":50,
                    "C":100,
                    "D":500,
                    "M":1000}


numero_romano = input("¿Dame una numero romano?")


tamanio = len (numero_romano) 
obt_numero_ant = 0
print(tamanio)

if tamanio == 1:
     
        obt_numero = numeros_base.get(numero_romano)
else:
    for conteo_letras in range(tamanio): 
        ls_caracter = numero_romano[conteo_letras]
        print(f"caracter: {ls_caracter}") 
        obt_numero = numeros_base.get(ls_caracter)
        print(obt_numero)

        if obt_numero_ant > obt_numero:
            obt_numero = obt_numero - obt_numero_ant
            print(obt_numero)
        else:
            obt_numero = obt_numero + obt_numero_ant
            print(obt_numero)

    



"""
for conteo_letras in range(tamanio):   
   
    if tamanio > 1:
        if obt_numero_ant <= obt_numero_act:
            obt_numero_act = obt_numero_act - obt_numero_ant
        else:
            obt_numero_act = obt_numero_act + obt_numero_ant

        obt_numero_ant = obt_numero_act
        print(obt_numero_act)
    
    else:    
        print(conteo_letras)
        obt_numero_act = numeros_base.get(conteo_letras) 



print(obt_numero_act)

 
for numero in numeros_base.items(): 
    obt_numero = numeros_base.get(numero_romano)
 
"""