import os

def crear_carpeta():
    print("Preparándose para la creación de la carpeta. ¿Desea continuar (S/N)?")
    choice = input()
    if choice.lower() == 's':
        foldername = input("Introduzca el nombre de la carpeta a crear: ")
        os.makedirs(foldername)
        os.makedirs(os.path.join(foldername, 'src', 'css'))
        os.makedirs(os.path.join(foldername, 'src', 'js'))
        os.makedirs(os.path.join(foldername, 'src', 'imgs'))

        with open(os.path.join(foldername, 'index.html'), 'w') as html_file:
            html_file.write('''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <script src="src/js/main.js"></script>
    <link rel="stylesheet" href="src/css/styles.css">
</body>
</html>''')

        # Crear archivos main.js y styles.css
        with open(os.path.join(foldername, 'src', 'js', 'main.js'), 'w') as js_file:
            js_file.write('// JavaScript Code')

        with open(os.path.join(foldername, 'src', 'css', 'styles.css'), 'w') as css_file:
            css_file.write('* Estilos Globales */')

        print("Carpeta y archivos creados exitosamente.")
    else:
        print("Operación cancelada.")

if __name__ == "__main__":
    crear_carpeta()

