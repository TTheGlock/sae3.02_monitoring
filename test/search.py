import sys
import psycopg2
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
)

class UserInfoWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Recherche d'informations par adresse IP")
        self.setGeometry(100, 100, 500, 250)

        self.layout = QVBoxLayout()

        self.label = QLabel("Entrez l'adresse IP de l'utilisateur :")
        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("Entrez l'adresse IP")
        self.search_button = QPushButton("Rechercher")
        self.search_button.setStyleSheet(
            "QPushButton { background-color: #4CAF50; color: white; font-weight: bold; border-radius: 5px; padding: 8px 10px; }"
            "QPushButton:hover { background-color: #45a049; }"
            "QPushButton:pressed { background-color: #379e3c; }"
        )
        self.search_button.clicked.connect(self.search_user)

        self.result_label = QLabel()
        self.result_label.setStyleSheet(
            "QLabel { background-color: #f0f0f0; border-radius: 5px; padding: 10px; font-size: 14px; }"
        )

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.label)
        input_layout.addWidget(self.ip_input)
        input_layout.addWidget(self.search_button)

        self.layout.addLayout(input_layout)
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

    def search_user(self):
        ip_address = self.ip_input.text()  # Récupère l'adresse IP du champ de saisie

        # Connexion à la base de données
        conn = psycopg2.connect(
        dbname='sae302_monitoring',
        user='application',
        password='gtrnet',
        host='localhost',
        port='5432'
        )  # Établit une connexion à la base de données PostgreSQL
        cursor = conn.cursor()  # Crée un objet curseur pour exécuter des requêtes SQL

        # Requête pour récupérer les informations de l'utilisateur en fonction de son adresse IP
        query = """
            SELECT * FROM machines
            WHERE ip_addr = %s
        """  # Définit la requête SQL pour récupérer les données de la table 'machines'
        cursor.execute(query, (ip_address,))  # Exécute la requête, en passant l'adresse IP en tant que paramètre
        user_info = cursor.fetchall()  # Récupère toutes les lignes de la base de données qui correspondent à l'adresse IP

        cursor.close()  # Ferme l'objet curseur
        conn.close()  # Ferme la connexion à la base de données

        if user_info:
            # Format the table rows and generate the result text
            result_text = f"""
                <h3>Informations sur l'utilisateur</h3>
                <table border="1" cellpadding="5" cellspacing="0">
                    <tr>
                        <th>Adresse IP</th>
                        <th>Hostname</th>
                        <th>Système</th>
                        <th>CPU</th>
                        <th>Mémoire</th>
                        <th>Disque</th>
                    </tr>
                    {self._generate_table_rows(user_info)}
                </table>
            """
        else:
            result_text = "Aucune information trouvée pour cette adresse IP."

        self.result_label.setText(result_text)

    def _generate_table_rows(self, user_info):
        rows = []
        for row in user_info:
            rows.append(f"<tr><td>{row[3]}</td><td>{row[2]}</td><td>{row[1]}</td><td>{row[5]}%</td><td>{row[6]}%</td><td>{row[7]}%</td></tr>")
        return "".join(rows)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserInfoWidget()
    window.show()
    sys.exit(app.exec())
