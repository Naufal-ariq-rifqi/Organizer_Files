import sys
from PyQt6.QtWidgets import QApplication

from View.Organize_File_GUI import MainWindow
from Controller.Organize_File_Controller import FileController

app = QApplication(sys.argv)

view = MainWindow()
controller = FileController(view)

view.show()

app.exec()