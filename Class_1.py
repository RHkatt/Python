import datetime as dt # importar funciones - modulo fecha
import random as rd #  importar funciones - modulo aleatorio
Nombre = "Katherin" # constantes
Fecha = dt.datetime.now().strftime("%d/%m/%Y, %H:%M:%S") # variable
# Definir valores aleatorios
print("Hola "+ Nombre)
print(Fecha) # salida de la variable
for i in range(10): # bucle for 
    v = rd.randint(0,1023) # valor aleatorio entre 1 y 100
    if v < 100: # condicion
        print("valor bajo: "+ str(v)) # salida de la variable
    elif v < 500: # condicion
        print("valor medio: "+ str(v)) # salida de la variable