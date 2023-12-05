import sys
import platform
import psutil
import socket
import json  # Module pour formater les données

from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

class SystemInfoWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Création d'un layout vertical
        layout = QVBoxLayout()

        # Bouton pour envoyer les informations au serveur
        send_button = QPushButton("Envoyer les informations au serveur")
        send_button.clicked.connect(self.send_info)

        # Ajout du bouton au layout
        layout.addWidget(send_button)

        # Appliquer le layout à la fenêtre principale
        self.setLayout(layout)

    def get_system_info(self):
        os_info = platform.platform()
        version_info = platform.version()
        hostname_info = platform.node()
        ip_address_info = socket.gethostbyname(socket.gethostname())
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        system_info = {
            "OS": os_info,
            "Version du système": version_info,
            "Hostname": hostname_info,
            "Adresse IP": ip_address_info,
            "Charge CPU": cpu_usage,
            "Charge mémoire": memory_usage,
            "Charge des disques": disk_usage
        }
        return system_info

    def send_info(self):
        # Récupérer les informations système
        system_info = self.get_system_info()

        # Convertir les données en JSON
        serialized_data = json.dumps(system_info).encode('utf-8')

        # Établir une connexion avec le serveur
        server_address = ('172.17.15.21', 12345)  # Adresse et port du serveur
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(server_address)

        # Envoyer les informations au serveur
        client_socket.sendall(serialized_data)

        # Fermeture de la connexion avec le serveur
        client_socket.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SystemInfoWidget()
    window.setWindowTitle('Informations Système - Client')
    window.setGeometry(100, 100, 400, 400)
    window.show()
    sys.exit(app.exec())
