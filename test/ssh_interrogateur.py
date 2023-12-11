import paramiko

# Établir la connexion SSH
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#mettre ce programme en def ssh_vers_client(x,y): AVEC x la nouvelle_valeur et y chaque adresse ip disponible

# Informations de connexion SSH
ssh_host = '172.17.6.21'
ssh_port = 22
ssh_username = 'etudiant'
ssh_password = 'etudiant'

# Se connecter à la machine distante
ssh_client.connect(hostname=ssh_host, port=ssh_port, username=ssh_username, password=ssh_password)

# Commande Bash à exécuter à distance
commande_bash = """
#!/bin/bash

nouvelle_valeur="au revoir"
chemin_fichier="/home/etudiant/Documents/test/temp.py"

sed -i "s/ma_variable = .*/ma_variable = '$nouvelle_valeur'/" "$chemin_fichier"
"""

# Exécution de la commande Bash à distance
stdin, stdout, stderr = ssh_client.exec_command(commande_bash)

# Lire les résultats
print(stdout.read().decode())
print(stderr.read().decode())

# Fermer la connexion SSH
ssh_client.close()
