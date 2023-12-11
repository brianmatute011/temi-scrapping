from PyQt6 import QtWidgets

def open_file_dialog(self):
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFile)
        if file_dialog.exec():
            file_names = file_dialog.selectedFiles()
            # Process file... 
            print("Select file:", file_names[0])