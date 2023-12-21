import sys
import psycopg2
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QGridLayout,
)


class UserInfoWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Recherche d'informations par adresse IP")
        self.setGeometry(100, 100, 500, 250)

        # Créez la structure d'affichage
        self.layout = QVBoxLayout()

        # Créez le champ d'entrée d'adresse IP
        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("Entrez l'adresse IP")

        # Créez le bouton de recherche
        self.search_button = QPushButton("Rechercher")

        # Connectez le bouton de recherche à la fonction update_result_label()
        self.search_button.clicked.connect(self.update_result_label)

        # Créez les labels qui afficheront les résultats
        self.name_label = QLabel("")
        self.name_label.setStyleSheet("border: 1px solid black;")
        self.name_label.setAlignment(Qt.AlignLeft)
        self.os_label = QLabel("")
        self.os_label.setStyleSheet("border: 1px solid black;")
        self.os_label.setAlignment(Qt.AlignCenter)
        self.cpu_label = QLabel("")
        self.cpu_label.setStyleSheet("border: 1px solid black;")
        self.cpu_label.setAlignment(Qt.AlignCenter)
        self.memory_label = QLabel("")
        self.memory_label.setStyleSheet("border: 1px solid black;")
        self.memory_label.setAlignment(Qt.AlignCenter)

        # Créez le layout grille
        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.name_label, 0, 0)
        self.grid_layout.addWidget(self.os_label, 1, 0, 1, 2)
        self.grid_layout.addWidget(self.cpu_label, 2, 0)
        self.grid_layout.addWidget(self.memory_label, 3, 0)

        # Alignez les cases pour former un carré
        # Il n'y a pas besoin de la méthode setAlignment() ici car nous avons positionné les labels manuellement

        # Ajoutez le champ d'entrée d'adresse IP à l'agencement principal
        self.layout.addWidget(self.ip_input)

        # Ajoutez le bouton de recherche à l'agencement principal
        self.layout.addWidget(self.search_button)

        # Ajoutez le layout grille à l'agencement principal
        self.layout.addLayout(self.grid_layout)

        # Set the layout as the main layout
        self.setLayout(self.layout)

    def update_result_label(self):
        # Récupérez les informations de la base de données
        ip_address = self.ip_input.text()

        # Connexion à la base de données
        conn = psycopg2.connect(
            dbname="sae302_monitoring",
            user="application",
            password="gtrnet",
            host="localhost",
            port="5432"
        )
        cursor = conn.cursor()

        # Requête pour récupérer les informations de la machine en fonction de son adresse IP
        query = """
            SELECT *
            FROM machines
            WHERE ip_addr = %s
            LIMIT 10
        """
        cursor.execute(query, (ip_address,))
        user_info = cursor.fetchone()

        cursor.close()
        conn.close()

        if user_info:
            # Mettez à jour les informations affichées dans les labels des résultats
            info = f"Nom : {user_info[2]} \nSystème : {user_info[3]}"
            self.info_label.setText(info)
            self.cpu_label.setText(f"Processeur : {user_info[5]}%")
            self.memory_label.setText(f"Mémoire : {user_info[6]}%")
            self.disk_label.setText(f"Disque : {user_info[7]}%")
        else:
            # Affiche un message si aucune information n'est trouvée
            self.info_label.setText("Aucune information trouvée")
            self.cpu_label.setText("")
            self.memory_label.setText("")
            self.disk_label.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserInfoWidget()
    window.show()
    sys.exit(app.exec())
