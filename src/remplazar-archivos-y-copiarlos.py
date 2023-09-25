import shutil
import os

# Definir los nombres de los archivos a copiar y reemplazar
nombre_archivo_origen1 = "src/css/styles.css"
nombre_archivo_destino1 = "pages/src/css/styles.css"

# Obtener la ruta del directorio actual
ruta_actual = os.getcwd()

# Definir las rutas completas de los archivos de origen y destino
ruta_origen1 = os.path.join(ruta_actual, nombre_archivo_origen1)
ruta_destino1 = os.path.join(ruta_actual, nombre_archivo_destino1)

# Mostrar las rutas de origen y destino
print("Ruta de origen: ", ruta_origen1)
print("Ruta de destino: ", ruta_destino1)

# Copiar y reemplazar el archivo
shutil.copyfile(ruta_origen1, ruta_destino1)

print("Archivos copiados y reemplazados exitosamente.")
input("Presiona Enter para salir...")

