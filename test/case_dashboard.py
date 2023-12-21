import sys
import psycopg2
from graph_test import graph
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

        # Créez le label qui affichera les informations
        self.info_label = QLabel("")
        self.info_label.setStyleSheet("border: 1px solid black;")

        # Créez le bouton de recherche
        self.search_button = QPushButton("Rechercher")

        # Connectez le bouton de recherche à la fonction update_result_label()
        self.search_button.clicked.connect(self.update_result_label)

        # Créez les labels qui afficheront les résultats
        self.info_label = QLabel("")
        self.info_label.setStyleSheet("border: 1px solid black;")

        self.cpu_label = QLabel("")
        self.cpu_label.setStyleSheet("border: 1px solid black;")

        self.memory_label = QLabel("")
        self.memory_label.setStyleSheet("border: 1px solid black;")

        self.disk_label = QLabel("")
        self.disk_label.setStyleSheet("border: 1px solid black;")

        # Créez le layout grille
        self.grid_layout = QGridLayout()

        # Ajoutez les widgets d'informations
        self.grid_layout.addWidget(self.info_label, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.cpu_label, 0, 1, 1, 1)

        # Ajoutez les widgets graphiques
        self.grid_layout.addWidget(self.disk_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.memory_label, 1, 1, 1, 1)

        # Ajoutez le champ d'entrée d'adresse IP à l'agencement principal
        self.layout.addWidget(self.ip_input)

        # Ajoutez le bouton de recherche à l'agencement principal
        self.layout.addWidget(self.search_button)

        #Ajoutez le layout grille au layout principal
        self.layout.addLayout(self.grid_layout, 0)

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


        # Requête pour récupérer les 10 derniers cpu_charge, ram_charge et disk_charge de l'adresse IP '192.168.1.39'
        query2 = """
            SELECT cpu_charge, ram_charge, disk_charge
            FROM machines
            WHERE ip_addr = '%s'
            LIMIT 10
        """

        # Exécute la requête et récupère les résultats
        cursor.execute(query2)
        results = cursor.fetchall()

        # Convertit les charges en chiffres
        cpu_charge = []
        ram_charge = []
        disk_charge = []
        for result in results:
            cpu_charge.append(int(result[0]))
            ram_charge.append(int(result[1]))
            disk_charge.append(int(result[2]))


        # Créez les graphiques
        #cpu_graph = graph.graph.create_line_graph(cpu_charge)
        #ram_graph = graph.graph.create_line_graph(ram_charge)
        #disk_graph = graph.graph.create_line_graph(disk_charge)

        cursor.close()
        conn.close()

        if user_info:
            # Mettez à jour les informations affichées dans les labels des résultats
            info = f"Nom : {user_info[4]}\nSystème : {user_info[2]} \nVersion : {user_info[3]} \nIP : {user_info[1]}"
            self.info_label.setText(info)
            
            # Afficher les graphiques
            #self.cpu_label.setPixmap(cpu_graph)
            #self.memory_label.setPixmap(ram_graph)
            #self.disk_label.setPixmap(disk_graph)
        
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
