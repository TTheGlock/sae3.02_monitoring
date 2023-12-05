# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 20:39:26 2023

@author: charb
"""

import socket
import json
import psycopg2

# Établir la connexion à la base de données PostgreSQL
conn = psycopg2.connect(
    dbname='sae_database',
    user='sae',
    password='sae2023',
    host='localhost',
    port='5432'
)
cursor = conn.cursor()

# Créer la table pour stocker les données si elle n'existe pas déjà
cursor.execute('''
    CREATE TABLE IF NOT EXISTS system_info (
        id SERIAL PRIMARY KEY,
        os VARCHAR(100),
        system_version VARCHAR(100),
        hostname VARCHAR(100),
        ip_address VARCHAR(15),
        cpu_usage FLOAT,
        memory_usage FLOAT,
        disk_usage FLOAT
    )
''')
conn.commit()

# Mettre en place le serveur pour recevoir les données
server_address = ('172.17.15.21', 12345)  # Adresse et port du serveur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(1)

print("Serveur en attente de connexions...")

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connexion établie avec {client_address}")

    # Recevoir les données du client
    received_data = b''
    while True:
        chunk = client_socket.recv(4096)
        if not chunk:
            break
        received_data += chunk

    # Décodez les données depuis JSON
    decoded_data = received_data.decode('utf-8')
    system_info = json.loads(decoded_data)

    # Afficher les données reçues
    print("Données reçues du client :")
    for key, value in system_info.items():
        print(f"{key}: {value}")

    # Insérer les données dans la base de données
    insert_query = '''
        INSERT INTO system_info 
        (os, system_version, hostname, ip_address, cpu_usage, memory_usage, disk_usage) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    cursor.execute(insert_query, (
        system_info['OS'],
        system_info['Version du système'],
        system_info['Hostname'],
        system_info['Adresse IP'],
        system_info['Charge CPU'],
        system_info['Charge mémoire'],
        system_info['Charge des disques']
    ))
    conn.commit()

    print("Données enregistrées dans la base de données")

    # Fermeture de la connexion avec le client
    client_socket.close()

# Fermeture de la connexion à la base de données et du serveur
cursor.close()
conn.close()
server_socket.close()
