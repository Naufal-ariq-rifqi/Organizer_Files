from PyQt6.QtWidgets import QFileDialog
from Service.Scanner_File import ScannerService
from Service.Organize_File import OrganizerService


class FileController:

    def __init__(self, view):
        self.view = view

        self.scanner = ScannerService()
        self.organizer = OrganizerService()

        self.view.browseButton.clicked.connect(self.browse_folder)
        self.view.scanButton.clicked.connect(self.scan_folder)
        self.view.organizeButton.clicked.connect(self.organize_files)

    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self.view, "Pilih Folder")

        if folder:
            self.view.folderInput.setText(folder)

    def scan_folder(self):
        folder = self.view.folderInput.text().strip()

        if not folder:
            self.view.statusLabel.setText("Choose the folder first.")
            return

        try:
            self.view.progressBar.setValue(0)
            self.view.statusLabel.setText("Scanning...")

            result = self.scanner.scan(folder)

            self.view.totalFilesLabel.setText(
                f"Total Files : {result['total_files']}"
            )
            self.view.documentLabel.setText(
                f"Documents : {result['documents']}"
            )
            self.view.imageLabel.setText(
                f"Images : {result['images']}"
            )
            self.view.videoLabel.setText(
                f"Videos : {result['videos']}"
            )
            self.view.audioLabel.setText(
                f"Audio : {result['audio']}"
            )
            self.view.archiveLabel.setText(
                f"Archives : {result['archives']}"
            )
            self.view.otherLabel.setText(
                f"Others : {result['others']}"
            )

            self.view.progressBar.setValue(100)
            self.view.statusLabel.setText("Scan selesai.")

        except Exception as e:
            self.view.statusLabel.setText(f"Error: {e}")

    def organize_files(self):
        folder = self.view.folderInput.text().strip()

        if not folder:
            self.view.statusLabel.setText("Choose the folder first.")
            return

        try:
            self.view.progressBar.setValue(0)
            self.view.statusLabel.setText("Organizing files...")

            total = self.organizer.organize(folder)

            self.view.progressBar.setValue(100)
            self.view.statusLabel.setText(
                f"Successfully moved {total} files."
            )

        except Exception as e:
            self.view.statusLabel.setText(f"Error: {e}")