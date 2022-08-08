# Projeto para automatizar um relatório fotográfico

<img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
 
Programa criado para auxiliar e automatizar etapa da elaboração de um relatório fotográfico.

## Etapas concluídas:
 - Desenvolvimento da interface gráfica.
 - Desenvolvimento gerador de arquivos HTML com as imagens do relatório;
 - Criado conversor do arquivo HTML para PDF;
 - Adicionado balões de comentários com as coordenadas na última imagem do PDF;

## Próximos passos:
 - Aprimorar método de inserção do balão de comentário;
 - Extra: armazenar print screen da tela direto na interface gráfica que recebe as imagens para o relatório.

---
### Bibliotecas Necessárias:

[PySimpleGUI](https://pypi.org/project/PySimpleGUI/):
```
pip3 install pysimplegui
```

[PDFKit](https://pdfkit.org/) (Instalar também o [wkhtmltopdf](https://wkhtmltopdf.org/)):
```
pip3 install pdfkit 
```

[pdf-annotate](https://github.com/plangrid/pdf-annotate)
```
pip3 install pdf-annotate
```
