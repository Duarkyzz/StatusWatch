import csv


def exportar_csv(path, rows):
    def safe(value):
        text = "" if value is None else str(value)
        # Evita interpretar conteúdo externo como fórmula ao abrir no Excel.
        return "'" + text if text.lstrip().startswith(("=", "+", "-", "@")) else text

    with open(path, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["ID", "URL", "HTTP", "Status", "Resposta (s)", "Data"])
        writer.writerows([safe(value) for value in row] for row in rows)
