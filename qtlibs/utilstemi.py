from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import  QStandardItem, QStandardItemModel
from tlibs.pdf_scrapper_api import api_integration as apin

import os, pickle, hashlib, winreg



def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        if file_dialog.exec():
            file_names = file_dialog.selectedFiles()
            print(f'Fselect: {file_names[0]}')
            # load_file_dialog(self, file_names[0])
            

def saved_token(lt: str):
        
        token_directory = "./lic"
        if not os.path.exists(token_directory):
            os.makedirs(token_directory, exist_ok=True)
        
        # Encode token to hash    
        hashed_key = hashlib.sha256(lt.encode()).hexdigest()
        
        # Save namefile as encode token 
        token_path = os.path.join(token_directory, f'{hashed_key}')
        with open(token_path, 'wb') as file:
            pickle.dump(lt, file)
        
        key_name = "Software\\Alphax\\TemiScrapper"
        value_name = hashed_key

        # Validate if exist reg value
        try:
            with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_name) as key:
                print("Clave creada en el registro.")
        except OSError as e:
            print(f"Error al acceder al registro: {e}")  
                     
        # Write on Windows Reg
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_name, 0, winreg.KEY_WRITE) as key:
                winreg.SetValueEx(key, "token", 0, winreg.REG_SZ, hashed_key)
                print("Clave guardada en el registro.")
        except OSError as e:
            print(f"Error al acceder al registro: {e}")    

def get_tokenhash():
    key_name = "Software\\Alphax\\TemiScrapper"

    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_name, 0, winreg.KEY_READ) as key:
            value, _ = winreg.QueryValueEx(key, "token")
            print(f"Valor del registro: {value}")
            return value
        
    except OSError as e:
        print(f"Error al acceder al registro: {e}")
        return None

def read_binfile_from_tokenhash(tk_hash: str, bin_path = './lic'):
     
    try:
        if os.path.exists(bin_path):
            file_path = os.path.join(bin_path, f"{tk_hash}")
            license_text = ""

            try:
                with open(file_path, 'rb') as file:
                    try:
                        license_text = pickle.load(file)
                        print(f"Contenido del archivo binario: {license_text}")
                        # window.user_key = license_text
                        temp_cli = apin.user_pdftables(license_text)
                    except (pickle.UnpicklingError, EOFError) as e:
                        print(f"Error al cargar el archivo binario: {e}")
        
            except FileNotFoundError:
                print("El archivo binario no existe.")
        
        else:
            print("El directorio no existe.")

    except OSError as e:
        print(f"Error de sistema: {e}")
    
    return [temp_cli.remain(), license_text]    
               





# def load_file_dialog(self, path: str):
#         # Verificar si el modelo está inicializado correctamente
#         if self.model is None:
#             self.model = QStandardItemModel()
#             print("Pass None")

#         # Limpiar el modelo antes de cargar nuevos datos
#         self.model.clear()
#         print("Pass Out")
#         # Agregar la información del archivo al modelo
#         row_item = QStandardItem(str(path))
#         self.model.appendRow(row_item)