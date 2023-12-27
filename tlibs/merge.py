import pandas as pd
import os
from temidb.connection import temidb_connection, mat_base, equipment_base, salary_base_dollars

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

  desc_col = find_col( df, "EQUIPO" )
  cant_col = find_col( df, "CANTIDAD" )
  first_ro = find_row( df, "EQUIPO" )
  last_row = find_row( df, "SUBTOTAL" )

  temidb = temidb_connection(host="localhost", user="root", password="", database="temidb")
  equipment_mat_base = equipment_base(connection=temidb)

  for i, row in df.iterrows():
    if i == first_ro or i == last_row:
      continue
    
    for column, value in row.items():
      value = str( value )
      if desc_col == column:
        temp = equipment_mat_base.fetch_by_description( value )
        if temp:
          first_element, *_ = temp
          result.append( first_element )
        else:
          result.append( None )
      if cant_col == column:
        result.append( value )

  for i in range( len(result), 40 ):
    result.append( None )

  return result

def app_mobra( route ):
  df = pd.read_excel( route )
  result = []

  desc_col = find_col( df, "MANO DE OBRA" )
  cant_col = find_col( df, "CANTIDAD" )
  first_ro = find_row( df, "MANO DE OBRA" )
  last_row = find_row( df, "SUBTOTAL" )

  temidb = temidb_connection(host="localhost", user="root", password="", database="temidb")
  salary_base = salary_base_dollars(connection=temidb)

  for i, row in df.iterrows():
    if i == first_ro or i == last_row:
      continue
    
    for column, value in row.items():
      value = str( value )
      if desc_col == column:
        temp = salary_base.fetch_by_worker_category( value )
        if temp:
          first_element, *_ = temp
          result.append( first_element )
        else:
          result.append( None )
      if cant_col == column:
        result.append( value )
  
  for i in range( len(result), 40 ):
    result.append( None )

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
          if temp:
            first_element, *_ = temp
            result.append( first_element )
          else:
            result.append( None )
      if cant_col == column:
        result.append( value )

  for i in range( len(result), 40 ):
    result.append( None )

  return result

def app_trans( route ):
  df = pd.read_excel( route )
  result = []

  for i in range( 0, 80 ):
    result.append( 0 )

  return result

def merge( source_path, xlsx_file  ):
    keywords = ['FIRST','EQUIPO', 'MANO DE OBRA', 'MATERIALES', 'TRANSPORTE']
    # 'C:/Users/Brian/Documents/GitHub/temi-scrapping/tlibs/temp/APUS lite_page_1.xlsx'
    
    global_list = []
    for i in range(0, len(keywords ) ):
        route = os.path.join(source_path, f'{xlsx_file[:-5]}_tab{i}_s.xlsx' ) 
        
        if i == 0:
            global_list = global_list + app_first( route )
        if i == 1:
            global_list = global_list + app_equip( route ) 
        if i == 2:
            global_list = global_list + app_mobra( route )
        if i == 3:
            global_list = global_list + app_mater( route )
        if i == 4:
            global_list = global_list + app_trans( route )

    return global_list