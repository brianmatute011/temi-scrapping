import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QStandardItemModel
from app.temi import Ui_MainWindow
from qtlibs.utilstemi import open_file_dialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionOpen_file.triggered.connect(open_file_dialog)

        self.setup_layouts()
        
    def setup_layouts(self):
        central_widget = self.ui.centralwidget

        # Get the widgets from the generated file
        scroll_area = self.ui.scrollArea
        push_button = self.ui.pushButton
        push_button_2 = self.ui.pushButton_2
        label = self.ui.label
        label_2 = self.ui.label_2

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
               

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
