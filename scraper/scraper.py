import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# URL de la página de libros más populares en Project Gutenberg
URL = "https://www.gutenberg.org/browse/scores/top"

# Cabeceras para evitar bloqueos
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

def obtener_detalles_libro(url):
    """ Extrae el autor y el número de descargas del libro. """
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    # Obtener autor
    autor = "Desconocido"
    if soup.find("h1"):
        autor = soup.find("h1").text.strip()
    elif soup.find("h2"):
        autor = soup.find("h2").text.strip()

    # Obtener número de descargas
    descargas = "No disponible"
    downloads_section = soup.find("td", string=lambda text: text and "downloads" in text.lower())
    if downloads_section:
        descargas = downloads_section.text.strip()

    return autor, descargas

def obtener_libros():
    """ Extrae los libros más populares de Gutenberg con título, enlace, autor e idioma. """
    response = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Lista para almacenar los libros
    libros = []

    # Encontrar la lista de libros en la página
    ol = soup.find('ol')

    # Iterar sobre los elementos de la lista
    for li in ol.find_all('li')[:30]:  # Limitar a 30 libros para evitar bloqueos
        try:
            titulo = li.get_text()
            enlace_relativo = li.find('a')['href']
            enlace = f"https://www.gutenberg.org{enlace_relativo}"
            
            # Obtener detalles adicionales (autor e idioma)
            autor, idioma = obtener_detalles_libro(enlace)
            
            libros.append({"titulo": titulo, "autor": autor, "idioma": idioma, "enlace": enlace})
            
            time.sleep(1)  # Pequeña pausa para evitar bloqueos del servidor
        except Exception as e:
            print(f"❌ Error obteniendo datos de un libro: {e}")

    return libros

def guardar_csv(libros):
    """ Guarda los libros en formato CSV. """
    df = pd.DataFrame(libros)
    df.to_csv("scraper/libros_populares.csv", index=False, encoding="utf-8")
    print("✅ CSV guardado correctamente en 'scraper/libros_populares.csv'")

if __name__ == "__main__":
    libros = obtener_libros()
    
    if libros:
        print("🔍 Libros obtenidos:")
        for libro in libros[:5]:  # Mostrar los primeros 5 libros en consola
            print(libro)
        
        guardar_csv(libros)
    else:
        print("⚠️ No se encontraron libros.")
