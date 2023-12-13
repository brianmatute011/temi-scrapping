from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import  QStandardItem, QStandardItemModel


def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        if file_dialog.exec():
            file_names = file_dialog.selectedFiles()
            print(f'Fselect: {file_names[0]}')
            # load_file_dialog(self, file_names[0])

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