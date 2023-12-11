import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from app.temi import Ui_MainWindow
from qtlibs.utilstemi import open_file_dialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionOpen_file.triggered.connect(open_file_dialog)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
