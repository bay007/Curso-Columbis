###############################################################################
## Modificar odas las variables de modo que todas las expresiones sean True. ##
###############################################################################

var1 = 4 #entero #es menor a 35
var2 = "perenne" #es string #es una cadena, el elemento 5 es 'n' el elemento 0 es "p"
var3 = ["uno","dos","tres","cuatro","cinco"] # es una lista, su longitud es 5
var4 = ("Hello, Java!","Hello, C++!","Hello, Python!","Hello, PowerBuider") # es uan tupla #el element 2 es "Hello, Python!"
var5 = {"egg":"salad","happy":7,"tuna":"fish"} #es un diccionario #
var6 = 37.5 #flotante #es mayor o igual a 35

##############################################
## No editar nada debajo de éste ocmentario ##
##############################################

# integers
print(type(var1) is int)
print(type(var6) is float)
print(var1 < 35)
print(var1 <= var6)

# strings
print(type(var2) is str)
print(var2[5] == 'n' and var2[0] == "p")

# lists
print(type(var3) is list)
print(len(var3) == 5)

# tuples
print(type(var4) is tuple)
print(var4[2] == "Hello, Python!")

# dictionaries
print(type(var5) is dict)
print("happy" in var5)
print(7 in var5.values())
print(var5.get("egg") == "salad")
print(len(var5) == 3)
var5["tuna"] = "fish"
print(len(var5) == 3)