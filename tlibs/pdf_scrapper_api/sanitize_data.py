import pandas as pd
import pdftables_api
import os

def find_key( palabra, datos ):
  for i, fila in datos.iterrows():
    for columna, valor in fila.items():
      valor = str( valor )
      if palabra in valor:
        return i

def find_key_last( palabra, datos, indice ):
  for i, fila in datos.iloc[indice:].iterrows():
    for columna, valor in fila.items():
      valor = str( valor )
      if palabra == valor:
        return i

  return -1

def Sanitize(xlsx_save_path):
  carpeta_xlsx = xlsx_save_path
  archivos_xlsx = [archivo for archivo in os.listdir(carpeta_xlsx) if archivo.endswith('.xlsx')]

  for archivo_xlsx in archivos_xlsx:
    ruta_completa_xlsx = os.path.join(carpeta_xlsx, archivo_xlsx)
    df = pd.read_excel( ruta_completa_xlsx )
    ruta_parcial = archivo_xlsx[:-5]

    #os.remove( ruta_completa_xlsx )

    palabras_clave = ['EQUIPO', 'MANO DE OBRA', 'MATERIALES', 'TRANSPORTE']
    palabras_clave2 = ['SUBTOTAL M', 'SUBTOTAL N', 'SUBTOTAL O', 'SUBTOTAL P']
    palabras_clave3 = ['PARCIAL M', 'PARCIAL N', 'PARCIAL O', 'PARCIAL P']

    for i in range(0, len(palabras_clave )):
      inicio = find_key( palabras_clave[i], df )
      final = find_key_last( palabras_clave2[i], df, inicio )
      if final == -1:
        final = find_key_last( palabras_clave3[i], df, inicio )
      nuevo_df = df.iloc[inicio:final + 1, :]
      nuevo_df.to_excel( ruta_parcial + f'_tab{i}.xlsx')
      #temp = os.path.join('/content/', ruta_parcial + f'_tab{i}.xlsx')
      #!cp {temp} {carpeta_xlsx}\

      #api mira esto aca y decide como quieres que guarde