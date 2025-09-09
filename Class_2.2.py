valor_txt = input("Ingrese los valores de la Temperatura en °C :")
try:  # Código que podría generar un error
    valor_float = float(valor_txt)
    if valor_float >= 30: # Condicion if si la "Condicion 1" es verdadera
        print("Alerta alta temperatura")
    elif valor_float < 0: # Condicion elif si la "Condicion 2" es verdadera
        print("Temperatura bajo cero")
    else: # Condicion else es la "Condicion 3" si ninguna condición anterior fue verdadera
        print("Temperatura normal")
except ValueError:   # Código que se ejecuta por si ocurre un error
    print("Error: Entrada no válida. Por favor, ingrese un número (ej. 25.5).")