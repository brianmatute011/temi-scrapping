import pandas as pd
import os
from temidb.connection import temidb_connection, mat_base

def find_col( data, key ):
    for i, row in data.iterrows():
        for column, value in row.items():
            value = str( value )
            if key in value:
                return column

def find_row( data, key ):
    for i, row in data.iterrows():
        for column, value in row.items():
            value = str( value )
            if key in value:
                return i

def app_first( route ):
  df = pd.read_excel( route )
  result = []

  for i in range( 0, 8 ):
    if i == 0:
      result.append( df[0][1] )
    if i == 4:
      result.append( df[0][3] )
    if i == 6:
      result.append( df[0][5] )
    if i == 7:
      result.append( df[0][7] )
    if i == 1 or i == 2 or i == 3 or i == 5:
      result.append( None )
      
  return result

def app_equip( route ):
  df = pd.read_excel( route )
  result = []

  return result

def app_mobra( route ):
  df = pd.read_excel( route )
  result = []

  return result

def app_mater( route ):
  df = pd.read_excel( route )
  result = []

  desc_col = find_col( df, "MATERIALES" )
  cant_col = find_col( df, "CANTIDAD" )
  first_ro = find_row( df, "MATERIALES" )
  last_row = find_row( df, "SUBTOTAL" )

  temidb = temidb_connection(host="localhost", user="root", password="", database="temidb")
  table_mat_base = mat_base(connection=temidb)

  for i, row in df.iterrows():
    if i == first_ro or i == last_row:
      continue
    
    for column, value in row.items():
      value = str( value )
      if desc_col == column:
        temp = table_mat_base.fetch_by_description( value )
        if temp is not None:
          result.append( temp[0] )
        else:
          result.append( None )
      if cant_col == column:
        result.append( value )

  return result

def app_trans( route ):
  df = pd.read_excel( route )
  result = []

  for i in range( 0, 80 ):
    result.append( 0 )

  return result

def function( source  ):
    keywords = ['FIRST','EQUIPO', 'MANO DE OBRA', 'MATERIALES', 'TRANSPORTE']
    xlsx_folder = source

    xlsx_files = [archivo for archivo in os.listdir(xlsx_folder) if archivo.endswith('.xlsx') and not archivo.endswith('s.xlsx')]

    line = []

    for xlsx_file in xlsx_files:
        for i in range(0, len(keywords ) ):
            route = os.path.join(xlsx_folder, f'{xlsx_file[:-5]}_tab{i}_s.xlsx' ) 
            
            if i == 0:
                line.append( app_first( route ) )
            if i == 1:
                line.append( app_equip( route ) )
            if i == 2:
                line.append( app_mobra( route ) )
            if i == 3:
                line.append( app_mater( route ) )
            if i == 4:
                line.append( app_trans( route ) )

    return line