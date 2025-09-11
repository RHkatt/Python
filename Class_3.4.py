# Generar un grupo de 10 numeros aleatorios en la lista
# Ordenar la lista de mayor a menor
# Mostrar la lista ordenada de ascendente y descendente
import random as rd
lista = []
# Genera una lista de 10 numeros aleatorios entre 0 y 50 sin repeticion
# N0 = rd.sample(range(0, 50), 10) # sample devuelve una lista
for i in range(10):
    N = rd.randint(0,50)  # randint devuelve un numero entre 0 y 50
    lista.append(N) # append agrega el numero a la lista
print(f"Lista original: {lista}")
# Dividir la lista en dos listas, con numeros mayores y menores
Vmayor = []
Vmenor = []
for i in lista:
    if i >= 25:
        Vmayor.append(i)
    else:
        Vmenor.append(i)
# Ordenar la lista
orden = len(lista) # len devuelve la cantidad de numeros en la lista    
for a in range(orden):
    for b in range(0, orden - a - 1):
        if lista[b] > lista[b + 1]:
            # Intercambiar los elementos si están en el orden incorrecto
            lista[b], lista[b + 1] = lista[b + 1], lista[b]    
# salida de datos
# Se puede usar {Vmayor[:5]} para mostrar los primeros 5 numeros
print(f"Los numeros altos: {Vmayor}") 
print(f"Los numeros bajos: {Vmenor}") 
print(f"Lista ascendente : {lista}")
# Tambien se podria el mismo if solo que cambia el signo de > a <
print(f"Lista descendente : {lista[::-1]}") # lista[::-1] invierte la lista