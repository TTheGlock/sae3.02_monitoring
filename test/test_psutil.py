import paramiko
import socket
import platform
import psutil
import getmac
import shutil
import netifaces as ni

def recuperation_data():
    #----- Système -----
    nom = str(platform.node())
    architecure = platform.machine() #ex : x86_64
    plateforme = platform.platform() #ex : Linux-6.5.8-200.fc38.x86_64-x86_64-with-glibc2.37
    systeme = str(platform.system())
    release = platform.release() #ex : 6.5.8-200.fc38.x86_64
    version = platform.version() #1 SMP PREEMPT_DYNAMIC Fri Oct 20 15:53:48 UTC 2023
    version = str(version.replace("#", ""))  # Remplace tous les '#' par une chaîne vide ''

    #----- CPU -----
    cpu_intervalles = 5
    cpu_charge = str(psutil.cpu_percent(interval=cpu_intervalles))

    #----- Mémoire RAM -----
    ram_total = psutil.virtual_memory().total / (2**30)
    memory_usage = str(f"{psutil.virtual_memory().percent}")

    #----- Mémoire Disque et Réseaux -----
    lettres = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]
    if systeme == "Linux":
        disque_total, disque_used, disque_free = shutil.disk_usage("/")
        ipv4 = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
    elif systeme == "Windows":
        for lettre in lettres:
            disque_total, disque_used, disque_free = shutil.disk_usage(f"{lettre}:\\")    
            adresse_ip = socket.gethostbyname(socket.gethostname())

    disque_total_gb = disque_total // (2**30)
    disque_used_gb = disque_used // (2**30)
    disque_free_gb = disque_free // (2**30)
    charge_disk = disque_used_gb/disque_total_gb*100
    charge_disk = str("{:.2f}".format(charge_disk))

    #----- Réseau -----
    adresse_mac = str(getmac.get_mac_address())
    ipv4 = str(ni.ifaddresses('eth0')[ni.AF_INET][0]['addr'])

    #----- data -----
    data = f"('{ipv4}', '{systeme}', '{version}', '{nom}', '{cpu_charge}', '{charge_disk}', '{memory_usage}')"
    
    return data

if __name__ == "__main__":
    data = recuperation_data()
    print(data)  # Pour afficher les données récupérées
