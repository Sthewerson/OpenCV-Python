import PyPDF2

# Abre o arquivo pdf
# Lembre-se também que você precisa colocar o caminho absoluto
pdf_file = open('./plr_desafio.pdf', 'rb')

# Faz a leitura usando a biblioteca
read_pdf = PyPDF2.PdfReader(pdf_file)

# Pega o número de páginas
number_of_pages = len(read_pdf.pages)

# Lê a primeira página completa
page = read_pdf.pages[0]

# Extrai apenas o texto
page_content = page.extract_text()

# Código para encontrar o texto após as palavras ‘INFORMAÇÃO NUTRICIONAL’
indice1 = page_content.find('INFORMAÇÃO NUTRICIONAL')
tabela_nutricional = page_content[indice1:]

pdf_file.close()

# Já para rodar a biblioteca de OCR tesseract, utilize os seguintes comandos:
import pytesseract

# Texto puro
texto_rotulo = pytesseract.image_to_string('files/lacta1.png', lang='por')

# Texto com as localizações por nível, página, etc.
dados = pytesseract.image_to_data('files/lacta2.png', lang='por')

# Bounding box da localização das imagens dos rótulos
boundings = pytesseract.image_to_boxes('files/lacta2.png', lang='por')

print(texto_rotulo)
print(dados)
print(boundings)
