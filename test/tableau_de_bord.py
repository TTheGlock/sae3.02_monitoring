import sys
import psycopg2
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QVBoxLayout,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
)

class DashboardWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tableau de Bord - Informations Utilisateurs")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout()

        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(7)
        self.table_widget.setHorizontalHeaderLabels([
            "ID",
            "OS",
            "Version du système",
            "Hostname",
            "Adresse IP",
            "Charge CPU",
            "Charge mémoire",
            "Charge des disques"
        ])
        self.layout.addWidget(self.table_widget)
        self.setLayout(self.layout)

        self.populate_table()

    def populate_table(self):
        # Connexion à la base de données
        conn = psycopg2.connect(
            dbname='sae_database',
            user='sae',
            password='sae2023',
            host='localhost',
            port='5432'
        )
        cursor = conn.cursor()

        # Récupérer toutes les données de la table system_info
        cursor.execute('SELECT * FROM system_info')
        user_data = cursor.fetchall()

        cursor.close()
        conn.close()

        # Afficher les données dans le tableau
        self.table_widget.setRowCount(len(user_data))
        for row_num, row_data in enumerate(user_data):
            for col_num, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.table_widget.setItem(row_num, col_num, item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DashboardWidget()
    window.setGeometry(750,400,750,400)
    window.show()
    sys.exit(app.exec())
