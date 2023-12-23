import pandas as pd
import os
from autocorrect import Speller
from collections import Counter

# Define the function to handle exceptions
def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")
    return wrappe

# Define the spell check function 
@handle_exceptions
def spell_check(string):
    spell = Speller(lang='es')
    string = str(string)
    return spell(string)

# Define the find_key function to find the first occurrence of a keyword
@handle_exceptions
def find_key(palabra, datos):
    for i, fila in datos.iterrows():
        for columna, valor in fila.items():
            valor = str(valor)
            if palabra in valor:
                return i

# Define the find_key_last function to find the last occurrence of a keyword after a given index
@handle_exceptions
def find_key_last(palabra, datos, indice):
    for i, fila in datos.iloc[indice:].iterrows():
        for columna, valor in fila.items():
            valor = str(valor)
            if palabra == valor:
                return i

# Define the look_row function to find a row containing a specified key
@handle_exceptions
def look_row(data, key):
    for i, row in data.iterrows():
        for col, value in row.items():
            value = str(value)
            if key == value and key == 'RUBRO :':
                return row
            if key in value:
                return row

# Define the extract_rubro_col function to extract the column index for 'RUBRO :'
@handle_exceptions
def extract_rubro_col(data, key):
    for i in range(len(data)):
        if str(data[i]) in key and key == 'RUBRO :':
            return i + 1

# Define the extract_detalles_col function to extract the column index for 'DETALLE :'
@handle_exceptions
def extract_detalles_col(data, key):
    for i in range(len(data)):
        if str(data[i]) in key and key == 'DETALLE :':
            return i + 1

# Define the extract_unit_rendimiento_col function to extract the column index for unit of 'RENDIMIENTO'
@handle_exceptions
def extract_unit_rendimiento_col(data, key):
    for i in range(len(data)):
        if key in str(data[i]):
            return i

# Define the extract_unit_value function to extract the unit from the data
@handle_exceptions
def extract_unit_value(data, key):
    units = [' km', ' m', ' m2', ' m3', ' kg', ' ml', ' u', ' pt', ' pto', ' glb', ' un', ' cm', ' cm2', ' cm3', ' plancha', ' m3*km']

    value = str(data)
    value = value.lower()

    for j in range(len(units)):
        if units[j] in value:
            return units[j]

# Define the extract_rendimiento function to extract the most common element from the numerical data
@handle_exceptions
def extract_rendimiento(data, k):
    numbers_only = [x for x in data if isinstance(x, (int, float))]
    counter = Counter(numbers_only)
    most_common_element, count = counter.most_common(1)[0]

    return most_common_element

# Define the first_data function to extract specific data from a DataFrame
@handle_exceptions
def first_data(data):
    # Define key and save_format lists
    key = ['RUBRO :', 'DETALLE :', 'UNIDAD', 'RENDIMIENTO']
    save_format = ['COD', 'CONCEPTO', 'UNIDAD', 'RENDIMIENTO']
    result = []

    # Iterate over the key and save_format lists
    for i in range(0, len(key)):
        result.append(save_format[i])
        # Extract the row that has the data from that key
        row = look_row(data, key[i])

        # Check if the row is not None
        if row is not None:
            if i == 0:
                # Find the Rubro Number
                temp = str(row[extract_rubro_col(row, key[i])])
                result.append(temp)
            if i == 1:
                # Find the Rubro Name or Detalle 
                temp = str(row[extract_detalles_col(row, key[i])])
                result.append(temp)
            if i == 2:
                # Find tha Unit 
                temp = str(row[extract_unit_rendimiento_col(row, key[i])])
                temp = extract_unit_value(temp, key[i])
                result.append(temp)
            if i == 3:
                # Find the Rendimiento
                index = find_key(key[i], data)
                col_index = extract_unit_rendimiento_col(row, key[i])
                col = data.iloc[index:index + 10, col_index]
                result.append(extract_rendimiento(col, key[i]))
        else:
            result.append(None)

    return result

# Define the main function with exception handling
@handle_exceptions
def Sanitize(xlsx_save_path):
    try:
        folder_xlsx = xlsx_save_path

        # Filter Excel files in the specified folder
        xlsx_files = [file for file in os.listdir(folder_xlsx) if file.endswith('.xlsx') and not file.endswith('s.xlsx')]

        for xlsx_file in xlsx_files:
            full_path_xlsx = os.path.join(folder_xlsx, xlsx_file)

            try:
                # Read Excel file into a DataFrame
                df = pd.read_excel(full_path_xlsx)
                partial_path = xlsx_file[:-5]

                # Uncomment the line below to remove the original xlsx file
                # os.remove(full_path_xlsx)

                # Keyword lists for different sections
                keyword_list = ['None', 'EQUIPO', 'MANO DE OBRA', 'MATERIALES', 'TRANSPORTE']
                keyword_list2 = ['None', 'SUBTOTAL M', 'SUBTOTAL N', 'SUBTOTAL O', 'SUBTOTAL P']
                keyword_list3 = ['None', 'PARCIAL M', 'PARCIAL N', 'PARCIAL O', 'PARCIAL P']

                for i in range(len(keyword_list)):
                    sanitized_file_path = os.path.join(folder_xlsx, f"{partial_path}_tab{i}_s.xlsx")

                    if not os.path.exists(sanitized_file_path):
                        if i == 0:
                            # Create a new Excel file with the first row of the DataFrame
                            tmp_df = pd.DataFrame(first_data(df))
                            tmp_df.to_excel(sanitized_file_path)
                        else:
                            # Extract a section based on keywords and perform spell check
                            start = find_key(keyword_list[i], df)
                            end = find_key_last(keyword_list2[i], df, start)
                            if end is None:
                                end = find_key_last(keyword_list3[i], df, start)
                            new_df = df.iloc[start:end + 1, :]
                            new_df.to_excel(sanitized_file_path)
                            
                            #spell_df = new_df.applymap(spell_check)

                            # Save the sanitized DataFrame to a new Excel file
                            #spell_df.to_excel(sanitized_file_path)

            except Exception as inner_exception:
                print(f"An error occurred while processing file {xlsx_file}: {inner_exception}")

    except Exception as outer_exception:
        print(f"An error occurred in the main loop: {outer_exception}")