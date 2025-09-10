print("==== REPORTE DEL SENSOR ====")
# Entrada de Datos
while True:
    name_student = input("Ingrese el Nombre del estudiante: ")
    # Elimina los espacios y verifica que solo sean letras
    if name_student.replace(" ", "").isalpha():
        break  # Salida del bucle porque el nombre es válido
    else:
        print("Error: Entrada no válida, ingrese un nombre (Ej: Alonso Carrera)")
while True: # Bucle para repetir hasta que la entrada sea válida
    name_equipo = input("Ingrese el Nombre del equipo: ")
    # Verifica si al menos uno de los caracteres es una letra
    if any(a.isalpha() for a in name_equipo):
        break # Salida del bucle porque el nombre es válido
    else:
        print("Error: Intentalo de nuevo)")
# Lecturas de voltaje
print("=== LECTURAS DEL SENSOR ===")
while True: # Bucle para repetir hasta que la entrada sea válida
    try:
        # Conversion de las lecturas a float usando map y split es el espacio entre lecturas
        Lectura1, Lectura2 = map(float, input("Lecturas (V): ").split(","))
        break # Salida del bucle porque las lecturas son válidas
    except ValueError:
         print("Error: Entrada no válida (Ej: 12.5 , 15.3)")
promedio = (Lectura1 + Lectura2) / 2
print(f"Promedio : {promedio :.3f} V") # Mostrar promedio con 3 decimales
# Condicionales para el Estado del sensor
if promedio >= 5: # Condicion if si la "Condicion 1" es verdadera
    print("Estado : Umbral alto")
elif promedio < 0: # Condicion elif si la "Condicion 2" es verdadera
    print("Estado : Umbral bajo")
else: # Condicion else es la "Condicion 3" si ninguna condición anterior fue verdadera
        print("Estado : Umbral medio")
