# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 20:39:26 2023

@author: charb
"""

import socket
import psycopg2

# Connexion à PostgreSQL (adapté avec vos informations de connexion)
conn = psycopg2.connect(
    dbname='votre_nom_de_bdd',
    user='votre_utilisateur',
    password='votre_mot_de_passe',
    host='localhost',
    port='votre_port'
)
cursor = conn.cursor()

# Création de la table si elle n'existe pas déjà
cursor.execute('''
    CREATE TABLE IF NOT EXISTS system_info (
        id SERIAL PRIMARY KEY,
        os TEXT,
        version TEXT,
        hostname TEXT,
        cpu INTEGER,
        memory INTEGER,
        ip TEXT,
        disk INTEGER
    )
''')
conn.commit()

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
    data = client_socket.recv(4096)

    if not data:
        break

    # Décodage des données
    system_info = data.decode()

    # Séparation des données reçues
    info_list = system_info.split(',')

    # Insertion des données dans la base de données
    cursor.execute('''
        INSERT INTO system_info (os, version, hostname, cpu, memory, ip, disk)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    ''', (info_list[0], info_list[1], info_list[2], info_list[3], info_list[4], info_list[5], info_list[6]))

    # Commit des changements dans la base de données
    conn.commit()

    # Fermeture de la connexion avec le client
    client_socket.close()
    print("Connexion avec le client fermée\n")

# Fermeture du socket du serveur
server_socket.close()
