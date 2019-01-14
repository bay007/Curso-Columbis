def obtiene_romano(*args):
        numeros_romanos = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        numero_dado = args
        #numero_dado = "MCMLXVIII"
        suma = 0
        numero_anterior = 0
        valor_romano = 0
        for numero_romano in numero_dado[::-1]:
            valor_romano = numeros_romanos.get(numero_romano)   
            if valor_romano >= numero_anterior:
                suma = suma + valor_romano
            else:
                suma = suma - valor_romano 
            numero_anterior = valor_romano
        print(f"EL numero dado es {numero_dado}")
        print(f"La suma total es {suma}")        
        return(suma)

print(obtiene_romano("MCMLXVIII"))