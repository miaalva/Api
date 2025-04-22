import os
import requests
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

API_KEY = os.getenv("API_KEY_SEARCH_GOOGLE")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")

# Configuración de la consulta y los parámetros de búsqueda
query = 'filetype:sql "MySQL dump" (pass|password|passwd|pwd)'
page = 1
lang = "lang_es"

# Construcción de la URL para la API de Google Custom Search
url = (
    f"https://www.googleapis.com/customsearch/v1"
    f"?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={page}&lr={lang}"
)

# Realizar la solicitud a la API
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    results = data.get('items', [])

    if not results:
        print("No se encontraron resultados.")
    else:
        for item in results:
            print(f"Title: {item.get('title')}")
            print(f"Link: {item.get('link')}")
            print(f"Snippet: {item.get('snippet')}")
            print("-" * 80)
else:
    print(f"Error en la solicitud: {response.status_code}")

