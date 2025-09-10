import random as rd
lista = [] # Lista vacia
for i in range (5): # Bucle para 5 iteraciones
    num = rd.randint(1, 10) # Numero aleatorio entre 1 y 10
    lista.append(num) # appened agrega la lista
print(lista) # Imprime la lista

vol_sqrt=[] # Lista vacia
V = [8, 27, 64, 125] # Lista dada
for i in V: # Bucle para recorrer la lista
    vol_sqrt.append(i*i) # Agrega a la lista el volatje al cuadrado
print(f"El volatje al cuadrado es : {vol_sqrt}") 
      
lecturas = [4.5, 6.7, 8.9, 10.1]
for idx, vol in enumerate(lecturas, start=1): # enumerate para obtener indice y valor
   print(f"{idx}: {vol: .2f} V") # Imprime indice y valor con 2 decimales
    
