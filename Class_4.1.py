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
from statistics import mean

# ===PATH - RUTA DE ACCESO===
ROOT = Path(__file__).resolve().parents[1]  # sube desde src/ a la raíz del proyecto C:\Users\19mar\Python_katt\Python
TXT  = ROOT / "Python" / "Lectura de Datos" 
IN_FILE = TXT /"Archs sucios" / "voltajes_250_sucio.csv" #archivo de Ingreso
OUT_FILE = TXT / "Archs depurados" /"volajes_250_limpio.csv" #archivo de Salida
# print(IN_FILE, OUT_FILE) Imprime la ruta del archivo

# ===APERTURA DE ARCHIVOS===
with open(IN_FILE,'r', encoding="utf-8", newline="") as fin,\
    open(OUT_FILE, "w", encoding="utf-8", newline="") as fout:
    reader = csv.DictReader(fin, delimiter=';')       # usa ',' si tu archivo lo requiere
    writer = csv.DictWriter(fout, fieldnames=["timestamp", "value","control"]) #crea el archivo y su cabera
    writer.writeheader()

# ===LIMPIEZA LINEA POR LINEA Y SELECCIONAR UN CRUDO EN RAW===
    total = kept = 0
    bad_ts = bad_val = 0
    voltajes = []
    for row in reader:
        total += 1
        ts_raw  = (row.get("timestamp") or "").strip()
        val_raw = (row.get("value") or "").strip()
        
# ===LIMPIEZA DE DATOS===
        val_raw = val_raw.replace(",", ".")
        val_low = val_raw.lower()
        if val_low in {"", "na", "n/a", "nan", "null", "none", "error"}:
            bad_ts += 1
            continue  # saltar fila
        try:
            val = float(val_raw)
        except ValueError:
            bad_ts += 1
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
            bad_ts += 1
            continue  # saltar fila si no pudimos interpretar la fecha
# ===SISTEMA DE CONTROL DE VOLTAJE===       
        if val >= 5: # Si el valor es mayor o igual a 5
            control = "Cuidado" 
        else:
            control = "OK"
        voltajes.append(val) #agrego a la lista voltajes el valor val
#grabar datos en writer
        writer.writerow({"timestamp": ts_clean, "value": f"{val:.2f}", "control": control})
        kept += 1 #sume 1 kept, en nuestro caso cambia de fila

# ===KPIs===
n = len(voltajes)
if n ==0:
    kpis = {"n":0, "min":None, "max":None, "prom":None , "alertas": 0, "alerts_pct":0.0} # por facilidad se usa diccionario
else:
    alertas = sum(v >=5 for v in voltajes) # Estructura generadora de alertas repetitivas simples
    kpis = {
        "n": n,
        "min": min(voltajes),
        "max": max(voltajes),
        "prom": mean(voltajes),
        "alertas": alertas,
        "alerts_pct": 100.0 * alertas / n,
    }    
print(f"De un total de: {int(kpis["n"])} datos, los val max y min son: {float(kpis["max"]):.2f}, {kpis["min"]}")