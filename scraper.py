import requests
from bs4 import BeautifulSoup
import csv

# URL base
BASE_URL = "https://realpython.github.io/fake-jobs/"

# Obtener la página principal
response = requests.get(BASE_URL)
response.raise_for_status()  # Lanza error si la petición falla

soup = BeautifulSoup(response.text, "html.parser")

# Encontrar todas las ofertas de empleo
job_cards = soup.find_all("div", class_="card-content")

# Archivo CSV de salida
csv_filename = "jobs.csv"

with open(csv_filename, mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["titulo", "empresa", "ubicacion", "url_detalle"])

    for job in job_cards:
        # Extraer campos con manejo de ausencias
        titulo = job.find("h2", class_="title")
        empresa = job.find("h3", class_="company")
        ubicacion = job.find("p", class_="location")
        enlace = job.find("a", text="Apply")

        titulo = titulo.get_text(strip=True) if titulo else "N/A"
        empresa = empresa.get_text(strip=True) if empresa else "N/A"
        ubicacion = ubicacion.get_text(strip=True) if ubicacion else "N/A"
        url_detalle = BASE_URL + enlace["href"] if enlace else "N/A"

        writer.writerow([titulo, empresa, ubicacion, url_detalle])

print(f"Extracción completada. Datos guardados en {csv_filename}")
