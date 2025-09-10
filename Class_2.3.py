# Entrada de Datos
while True:
    name_student = input("Ingrese el Nombre del estudiante: ")
    # Elimina los espacios y verifica que solo sean letras
    if name_student.replace(" ", "").isalpha():
        break  # Salida del bucle porque el nombre es válido
    else:
        print("Error: Entrada no válida, ingrese un nombre (Ej: Alonso Carrera)")
while True: # Bucle para repetir hasta que la entrada sea válida
    try:
        number_equipo = int(input("Ingrese el Número del equipo: "))
        break  # Entrada válida, salir del bucle
    except ValueError:
        print("Error: Inténtalo de nuevo.(Ej: 12)")
# Lecturas de voltaje
print("La lista de lectura se termina cuando deja  de poner comas")  
while True: # Bucle para repetir hasta que la entrada sea válida
    try:
        # Conversion de las lecturas a float usando map y split con coma entre lecturas
        lecturas = list(map(lambda x: float(x.strip()),input("Lecturas (V): ").split(",")))
      
        break # Salida del bucle porque las lecturas son válidas
    except ValueError:
            print("Solo permite numeros (Ej: 12.5 , 15.3)")
# Cálculo del promedio
promedio = (sum(lecturas)) / len(lecturas) 
# Condicionales para el Estado del sensor
if promedio >= 5: # Condicion if si la "Condicion 1" es verdadera
    ESTADO = "ALTO ( >= 5V )"
elif promedio < 0: # Condicion elif si la "Condicion 2" es verdadera
    ESTADO= "BAJO ( < 0V )"
else: # Condicion else es la "Condicion 3" si ninguna condición anterior fue verdadera
    ESTADO= "MEDIO ( >= 5V Y > 0V )"
        
print("==== REPORTE DEL SENSOR ====")
print(f"Nombre del estudiante : {name_student} / Número del equipo : {number_equipo} ") 
print("=== LECTURAS DEL SENSOR ===")
# Muestra las lecturas como cadena separada por comas / Promedio con 2 decimales
print(f"Lecturas : {', '.join(map(str, lecturas))} V / Promedio : {promedio :.2f} V ")  
print(f"Estado del sensor : {ESTADO} ")

