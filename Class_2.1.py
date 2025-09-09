import datetime as dt  # importar funciones - modulo fecha
import random as rd    # importar funciones - modulo aleatorio
fecha = dt.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
Nombre = "Katherin Marin"  
jefe = "Oscar Casas"
edad = 20           
activo = 25          
print(f"Informe redactado por {Nombre}, de {edad} años, practicante.")  
print(f"Fecha y Hora del envio: {fecha}")
print("Medicion del voltaje diario:")
for i in range(5): # bucle for 
    v = rd.randint(25,40) # valor aleatorio entre 1 y 60
    if v < 30: # condicion
        print(f"volatje: {v:.2f} V") 
        print("Motor activo: False")  
    elif v < 41: # condicion
        print(f"volatje: {v:.2f} V") # salida de la variable
        print("Motor activo: True")
print("Estos datos representan que hay una irregularidad,")
print("el motor a partir de un voltaje menor a 30, el motor deja de funcionar.")
print(f"Tipos -- Nombre y jefe: {type(Nombre).__name__}, {type(jefe).__name__}")
print(f"Tipos -- Fecha: {type(fecha).__name__},  Edad :{type(edad).__name__}")
print(f"Tipos -- Volatje: {type(v).__name__}")
print(f"Tipos -- Activo: {type(activo).__name__}")