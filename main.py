import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_page import Ui_MainWindow  # Import the UI class from the generated Python file

# Import the UI for the advanced page
from advanced import Ui_AdvancedPage

class AdvancedWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AdvancedWindow, self).__init__(parent)
        self.ui = Ui_AdvancedPage()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.back_to_main_window)

    def back_to_main_window(self):
        self.close()
        parent_window = self.parent()
        if parent_window:
            parent_window.show()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect the "Advanced" button to open the advanced page
        self.ui.pushButton_2.clicked.connect(self.open_advanced_page)

    def open_advanced_page(self):
        self.advanced_window = AdvancedWindow(parent=self)
        self.advanced_window.show()
        self.hide()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
