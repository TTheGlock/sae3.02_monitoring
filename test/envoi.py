# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:32:24 2023

@author: charb
"""

import sys
import psutil
import platform
import socket
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class ClientWidget(QWidget):
    def __init__(self):
        super(ClientWidget, self).__init__()

        self.server_address = ('127.0.0.1', 12345)  # Adresse et port du serveur
        self.client_socket = None

        self.init_ui()

    def init_ui(self):
        # Création des widgets
        self.connect_button = QPushButton('Connecter au serveur', self)
        self.info_label = QLabel('Appuyez sur le bouton pour envoyer les informations au serveur.', self)

        # Mise en place du layout
        layout = QVBoxLayout()
        layout.addWidget(self.connect_button)
        layout.addWidget(self.info_label)

        self.setLayout(layout)

        # Connexion des signaux
        self.connect_button.clicked.connect(self.send_info_to_server)

    def send_info_to_server(self):
        if not self.client_socket:
            # Création du socket client et connexion au serveur
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect(self.server_address)

            # Récupération des informations système
            system_info = {
                "os": platform.system(),
               "version": platform.version(),
               "hostname": platform.node(),
                "cpu": psutil.cpu_percent(),
                "memory": psutil.virtual_memory().percent,
                "disk": psutil.disk_usage('/').percent
            }

            # Envoi des informations au serveur
            self.client_socket.send(str(system_info).encode('utf-8'))

            # Fermeture du socket client après l'envoi des informations
            self.client_socket.close()
            self.client_socket = None

            # Mise à jour de l'étiquette d'information
            self.info_label.setText('Informations envoyées au serveur.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ClientWidget()
    window.setWindowTitle('Client d\'Informations Système')
    window.setGeometry(100, 100, 400, 200)
    window.show()
    sys.exit(app.exec_())
