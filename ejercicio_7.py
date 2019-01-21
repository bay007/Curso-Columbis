###############################################################################
## Modificar odas las variables de modo que todas las expresiones sean True. ##
###############################################################################

var1 = 25
var2 = "python"
var3 = [1,2,3,4,5]
var4 = (1,2,"Hello, Python!")
var5 = {"egg":"salad","edad":7, "happy":"feliz"}
var6 = 45.2

##############################################
## No editar nada debajo de éste ocmentario ##
##############################################

# integers
print("##############INTEGER##############")
print(type(var1) is int)
print(type(var6) is float)
print(var1 < 35)
print(var1 <= var6)

# strings
print("##############STRING##############")
print(type(var2) is str)
print(var2[5] == 'n' and var2[0] == "p")#python


# lists
print("##############LISTA##############")
print(type(var3) is list)
print(len(var3) == 5)

# tuples
print("##############TUPLAS##############")
print(type(var4) is tuple)
print(var4[2] == "Hello, Python!")

# dictionaries
print("##############DICCIONARIOS##############")
print(type(var5) is dict)
print("happy" in var5)
print(7 in var5.values())
print(var5.get("egg") == "salad")
print(len(var5) == 3)
var5["tuna"] = "fish"
#print(var5)
var5.pop('edad')
print(len(var5) == 3)
