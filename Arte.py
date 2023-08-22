import PyPDF2
import pytesseract
from PIL import Image

class Arte:
    """
    Uma classe para manipular informações de arte e verificar sua conformidade com uma PLR (Product Label Review).

    Attributes:
        plr_ingredientes (str): O texto do campo Ingredientes da PLR.
        plr_alergenicos (str): O texto do campo alérgicos da PLR.
        plr_endereco (str): O primeiro texto do campo Signature Line Text da PLR.
        plr_industria (str): O segundo texto do campo Signature Line Text da PLR.
        plr_nutricional (list): Uma lista que representa a tabela INFORMAÇÃO NUTRICIONAL da PLR.

        ingredientes (str): O texto do campo Ingredientes da arte.
        alergenicos (str): O texto do campo alérgicos da arte.
        endereco (str): O primeiro texto do campo texto da arte.
        industria (str): O segundo texto do campo industria da arte.
        nutricional (list): Uma lista que representa a tabela INFORMAÇÃO NUTRICIONAL da arte.
        conformidade (int): Uma métrica que mede quão conforme está a arte em relação à PLR.
    """

    def __init__(self):
        self.plr_ingredientes = ""
        self.plr_alergenicos = ""
        self.plr_endereco = ""
        self.plr_industria = ""
        self.plr_nutricional = []

        self.ingredientes = ""
        self.alergenicos = ""
        self.endereco = ""
        self.industria = ""
        self.nutricional = []
        self.conformidade = 0

    def lerPlr(self, pdf_file_path):
        """
        Lê um arquivo PDF que contém informações da PLR (Product Label Review).

        Args:
            pdf_file_path (str): O caminho para o arquivo PDF da PLR.

        Returns:
            None

        Raises:
            FileNotFoundError: Se o arquivo PDF especificado não for encontrado.
        """
        pdf_file = open(pdf_file_path, 'rb')

        # Faz a leitura usando a biblioteca
        read_pdf = PyPDF2.PdfReader(pdf_file)


        # Lê a primeira página completa
        page = read_pdf.pages[0]

        # Extrai apenas o texto
        page_content = page.extract_text()
        
        # Encontra a posição do texto 'INFORMAÇÃO NUTRICIONAL'
        indice1 = page_content.find('INFORMAÇÃO NUTRICIONAL')

        # Atualiza os atributos da classe com os valores extraídos
        self.plr_ingredientes = page_content[:indice1].strip()
        self.plr_alergenicos = ""  
        self.plr_endereco = ""     
        self.plr_industria = ""    
        self.plr_nutricional = []  

        # Fecha o arquivo PDF
        pdf_file.close()

    def analisarArte(self, image_file_path):
        """
        Analisa uma imagem da arte e verifica sua conformidade com a PLR.

        Args:
            image_file_path (str): O caminho para o arquivo de imagem da arte.

        Returns:
            None
        """
        # Lê a imagem da arte
        image = Image.open(image_file_path)

        # Usa pytesseract para extrair o texto da imagem
        texto_arte = pytesseract.image_to_string(image, lang='por')

        # Atualiza os atributos da classe com os valores extraídos
        self.ingredientes = ""  
        self.alergenicos = ""   
        self.endereco = ""      
        self.industria = ""     
        self.nutricional = []   

        # Calcula a métrica de conformidade (um exemplo simples)
        if self.ingredientes == self.plr_ingredientes:
            self.conformidade += 20
        if self.alergenicos == self.plr_alergenicos:
            self.conformidade += 20
        if self.endereco == self.plr_endereco:
            self.conformidade += 20
        if self.industria == self.plr_industria:
            self.conformidade += 20
        if self.nutricional == self.plr_nutricional:
            self.conformidade += 20

    def listar_campos(self, image_file_path):
        """
        Lista os campos identificados em uma imagem da arte.

        Args:
            image_file_path (str): O caminho para o arquivo de imagem da arte.

        Returns:
            None
        """
        # Lê a imagem da arte
        image = Image.open(image_file_path)

        # Usa pytesseract para extrair informações da imagem
        dados = pytesseract.image_to_data(image, lang='por', output_type=pytesseract.Output.DICT)

        # Imprime cada item da array gerada pelo pytesseract.image_to_data
        for i in range(len(dados['text'])):
            print(f"Texto: {dados['text'][i]}")
            print(f"Altura: {dados['height'][i]}")
            print("---")

# Exemplo de uso da classe
arte = Arte()
arte.lerPlr("files/plr_desafio.pdf")
arte.analisarArte("files/lacta1.png")
arte.listar_campos("files/lacta2.png")
