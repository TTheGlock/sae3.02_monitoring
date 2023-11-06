import socket
import platform
import psutil
import getmac
import shutil

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

print(ram_total, -3)

#----- Mémoire Disque -----

lettres = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O"]

if systeme == "Linux":
    disque_total, disque_used, disque_free = shutil.disk_usage("/")
elif systeme == "Windows":
    for lettre in lettres:
        disque_total, disque_used, disque_free = shutil.disk_usage(f"{lettre}:\\")    

disque_total_gb = disque_total // (2**30)  #transformation de bits en gigabits
disque_used_gb = disque_used // (2**30)  #//
disque_free_gb = disque_free // (2**30)  #//
en_tout = disque_used_gb/disque_total_gb*100

#----- Réseau -----

adresse_mac = str(getmac.get_mac_address())  #ipv6 locale
adresse_ip = socket.gethostbyname(socket.gethostname()) #ipv4 locale