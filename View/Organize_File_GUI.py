from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QLineEdit, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout, QFileDialog, QProgressBar

# Only needed for access to command line arguments
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI File Organizer")
        self.resize(500, 300)

        # Widget utama
        central = QWidget()

        # Layout
        layout = QVBoxLayout()

        # Label
        self.titleLabel = QLabel("AI File Organizer")
        self.folderLabel = QLabel("Folder :")

        # Button
        self.scanButton = QPushButton("Scan Folder")
        self.organizeButton = QPushButton("Organize Files")
        self.browseButton = QPushButton("Browse")

        # Masukkan label ke layout
        layout.addWidget(self.titleLabel)
        layout.addSpacing(10)
        layout.addWidget(self.folderLabel)

        # layout browse Scaner folder dan Organize Files
        folder_layout = QHBoxLayout()
        self.folderInput = QLineEdit()
        self.folderInput.setPlaceholderText("Enter folder path...")
        folder_layout.addWidget(self.folderInput)
        folder_layout.addWidget(self.browseButton)
        layout.addLayout(folder_layout)
        layout.addSpacing(5)
        layout.addWidget(self.scanButton)
        layout.addWidget(self.organizeButton)

        # Layout Progress Bar dan Status
        progress_layout = QVBoxLayout()
        self.progressBar = QProgressBar()
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        self.statusLabel = QLabel("Status: Idle")
        progress_layout.addWidget(self.progressBar)
        progress_layout.addWidget(self.statusLabel)

        # file
        self.totalFilesLabel = QLabel("Total Files : 0")
        self.documentLabel = QLabel("Documents : 0")
        self.imageLabel = QLabel("Images : 0")
        self.videoLabel = QLabel("Videos : 0")
        self.audioLabel = QLabel("Audio : 0")
        self.archiveLabel = QLabel("Archives : 0")
        self.otherLabel = QLabel("Others : 0")

        # Agar semua widget tetap di atas
        layout.addLayout(progress_layout)
        layout.addSpacing(10)
        layout.addWidget(self.totalFilesLabel)
        layout.addWidget(self.documentLabel)
        layout.addWidget(self.imageLabel)
        layout.addWidget(self.videoLabel)
        layout.addWidget(self.audioLabel)
        layout.addWidget(self.archiveLabel)
        layout.addWidget(self.otherLabel)
        layout.addStretch()

        # Pasang layout ke widget utama
        central.setLayout(layout)

        # Jadikan widget utama sebagai central widget
        self.setCentralWidget(central)