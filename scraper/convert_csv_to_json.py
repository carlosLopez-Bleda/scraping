import pandas as pd
import os
import json

# Rutas de archivos
CSV_PATH = os.path.join("scraper", "libros_populares.csv")
JSON_PATH = os.path.join("backend", "libros_populares.json")

def convertir_csv_a_json():
    try:
        df = pd.read_csv(CSV_PATH)
        df.to_json(JSON_PATH, orient="records", indent=4, force_ascii=False)
        print(f"✅ Archivo JSON guardado en {JSON_PATH}")
    except Exception as e:
        print(f"❌ Error al convertir CSV a JSON: {e}")

if __name__ == "__main__":
    convertir_csv_a_json()
