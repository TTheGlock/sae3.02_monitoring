import psycopg2
from recuperation import recuperation_data
import time

a = 10

# Paramètres de connexion à la base de données
parametres_connexion = {
    'dbname': 'sae302_monitoring',
    'user': 'application',
    'password': 'gtrnet',
    'host': '172.17.21.25',  # ou '127.0.0.1' si votre base de données est en local
    'port': '5432'  # Port par défaut de PostgreSQL
}

while True:
    # Établir la connexion
    connexion = psycopg2.connect(**parametres_connexion)

    # Créer un curseur pour exécuter des requêtes
    curseur = connexion.cursor()

    # Données à insérer (sous forme de tuple)
    #donnees = ('192.168.1.39', 'Linux', '2.4.19', 'PC de Colin', '58.88', '40.00', '50.00')
    #donnees = ('172.17.6.21', 'Linux', '1 SMP PREEMPT_DYNAMIC Debian 6.1.55-1 (2023-09-29)', 'deb12', '10.1', '56.67', '79.0')
    donnees = recuperation_data()

    # Requête SQL d'insertion avec des placeholders (%s)
    requete_insertion = "INSERT INTO machines VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s);"

    print(requete_insertion)
    print(donnees)

    # Exécuter la requête avec les données
    curseur.execute(requete_insertion, donnees)


    # Valider les modifications dans la base de données
    connexion.commit()

    # Fermer le curseur et la connexion
    curseur.close()
    connexion.close()

    # Rafraîchissement toutes les 10 secondes
    print("Rafraîchissement...")
    time.sleep(a)
