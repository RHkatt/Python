# limpiar_csv_simple.py
# Objetivo: leer CSV "sucio", limpiar y guardar "limpio" con:
# - timestamp en formato ISO YYYY-MM-DDTHH:MM:SS
# - value como float con punto y 3 decimales
# - separador de salida: coma
# - filas inválidas: se saltan

# ===PARA LECTURA Y ESCRITURA===
import csv
from datetime import datetime
from pathlib import Path #importo el comando path (busca el lugar del codigo)

# ===PATH - RUTA DE ACCESO===
ROOT = Path(__file__).resolve().parents[1]  # sube desde src/ a la raíz del proyecto C:\Users\19mar\Python_katt\Python
TXT  = ROOT / "Python" 
IN_FILE = TXT / "voltajes_250_sucio.csv" #archivo de Ingreso
OUT_FILE = TXT / "volajes_250_limpio.csv" #archivo de Salida
# print(IN_FILE, OUT_FILE) Imprime la ruta del archivo

# ===APERTURA DE ARCHIVOS===
with open(IN_FILE,'r', encoding="utf-8", newline="") as fin,\
    open(OUT_FILE, "w", encoding="utf-8", newline="") as fout:
    reader = csv.DictReader(fin, delimiter=';')       # usa ',' si tu archivo lo requiere
    writer = csv.DictWriter(fout, fieldnames=["timestamp", "value"]) #crea el archivo y su cabera
    writer.writeheader()

# ===LIMPIEZA LINEA POR LINEA Y SELECCIONAR UN CRUDO EN RAW===
    total = kept = 0
    for row in reader:
        total += 1
        ts_raw  = (row.get("timestamp") or "").strip()
        val_raw = (row.get("value") or "").strip()
        
# ===LIMPIEZA DE DATOS===
        val_raw = val_raw.replace(",", ".")
        val_low = val_raw.lower()
        if val_low in {"", "na", "n/a", "nan", "null", "none", "error"}:
            continue  # saltar fila
        try:
            val = float(val_raw)
        except ValueError:
            continue  # saltar fila si no es número

# ===LIMPIEZA DE DATOS DE TIEMPO===
        ts_clean = None
        for fmt in ("%Y-%m-%dT%H:%M:%S", "%d/%m/%Y %H:%M:%S"):
            try:
                dt = datetime.strptime(ts_raw, fmt)
                ts_clean = dt.strftime("%Y-%m-%dT%H:%M:%S")
                break
            except ValueError:
                pass
#milisegundo (opcional)
        if ts_clean is None and "T" in ts_raw and len(ts_raw) >= 19:
            try:
                dt = datetime.strptime(ts_raw[:19], "%Y-%m-%dT%H:%M:%S")
                ts_clean = dt.strftime("%Y-%m-%dT%H:%M:%S")
            except ValueError:
                ts_clean = None

        if ts_clean is None:
            continue  # saltar fila si no pudimos interpretar la fecha

#grabar datos en writer
        writer.writerow({"timestamp": ts_clean, "value": f"{val:.2f}"})
        kept += 1 #sume 1 kept, en nuestro caso cambia de fila