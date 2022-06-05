foto1 = "foto 1.jpeg"
foto2 = "foto 2.jpg"
gemini = "Captura de tela.png"
lista_fotos = [foto1, foto2, gemini]

with open("index.html", "w") as relatorio:
    relatorio.write("""<!DOCTYPE html>
<html lang=\"pt-br\">
<head>
<meta charset=\"UTF-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
<title>Relatorio Fotografico</title>
</head>
<body>
""")
    for foto in lista_fotos:
        relatorio.write(f"<img src=\"{foto}\" width=\"450px\">\n")
        relatorio.write("<br>\n")
    relatorio.write("""</body>
</html>
""")


