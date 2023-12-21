import sys
import PyQt6.QtCore as Qt
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QVBoxLayout
)


class MainWindow(QApplication):
    def __init__(self):
        super().__init__(sys.argv)

        self.setWindowTitle("Alignement d'un label")
        self.setGeometry(100, 100, 500, 250)

        # Créez le label
        self.label = QLabel("Ce label est aligné à gauche")

        # Définissez l'alignement du label
        alignment = Qt.Alignment(Qt.AlignTop | Qt.AlignLeft)
        self.label.setAlignment(alignment)

        # Ajoutez le label à la fenêtre
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        self.show()


if __name__ == "__main__":
    app = MainWindow()
    app.exec()