from PySide6.QtWidgets import QApplication, QMainWindow
# some imports missing
from PySide6.QtGui import QAction
from PySide6.QtCore import Slot
import sys

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        # some code missing
        self.show()

    # slots missing

q_app = QApplication(sys.argv)
gui = GUI()
q_app.exec()

# -------------------------------------------------------------
def confirm(self):
    """
    Confirms quitting from user

    Returns:
    True if user confirms quitting
    False otherwise
    """
    dialog = QMessageBox(self)
    dialog.setWindowTitle('Confirm')
    dialog.setText('Really exit?')
    dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    dialog.setIcon(QMessageBox.Question)
    button = dialog.exec()

    return button == QMessageBox.Yes

from PySide6.QtWidgets import QApplication, QMainWindow
# some imports missing
from PySide6.QtGui import QAction
from PySide6.QtCore import Slot
import sys

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        # some code missing
        self.show()

    # slots missing

q_app = QApplication(sys.argv)
gui = GUI()
q_app.exec()
