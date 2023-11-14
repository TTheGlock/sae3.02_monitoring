# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:38:20 2023

@author: charb
"""

import socket
import ast  # Module pour convertir la chaîne JSON en dictionnaire

# Configuration du serveur
server_address = ('127.0.0.1', 12345)  # Adresse et port du serveur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(1)

print(f"Le serveur écoute sur {server_address}")

while True:
    # Attente de la connexion d'un client
    print("En attente de la connexion d'un client...")
    client_socket, client_address = server_socket.accept()
    print(f"Connexion établie avec {client_address}")

    # Réception des données du client
    data = client_socket.recv(1024)
    if not data:
        break

    # Conversion de la chaîne JSON en dictionnaire
    system_info = ast.literal_eval(data.decode('utf-8'))

    # Affichage des informations reçues
    print("\nInformations reçues du client:")
    for key, value in system_info.items():
        print(f"{key}: {value}")

    # Fermeture de la connexion avec le client
    client_socket.close()
    print("Connexion avec le client fermée\n")

# Fermeture du socket du serveur
server_socket.close()
