# ===RUTA DEL ARCHIVO DE INGRESO===
# # Busca la ruta donde esta el codigo y luego se añade la ruta del archivo de ingreso
from pathlib import Path # Importa path (busca el lugar del archivo)
# Sube desde la src/ a la raiz del proyecto C:\Usuarios\19mar\Python_katt\Python
ROOT = Path(__file__).resolve().parents[1] 
TXT = ROOT / "Python" / "Lectura de Datos" / "Archs sucios" / "mediciones_basico.txt" # Ultima ruta del archivo "Python"
# print(ROOT) Imprime la ruta del archivo

# ===LECTURA Y LIMPIEZA DEL ARCHIVO TXT===
valores = []
with open(TXT, 'r', encoding='"utf-8"') as f:
    for linea in f: # Lee linea por linea del archivo ingresado
        s = linea.strip() # Elimina los espacios en blanco al inicio y al final
        if not s or s.startswith('#'): # Si la linea esta vacia o empieza con # (comentario)
            continue # Salta a la siguiente linea
        if not s or s.startswith('!'): # Si la linea esta vacia o empieza con "!" (exclamacion)
            continue # Salta a la siguiente linea
        s = s.replace(',', '.') # Reemplaza las comas por puntos (para decimales)
        try:
            # Convierte la cadena s a un número decimal (float) y lo agrega a la lista valores.
            valores.append(float(s)) 
        except ValueError:
            # Si no es ni linea ni numero, debe saltarlo
            pass 
print(f"Lista depurada: {valores}") # Valores limpios

# ===CLASIFICACION DE VALORES===
Valto = []
Vbajo = []
for i in valores: # Recorre cada valor en la lista valores limpia
    if i >= 5: # Si el valor es mayor o igual a 5
        Valto.append(i) 
    else:
        Vbajo.append(i)
print(f"Val. altos: {Valto}") # Imprime los valores altos
print(f"Val. bajos: {Vbajo}") # Imprime los valores bajos 
print(f"Cantidad de valores altos: {len(Valto)}") # Imprime la cantidad de valores altos
print(f"Cantidad de valores altos: {len(Vbajo)}") # Imprime la cantidad de valores bajos