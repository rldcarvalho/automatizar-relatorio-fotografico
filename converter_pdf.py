#pip3 install pdfkit
#Instalar o wkhtmltopdf
#adicionar o caminho ~wkhtmltopdf\bin a variável PATH nas variáveis de ambiente do windows

import pdfkit
pdfkit.from_file('index.html', 'relatorio.pdf')
