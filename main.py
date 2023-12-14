import sys, os, pickle, winreg, hashlib, socket
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QStandardItemModel
from app.temi import Ui_MainWindow
from qtlibs.utilstemi import open_file_dialog, saved_token, get_tokenhash, read_binfile_from_tokenhash
from app.temi_dialog_lic import Ui_Form
from tlibs.pdf_scrapper_api import api_integration as apin


class LicenseDialog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.setWindowTitle("temi license")
        self.ui.setupUi(self) 
        

        self.ui.pushButton.clicked.connect(self.process_license)

    def process_license(self):
        
        try:
            socket.create_connection(("www.google.com", 80))
        except OSError:
            self.ui.label.setText("Error de conexión a Internet")
            self.ui.label.setStyleSheet("color: red")
            return

        license_text = self.ui.lineEdit.text().strip()
        cli_service = apin.user_pdftables(license_text)
        count_page_avaibles =  cli_service.remain()

        if not count_page_avaibles is None:
            self.ui.label.setText(f'Licencia aceptada: {count_page_avaibles} paginas disponibles.')
            self.ui.label.setStyleSheet("color: green")
            saved_token(license_text)
            window.update_serviceinfo()
                    
            
        else:
            self.ui.label.setText("Licencia rechazada")
            self.ui.label.setStyleSheet("color: red")
            
                
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("temi-scrapped")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.user_key = get_tokenhash()
        self.license_dialog = LicenseDialog()

        self.ui.actionOpen_file.triggered.connect(open_file_dialog)
        self.ui.actionSet_License.triggered.connect(self.license_dialog.show)

        self.setup_layouts()
        self.update_serviceinfo()

    def update_serviceinfo(self):
        token_hash = get_tokenhash()
        if not token_hash is None:
            cpage_avaible = read_binfile_from_tokenhash(token_hash) 
            self.ui.label_3.setText(f'Paginas disponibles: {cpage_avaible}')
            self.ui.label_3.setStyleSheet("color: green")



    def setup_layouts(self):
        central_widget = self.ui.centralwidget

        # Get the widgets from the generated file
        scroll_area = self.ui.scrollArea
        push_button = self.ui.pushButton
        push_button_2 = self.ui.pushButton_2
        label = self.ui.label
        label_2 = self.ui.label_2
        label_3 = self.ui.label_3


        # Create layouts and establish them
        main_layout = QVBoxLayout(central_widget)
        bottom_buttons_layout = QHBoxLayout()
        top_labels = QHBoxLayout()

        main_layout.addLayout(top_labels)       
        main_layout.addWidget(scroll_area)
        main_layout.addLayout(bottom_buttons_layout)
        

        bottom_buttons_layout.addWidget(push_button)
        bottom_buttons_layout.addWidget(push_button_2)

        top_labels.addWidget(label)
        top_labels.addWidget(label_2)
        top_labels.addWidget(label_3)

       
               

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
