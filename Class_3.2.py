import random as rd
Lista = [] # Lista vacia
#with open("valores.txt", "r") as archivo: # Abrir archivo en modo lectura
#    for linea in archivo: # Bucle para cada linea en el archivo
#        Lista.append(float(linea.strip())) # Agregar valor a la lista
#archivo.close() # Cerrar archivo
for i in range (20): # Bucle para 10 iteraciones
    N = rd.randint(0, 30) # Numero aleatorio entre -10 y 10
    Lista.append(N) # appened agrega la lista
print(Lista)
Vmayor = []
Vmenor = []
Vmedio = []
for i in Lista:
    if i >= 20:
        Vmayor.append(i)
    elif i >= 10:
        Vmedio.append(i) 
    else:
        Vmenor.append(i)
print(f"Los voltajes altos: {Vmayor}")
print(f"Los voltajes medio: {Vmedio}")   
print(f"Los voltajes bajos: {Vmenor}") 
    

   
