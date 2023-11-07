#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 15:04:21 2023

@author: khoung01
"""
#Importation des modules
import sys
import socket
import os
import psutil 

#Définition du module qui récupère les données. Il faut noter que c'est propre à psutil .
def get_system_info():
    """
    Récupère les infos spécifiques à une machine
    
    L'utilisateur n'a pas grand chose à faire.
    Il exécute le script et les modules os, sys et psutil et leurs attributs récupèrent les infos.
    
    Returns:
       hostname:string 
       os_info:string
       cpu_usage:float
       memory_usage:float
       disk_usage:float
    
    """
    
    hostname = socket.gethostname()
    os_info = f"{sys.platform} {os.name}"
    cpu_usage = f"{psutil.cpu_percent(interval=1)}%"
    memory_usage = f"{psutil.virtual_memory().percent}%"
    disk_usage = f"{psutil.disk_usage('/').percent}%"

    return f"Hostname: {hostname}\nOS: {os_info}\nCPU Usage: {cpu_usage}\nMemory Usage: {memory_usage}\nDisk Usage: {disk_usage}"


if __name__ == '__main__':
    info = get_system_info()
    print(info)
