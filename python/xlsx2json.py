import os
import pandas as pd

# Nombre del archivo Excel (ajústalo a tu archivo)
archivo_excel = "Datos2.xlsx"

# Directorio donde se guardarán los archivos JSON
directorio_salida = "public/data"

# Crea el directorio si no existe
os.makedirs(directorio_salida, exist_ok=True)

# Lee todas las hojas del archivo Excel en un diccionario de DataFrames
hojas = pd.read_excel(archivo_excel, sheet_name=None)

# Itera sobre cada hoja y guarda su contenido en un archivo JSON diferente
for nombre_hoja, df in hojas.items():
    # Convierte el DataFrame a JSON con caracteres UTF-8
    json_resultado = df.to_json(orient="records", indent=4, force_ascii=False)
    
    # Define el nombre del archivo JSON basado en el nombre de la hoja
    archivo_json = os.path.join(directorio_salida, f"{nombre_hoja}.json")
    
    # Guarda el JSON en un archivo
    with open(archivo_json, "w", encoding="utf-8") as archivo:
        archivo.write(json_resultado)
    
    print(f"Archivo JSON guardado como {archivo_json}")
