import psycopg2
from graph_test import graph_1

# Établit une connexion à la base de données PostgreSQL
conn = psycopg2.connect(
    dbname='sae302_monitoring',
    user='application',
    password='gtrnet',
    host='localhost',
    port='5432'
)

# Crée un objet curseur pour exécuter des requêtes SQL
cursor = conn.cursor()

# Requête pour récupérer les 10 derniers cpu_charge, ram_charge et disk_charge de l'adresse IP '192.168.1.39'
query = """
    SELECT cpu_charge, ram_charge, disk_charge
    FROM machines
    WHERE ip_addr = '172.17.6.21'
    LIMIT 10
"""

# Exécute la requête et récupère les résultats
cursor.execute(query)
results = cursor.fetchall()

# Convertit les charges en chiffres
cpu_charge = []
ram_charge = []
disk_charge = []
for result in results:
    cpu_charge.append(int(result[0]))
    ram_charge.append(int(result[1]))
    disk_charge.append(int(result[2]))

# Affiche les charges
print("CPU charge :", cpu_charge)
print("Ram charge :", ram_charge)
print("Disk charge :", disk_charge)

# Ferme la connexion à la base de données
conn.close()




