import pandas as pd
import pdftables_api
import os
import fitz
import PyPDF2
import shutil

def cortar_crear_pdf(archivo_entrada, archivo_salida, pagina_inicial, pagina_final):
    # Abre el archivo PDF de entrada en modo binario
    with open(archivo_entrada, 'rb') as file:
        # Crea un objeto PDFReader
        pdf_reader = PyPDF2.PdfReader(file)

        # Crea un objeto PDFWriter
        pdf_writer = PyPDF2.PdfWriter()

        # Agrega las páginas deseadas al nuevo PDF
        for pagina in range(pagina_inicial - 1, pagina_final):
            pdf_writer.add_page(pdf_reader.pages[pagina])

        # Abre el archivo de salida en modo binario y escribe el nuevo PDF
        with open(archivo_salida, 'wb') as output_file:
            pdf_writer.write(output_file)

def Remain( key ):
  temporal_key = pdftables_api.Client(key)
  return temporal_key.remaining( )

def Sanitize(xlsx_save_path):
  a = 1

def Save_to_df(xlsx_save_path):

  carpeta_xlsx = xlsx_save_path
  archivos_xlsx = [archivo for archivo in os.listdir(carpeta_xlsx) if archivo.endswith('.xlsx')]
  Data = []

  for archivo_xlsx in archivos_xlsx:
    ruta_completa_xlsx = os.path.join(carpeta_xlsx, archivo_xlsx)
    df = pd.read_excel( ruta_completa_xlsx )
    Data.append( df )

  return Data

def Save_to_xlsx(pdf_path, xlsx_save_path, key):

  carpeta_pdf = pdf_path
  carpeta_xlsx = xlsx_save_path

  os.makedirs(carpeta_xlsx, exist_ok=True)

  api = pdftables_api.Client(key)

  archivos_pdf = [archivo for archivo in os.listdir(carpeta_pdf) if archivo.endswith('.pdf')]

  for archivo_pdf in archivos_pdf:
      ruta_completa_pdf = os.path.join(carpeta_pdf, archivo_pdf)
      pdf_documento = fitz.open(ruta_completa_pdf)
      for i, page in enumerate(pdf_documento):
        cortar_crear_pdf( ruta_completa_pdf, f'{archivo_pdf}_page{i}.pdf', i, i )
        api.xlsx( os.path.join('/content/', f'{archivo_pdf}_page{i}.pdf') , f'{archivo_pdf}_page{i}.xlsx')
        temp = os.path.join('/content/', f'{archivo_pdf}_page{i}.xlsx')
        shutil.copy({temp}, {carpeta_xlsx}) 

def PDF_Scrapper( decision = 'xlsx', api_key = 'mxz0vqzeb80a', pdf_paths = '/content/drive/MyDrive/DatosPDF/Test/', save_paths = '/content/drive/MyDrive/DatosPDF/Xlsx'):

    Save_to_xlsx( pdf_paths, save_paths, api_key )
    Sanitize( save_paths )

    if( decision == 'xlsx' ):
      return save_paths
    if( decision == 'rc' ):
      return Remain( api_key )
    if( decision == 'df' ):
      return Save_to_df( save_paths )