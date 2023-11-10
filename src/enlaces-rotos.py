import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# Función para verificar enlaces locales y condiciones avanzadas en un archivo HTML
def check_local_links_advanced(html_file):
    try:
        with open(html_file, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            links = soup.find_all('a')
            for link in links:
                href = link.get('href')
                if href:
                    if not href.startswith(('http://', 'https://')) and not href.startswith('#'):
                        local_path = os.path.join(os.path.dirname(html_file), href)
                        if not os.path.isfile(local_path):
                            print(f'Enlace roto en {html_file}: {href}')
                    elif not link.text.strip():
                        print(f'Enlace en {html_file} no contiene texto: {href}')
    except Exception as e:
        print(f'Error al procesar el archivo HTML: {html_file}')
        print(e)

# Directorio que contiene los archivos HTML a verificar
html_directory = '.'

# Recorre todos los archivos HTML en el directorio
for root, dirs, files in os.walk(html_directory):
    for file in files:
        if file.endswith(".html"):
            html_file = os.path.join(root, file)
            check_local_links_advanced(html_file)
