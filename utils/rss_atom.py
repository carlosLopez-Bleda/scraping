import feedparser
import json
import os

# Feeds de noticias de libros
FEEDS = {
    "The Guardian - Books": "https://www.theguardian.com/books/rss",
    "NPR Books": "https://feeds.npr.org/1032/rss.xml",
    "NY Times - Books": "https://rss.nytimes.com/services/xml/rss/nyt/Books.xml"
}

# Ruta donde guardaremos el JSON
OUTPUT_JSON = os.path.join("backend", "noticias.json")

def obtener_noticias():
    """ Extrae noticias de libros desde los feeds RSS/ATOM """
    noticias = []
    
    for fuente, url in FEEDS.items():
        feed = feedparser.parse(url)
        
        for entrada in feed.entries[:5]:  # Limitar a 5 noticias por fuente
            noticia = {
                "titulo": entrada.title,
                "link": entrada.link,
                "fuente": fuente
            }
            noticias.append(noticia)
    
    return noticias

def guardar_noticias_json():
    """ Guarda las noticias en un archivo JSON """
    noticias = obtener_noticias()
    
    with open(OUTPUT_JSON, "w", encoding="utf-8") as archivo:
        json.dump(noticias, archivo, indent=4, ensure_ascii=False)

    print(f"✅ Noticias guardadas en {OUTPUT_JSON}")

if __name__ == "__main__":
    guardar_noticias_json()
