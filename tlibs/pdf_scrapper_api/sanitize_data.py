import pandas as pd
import os
from autocorrect import Speller

def find_key(word, data):
    for i, row in data.iterrows():
        for column, value in row.items():
            value = str(value)
            if word in value:
                return i

def find_key_last(word, data, index):
    for i, row in data.iloc[index:].iterrows():
        for column, value in row.items():
            value = str(value)
            if word == value:
                return i

def spell_check(string):
    spell = Speller(lang='es')
    string = str(string)
    return spell(string)

def sanitize(xlsx_save_path):
    try:
        xlsx_folder = xlsx_save_path
        xlsx_files = [file for file in os.listdir(xlsx_folder) if file.endswith('.xlsx') and not file.endswith('s.xlsx')]

        for xlsx_file in xlsx_files:
            try:
                full_path_xlsx = os.path.join(xlsx_folder, xlsx_file)
                df = pd.read_excel(full_path_xlsx)
                partial_path = xlsx_file[:-5]

                keywords = ['EQUIPO', 'MANO DE OBRA', 'MATERIALES', 'TRANSPORTE']
                keywords2 = ['SUBTOTAL M', 'SUBTOTAL N', 'SUBTOTAL O', 'SUBTOTAL P']
                keywords3 = ['PARCIAL M', 'PARCIAL N', 'PARCIAL O', 'PARCIAL P']

                for i in range(0, len(keywords)):
                    start = find_key(keywords[i], df)
                    end = find_key_last(keywords2[i], df, start)
                    if start is not None and end is not None:
                        new_df = df.iloc[start:end + 1, :]
                        spell_df = new_df.applymap(spell_check)
                        spell_df.to_excel(partial_path + f'_tab{i}_s.xlsx')
                        #temp = os.path.join('/content/', partial_path + f'_tab{i}.xlsx')
                        #!cp {temp} {xlsx_folder}
                        #api look at this and decide how you want it to save
                    else:
                        print(f"No keys found for {keywords[i]} in {xlsx_file}")
            except Exception as e:
                print(f"Error processing file {xlsx_file}: {str(e)}")

    except Exception as e:
        print(f"General error: {str(e)}")
