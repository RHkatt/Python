# Crear una lista aleatoria de 10 valores menores a 10 voltios
# Verificar si los valores son mayores o menores a 5 voltios
# Imprimir en cada caso voltaje alto o voltaje bajo
import random as rd
Lista = [] # Lista vacia
#with open("valores.txt", "r") as archivo: # Abrir archivo en modo lectura
#    for linea in archivo: # Bucle para cada linea en el archivo
#        Lista.append(float(linea.strip())) # Agregar valor a la lista
#archivo.close() # Cerrar archivo
for i in range (10): # Bucle para 10 iteraciones
    N = rd.randint(0, 10) # Numero aleatorio entre -10 y 10
    Lista.append(N) # appened agrega la lista
print(Lista)
Vmayor = []
Vmenor = []
for i in Lista:
    if i >= 5:
        Vmayor.append(i)
    else:
        Vmenor.append(i)
print(f"Los voltajes mayores a 5V son: {Vmayor}")
print(f"Los voltajes menores a 5V son: {Vmenor}")    
    

   
