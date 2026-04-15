import csv
from pathlib import Path

CSV_FILE = "jobs.csv"
HTML_FILE = "jobs.html"

rows = []

# Leer el CSV
with open(CSV_FILE, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    headers = next(reader, [])  # primera fila como cabecera
    for row in reader:
        rows.append(row)

# Construir HTML
html = [
    "<!DOCTYPE html>",
    "<html lang='en'>",
    "<head>",
    "  <meta charset='UTF-8'>",
    "  <title>Job Offers</title>",
    "  <style>",
    "    table { border-collapse: collapse; width: 100%; font-family: sans-serif; }",
    "    th, td { border: 1px solid #ccc; padding: 8px; }",
    "    th { background-color: #f2f2f2; text-align: left; }",
    "    tr:nth-child(even) { background-color: #fafafa; }",
    "    a { color: #0066cc; }",
    "  </style>",
    "</head>",
    "<body>",
    "  <h1>Job Offers</h1>",
    "  <table>",
    "    <thead>",
    "      <tr>",
]

for h in headers:
    html.append(f"        <th>{h.capitalize()}</th>")

html += [
    "      </tr>",
    "    </thead>",
    "    <tbody>",
]

for row in rows:
    html.append("      <tr>")
    for i, cell in enumerate(row):
        # Si es la columna de URL, la convertimos en enlace clicable
        if headers and headers[i].lower().startswith("url"):
            html.append(f"        <td><a href='{cell}' target='_blank'>{cell}</a></td>")
        else:
            html.append(f"        <td>{cell}</td>")
    html.append("      </tr>")

html += [
    "    </tbody>",
    "  </table>",
    "</body>",
    "</html>",
]

# Guardar HTML
Path(HTML_FILE).write_text("\n".join(html), encoding="utf-8")
print(f"HTML generado: {HTML_FILE}")
