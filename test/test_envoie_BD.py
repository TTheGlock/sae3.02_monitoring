import psycopg2



# Paramètres de connexion à la base de données
parametres_connexion = {
    'dbname': 'sae302_monitoring',
    'user': 'application',
    'password': 'gtrnet',
    'host': 'localhost',  # ou '127.0.0.1' si votre base de données est en local
    'port': '5432'  # Port par défaut de PostgreSQL
}

# Établir la connexion
connexion = psycopg2.connect(**parametres_connexion)

# Créer un curseur pour exécuter des requêtes
curseur = connexion.cursor()

# Données à insérer (sous forme de tuple)
donnees = ('192.168.1.39', 'Linux', '2.4.19', 'PC de Colin', '58.88', '40.00', '50.00')

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


psql -U application -d sae302_monitoring -c "GRANT SELECT, INSERT, UPDATE, DELETE ON machines TO application;"
