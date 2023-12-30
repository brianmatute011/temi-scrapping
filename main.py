import sys, os, pickle, winreg, hashlib, socket
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QFileDialog, QMessageBox
from PyQt6.QtGui import QStandardItemModel
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl
from app.temi import Ui_MainWindow
from qtlibs.utilstemi import saved_token, get_tokenhash, read_binfile_from_tokenhash
from app.temi_dialog_lic import Ui_Form
from tlibs.pdf_scrapper_api import api_integration as apin
from tlibs import utilslibs as ul
from tlibs.temidb import connection as con





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
        count_page_avaibles = cli_service.remain()

        if not count_page_avaibles is None:
            self.ui.label.setText(f'Licencia aceptada: {count_page_avaibles} paginas disponibles.')
            self.ui.label.setStyleSheet("color: green")
            saved_token(license_text)
            window.update_serviceinfo()
            window.user_key = license_text
                    
            
        else:
            self.ui.label.setText("Licencia rechazada")
            self.ui.label.setStyleSheet("color: red")
            
                
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("temi-scrapped")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.user_key = None
        self.user_cpage_avaible = None
        self.updftable_count_from_doc = None
        self.user_pdft = None
        self.current_path_file = ""
        self.license_dialog = LicenseDialog()

        self.ui.actionOpen_file.triggered.connect(self.open_file_dialog)
        self.ui.actionSet_License.triggered.connect(self.open_license_dialog)
        self.ui.actionPurchase.triggered.connect(self.open_browser)
        self.ui.pushButton.clicked.connect(self.button_start)

        self.setup_layouts()
        self.update_serviceinfo()
    

    def button_start(self):
        self.ui.comboBox.setEnabled(True)
        
    
        if self.ui.comboBox.currentIndex() == 1:
            temidb = con.temidb_connection(host="localhost", user="root", password="", database="temidb")
            result_table = con.result(connection=temidb)
            parent_path = os.path.dirname(self.current_path_file)
            
            if parent_path == '':
                print(f'{parent_path} => parent_path')
                
                #Redirecting to the default document path
                default_documents_path = os.path.join(os.path.expanduser("~"), "Documents")

                excel_path = os.path.join(default_documents_path, "RESULT", "result.xlsx")
                if not os.path.exists(os.path.join(default_documents_path, "RESULT")):
                    os.makedirs(os.path.join(default_documents_path, "RESULT"))
                
                result_table.export_to_excel(excel_path)
            else:
                excel_path = os.path.join(parent_path, "RESULT", "result.xlsx")

                if not os.path.exists(os.path.join(parent_path, "RESULT")):
                    os.makedirs(os.path.join(parent_path, "RESULT"))
                    
                result_table.export_to_excel(excel_path)     

            QMessageBox.information(self, "Terminado", "Importacion Exitosa.")

        
        if self.ui.label_2.text().strip() == "No soportado" and self.ui.comboBox.currentIndex != 2:
            self.ui.comboBox.setEnabled(False)
            QMessageBox.warning(self, "Alerta", "Archivo no soportado.")
            return       
        
        print(f'{self.ui.comboBox.currentIndex()} -> {self.ui.comboBox.count()}: {self.current_path_file}')
        # Get user pdfptable instance from current key
        cli_service = self.user_pdft
        
        #Preprocess option comboBox enabled
        if self.ui.comboBox.currentIndex() == 0:
            cli_service.extract_pages(self.current_path_file)
            parent_path = os.path.dirname(self.current_path_file)
            cli_service.convert_pages_to_excel(f'{parent_path}/')
            recovery_list = ul.get_recovery_list(parent_path)
            print(f'recovery_list =>  {len(recovery_list)}')
            if recovery_list:
                temidb = con.temidb_connection(host="localhost", user="root", password="", database="temidb")
                result_table = con.result(connection=temidb)
                result_table.insert_result_from_recoverylist(recovery_list)
            QMessageBox.information(self, "Terminado", "Los Archivos fueron preprocesados.")

        
        #Upgrade service information
        self.update_serviceinfo()    



    def open_license_dialog(self):
        self.license_dialog.show()

    def open_file_dialog(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        if file_dialog.exec():
            base_file_names = file_dialog.selectedFiles()
            # file_name = os.path.splitext(os.path.basename(base_file_names[0]))[0]

            self.current_path_file = base_file_names[0]
            self.updftable_count_from_doc = apin.user_pdftables.count_page_document(self.current_path_file)
            self.ui.label.setText(f'Archivo seleccionado: {self.current_path_file}')
            self.ui.label_2.setText(f'Pag. del archivo: {self.updftable_count_from_doc}')
            
            if self.updftable_count_from_doc is None:
                self.ui.label_2.setText(f'No soportado')
                self.ui.label_2.setStyleSheet("color: red")
            elif self.updftable_count_from_doc > self.user_cpage_avaible:
                self.ui.label_2.setStyleSheet("color: red")
            else:
                self.ui.label_2.setStyleSheet("color: green")   

            print(f'Fselect: {base_file_names}   {self.updftable_count_from_doc}')
            
            # load_file_dialog(self, file_names[0])    

    def update_serviceinfo(self):
        token_hash = get_tokenhash()
        cpage_avaible = None
        if not token_hash is None:
            rbin_file =  read_binfile_from_tokenhash(token_hash)
            cpage_avaible = rbin_file[0]
            self.ui.label_3.setText(f'Paginas disponibles: {cpage_avaible}')

            if not cpage_avaible is None:
                if cpage_avaible <= (1000 * .10): 
                    self.ui.label_3.setStyleSheet("color: red")
                elif cpage_avaible <= (1000 * .30):
                    self.ui.label_3.setStyleSheet("color: yellow")
                else:
                    self.ui.label_3.setStyleSheet("color: green")
            else:
                return
            

        self.user_cpage_avaible = cpage_avaible
        self.user_key = rbin_file[1]
        print(f'User key:  {self.user_key}')
        self.user_pdft = apin.user_pdftables(self.user_key)                
    
    def open_browser(self):
        url = QUrl('https://pdftables.com/pricing#header')
        QDesktopServices.openUrl(url)
            



    def setup_layouts(self):
        central_widget = self.ui.centralwidget

        # Get the widgets from the generated file
        #scroll_area = self.ui.scrollArea
        push_button = self.ui.pushButton
        label = self.ui.label
        label_2 = self.ui.label_2
        label_3 = self.ui.label_3
        combo_box = self.ui.comboBox

        # Create layouts and establish them
        main_layout = QVBoxLayout(central_widget)
        bottom_buttons_layout = QHBoxLayout()
        top_labels = QHBoxLayout()

        main_layout.addLayout(top_labels)       
        #main_layout.addWidget(scroll_area)
        main_layout.addLayout(bottom_buttons_layout)
        
        bottom_buttons_layout.addWidget(push_button)

        top_labels.addWidget(label)
        top_labels.addWidget(label_2)
        top_labels.addWidget(label_3)
        top_labels.addWidget(combo_box)

       
               

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
