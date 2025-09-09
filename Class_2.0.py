Nombre = "Katherin"   # constante por convecion
edad = 20             # int
voltaje = 5.26715     # float
activo = True         # bool
print(type(Nombre))
print(type(edad))
print(type(voltaje))
print(type(activo))
# se pone str, que transforma a letras, porque edad es un numero
print("Hola "+ Nombre + " Edad: "+ str(edad))
# f-string (formato para cadenas de caracteres, letras)
print(f"Hola, {Nombre}. Edad: {edad}")
# para float {voltaje:.2f} el numero ej:".2" antes de f indica el numero de decimales despues de la coma
print(f"Volatje, {voltaje:.2f} V / Activo: {activo}")
print(f"Tipos -- Edad: {type(edad).__name__}, Voltaje: {type(voltaje).__name__}")