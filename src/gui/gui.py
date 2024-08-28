import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from src.cleaner.cleaner import start_cleaning_process

class DirProxyModel(QtCore.QSortFilterProxyModel):
    def __init__(self, fsModel):
        super().__init__()
        self.fsModel = fsModel
        self.setSourceModel(fsModel)

    def lessThan(self, left, right):
        leftIsDir = self.fsModel.fileInfo(left).isDir()
        if leftIsDir != self.fsModel.fileInfo(right).isDir():
            return leftIsDir
        return super().lessThan(left, right)

    def flags(self, index):
        flags = super().flags(index)
        if not self.fsModel.fileInfo(self.mapToSource(index)).isDir():
            flags &= ~QtCore.Qt.ItemIsEnabled
        return flags

class CleaningThread(QtCore.QThread):
    progress = QtCore.pyqtSignal(int)
    status = QtCore.pyqtSignal(str)

    def __init__(self, game_directory, backup_directory):
        super().__init__()
        self.game_directory = game_directory
        self.backup_directory = backup_directory

    def run(self):
        try:
            self.status.emit("In-Progress")
            start_cleaning_process(self.game_directory, self.backup_directory, self)
            self.status.emit("Completed")
        except Exception as e:
            self.status.emit("Error")
            print(f"Error during cleaning process: {e}")

    def setValue(self, value):
        self.progress.emit(value)

    def update(self):
        pass

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CarX Cleaner")
        self.setGeometry(100, 100, 600, 500)
        self.setWindowIcon(QIcon("src/gui/icon/carx_cleaner_icon.png"))
        self.setStyleSheet("""
            background-color: #2e2e2e; 
            color: #ffffff;
            font-family: Arial, sans-serif;
        """)

        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.layout.setAlignment(QtCore.Qt.AlignCenter)

        self.label = QtWidgets.QLabel("Input CarX Directory Path:")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("""
            color: #ffffff; 
            padding: 10px; 
            font-size: 16px;
        """)
        self.layout.addWidget(self.label)

        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setStyleSheet("""
            background-color: #3e3e3e; 
            color: #ffffff; 
            padding: 10px; 
            border-radius: 5px;
            font-size: 14px;
        """)
        self.layout.addWidget(self.lineEdit)

        self.backup_label = QtWidgets.QLabel("Input Backup Directory Path:")
        self.backup_label.setAlignment(QtCore.Qt.AlignCenter)
        self.backup_label.setStyleSheet("""
            color: #ffffff; 
            padding: 10px; 
            font-size: 16px;
        """)
        self.layout.addWidget(self.backup_label)

        self.backup_lineEdit = QtWidgets.QLineEdit()
        self.backup_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.backup_lineEdit.setStyleSheet("""
            background-color: #3e3e3e; 
            color: #ffffff; 
            padding: 10px; 
            border-radius: 5px;
            font-size: 14px;
        """)
        self.layout.addWidget(self.backup_lineEdit)

        self.clean_button = QtWidgets.QPushButton("Start Cleaning", self)
        self.clean_button.setStyleSheet("""
            background-color: #5e5e5e; 
            color: #ffffff; 
            padding: 10px; 
            border-radius: 5px;
            font-size: 14px;
            margin-top: 10px;
        """)
        self.clean_button.clicked.connect(self.start_cleaning)
        self.layout.addWidget(self.clean_button)

        self.progress_bar = QtWidgets.QProgressBar(self)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                background-color: #3e3e3e; 
                color: #ffffff; 
                border: 1px solid #5e5e5e; 
                padding: 5px; 
                text-align: center;
                border-radius: 5px;
            } 
            QProgressBar::chunk {
                background-color: #5e5e5e;
                border-radius: 5px;
            }
        """)
        self.progress_bar.setValue(0)
        self.layout.addWidget(self.progress_bar)

        self.status_label = QtWidgets.QLabel("Ready")
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setStyleSheet("""
            color: #ffffff; 
            padding: 10px; 
            font-size: 14px;
        """)
        self.layout.addWidget(self.status_label)

    def start_cleaning(self):
        game_directory = self.lineEdit.text()
        backup_directory = self.backup_lineEdit.text()
        if game_directory and backup_directory:
            self.clean_button.setEnabled(False)
            self.progress_bar.setValue(0)
            self.status_label.setText("In-Progress")

            self.cleaning_thread = CleaningThread(game_directory, backup_directory)
            self.cleaning_thread.progress.connect(self.progress_bar.setValue)
            self.cleaning_thread.status.connect(self.update_status)
            self.cleaning_thread.finished.connect(self.cleaning_finished)
            self.cleaning_thread.start()

    def update_status(self, status):
        self.status_label.setText(status)

    def cleaning_finished(self):
        self.clean_button.setEnabled(True)
        self.progress_bar.setValue(0)

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
