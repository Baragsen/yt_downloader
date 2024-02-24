import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from main_page import Ui_MainWindow  
import yt_downloader

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

        self.ui.pushButton.clicked.connect(self.start_download)

    def open_advanced_page(self):
        self.advanced_window = AdvancedWindow(parent=self)
        self.advanced_window.show()
        self.hide()

    def start_download(self):
        try:
            url = self.ui.lineEdit.text()
            yt_downloader.vid_download(url)
            self.ui.progressBar.setValue(progress=yt_downloader.down_prog())
        except Exception as e:
            print(e)




def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
