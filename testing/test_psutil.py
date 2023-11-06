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

#----- Disque -----

if systeme == "Linux":
    total, used, free = shutil.disk_usage("/")
elif systeme == "Windows":
    total, used, free = shutil.disk_usage("C:\\")    

total_gb = total // (2**30)  #transformation de bits en gigabits
used_gb = used // (2**30)  #//
free_gb = free // (2**30)  #//
en_tout = used_gb/total_gb*100

#----- Réseau -----

adresse_mac = str(getmac.get_mac_address())
adresse_ip = socket.gethostbyname(socket.gethostname()) #ipv4 locale