import pandas as pd
import os
from autocorrect import Speller

# Function to find the first row containing the keyword
def find_key(word, data):
    for i, row in data.iterrows():
        for column, value in row.items():
            value = str(value)
            if word in value:
                return i

# Function to find the firs row containing the keyword from a given index
def find_key_last(word, data, index):
    for i, row in data.iloc[index:].iterrows():
        for column, value in row.items():
            value = str(value)
            if word == value:
                return i

# Function to perform spell checking on a string
def spell_check(string):
    spell = Speller(lang='es')
    string = str(string)
    return spell(string)

# Main function to process Excel files in a given folder
def sanitize(xlsx_save_path):
    try:
        xlsx_folder = xlsx_save_path
        # Get the list of .xlsx files in the folder
        xlsx_files = [file for file in os.listdir(xlsx_folder) if file.endswith('.xlsx') and not file.endswith('s.xlsx')]

        # Iterate over each .xlsx file
        for xlsx_file in xlsx_files:
            try:
                full_path_xlsx = os.path.join(xlsx_folder, xlsx_file)
                # Read the Excel file into a DataFrame
                df = pd.read_excel(full_path_xlsx)
                partial_path = xlsx_file[:-5]

                # Define lists of keywords
                keywords = ['EQUIPO', 'MANO DE OBRA', 'MATERIALES', 'TRANSPORTE']
                keywords2 = ['SUBTOTAL M', 'SUBTOTAL N', 'SUBTOTAL O', 'SUBTOTAL P']
                keywords3 = ['PARCIAL M', 'PARCIAL N', 'PARCIAL O', 'PARCIAL P']

                # Iterate over each set of keywords
                for i in range(0, len(keywords)):
                    # Find the start and end positions of the keywords
                    start = find_key(keywords[i], df)
                    end = find_key_last(keywords2[i], df, start)
                    
                    # Check if both keys were found
                    if start is not None and end is not None:
                        # Select a subset of data
                        new_df = df.iloc[start:end + 1, :]
                        # Apply spell checking to the subset of data
                        spell_df = new_df.applymap(spell_check)
                        # Save the subset of data to a new Excel file
                        spell_df.to_excel(partial_path + f'_tab{i}_s.xlsx')
                    else:
                        # Print a message if both keys are not found
                        print(f"No keys found for {keywords[i]} in {xlsx_file}")
            except Exception as e:
                # Handle errors when processing individual files
                print(f"Error processing file {xlsx_file}: {str(e)}")

    except Exception as e:
        # Handle general errors
        print(f"General error: {str(e)}")
