import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import fitz  # import PyMuPDF

def Save_to_csv(pdf_path, csv_save_path):
  carpeta_pdf = pdf_path
  carpeta_csv = csv_save_path

  os.makedirs(carpeta_csv, exist_ok=True)

  archivos_pdf = [archivo for archivo in os.listdir(carpeta_pdf) if archivo.endswith('.pdf')]

  for archivo_pdf in archivos_pdf:
      ruta_completa = os.path.join(carpeta_pdf, archivo_pdf)
      pdf_documento = fitz.open(ruta_completa)
      for i, page in enumerate(pdf_documento):
        tabs = page.find_tables()
        df = []
        for tab in tabs:
          obj = tab.extract()
          for j in obj:
            if( len(j) > 3):
              df.append(j)
        data = pd.DataFrame(df)
        csv_file_path = os.path.join(carpeta_csv, f'{archivo_pdf}_page{i}.csv')
        data.to_csv(csv_file_path, index=False)

def Export_to_dataframe(pdf_path):
  Final_data = []
  carpeta_pdf = pdf_path
  archivos_pdf = [archivo for archivo in os.listdir(carpeta_pdf) if archivo.endswith('.pdf')]

  for archivo_pdf in archivos_pdf:
      ruta_completa = os.path.join(carpeta_pdf, archivo_pdf)
      pdf_documento = fitz.open(ruta_completa)
      for i, page in enumerate(pdf_documento):
        tabs = page.find_tables()
        df = []
        for tab in tabs:
          obj = tab.extract()
          for j in obj:
            if( len(j) > 3):
              df.append(j)
        Final_data.append(df)
  
  return Final_data

def PDF_Scrapper( decision = 'csv', pdf_paths = '/content/drive/MyDrive/Datos PDF/', csv_save_paths = '/content/drive/MyDrive/Datos PDF/CSV/'):
  if( decision == 'csv' ):
    Save_to_csv( pdf_paths, csv_save_paths )
  if( decision == 'df' ):
    return Export_to_dataframe( pdf_paths )