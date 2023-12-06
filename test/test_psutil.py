import socket
import platform
import psutil
import getmac 
import shutil
import netifaces as ni

#----- Système -----

nom = platform.node()  #ex : PC de Jacques
architecure = platform.machine()  #ex : x86_64
plateforme = platform.platform()  #ex : Linux-6.5.8-200.fc38.x86_64-x86_64-with-glibc2.37
systeme = platform.system()  #ex : Linux
release = platform.release()  #ex : 6.5.8-200.fc38.x86_64
version = platform.version()  #ex : #1 SMP PREEMPT_DYNAMIC Fri Oct 20 15:53:48 UTC 2023

#----- CPU -----

cpu_intervalles = 5
cpu_charge = str(psutil.cpu_percent(interval=cpu_intervalles))

#----- Mémoire RAM -----

ram_total = psutil.virtual_memory().total / (2**30)

memory_usage = f"{psutil.virtual_memory().percent}"


#----- Mémoire Disque et Réseaux-----

lettres = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]

if systeme == "Linux":
    disque_total, disque_used, disque_free = shutil.disk_usage("/")
    ipv4 = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
elif systeme == "Windows":
    for lettre in lettres:
        disque_total, disque_used, disque_free = shutil.disk_usage(f"{lettre}:\\")    
        adresse_ip = socket.gethostbyname(socket.gethostname()) #ipv4 locale

disque_total_gb = disque_total // (2**30)  #transformation de bits en gigabits
disque_used_gb = disque_used // (2**30)  #//
disque_free_gb = disque_free // (2**30)  #//
en_tout_disk = disque_used_gb/disque_total_gb*100

# Formater le pourcentage avec 2 décimales
en_tout_disk = "{:.2f}".format(en_tout_disk)

#----- Réseau -----

adresse_mac = str(getmac.get_mac_address())  #ipv6 locale
#adresse_ip = socket.gethostbyname(socket.gethostname()) #ipv4 locale

#print(adresse_mac, adresse_ip) #avoir 

ipv4 = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']

print(ipv4)



#----- data -----

data = f"('{nom}', '{architecure}', '{plateforme}', '{systeme}', '{cpu_charge}', '{ipv4}', '{en_tout_disk}', '{memory_usage}')"

print(f"{data}")

#----- send ----- 

send = f"INSERT INTO vendors(nom, architecture, plateform, system, cpu_charge, ipv4, en_tout_disk, memory_usage) VALUES{data} RETURNING vendor_id;"


print(send)