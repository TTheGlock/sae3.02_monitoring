#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 15:04:21 2023

@author: khoung01
"""

import sys
import socket
import os
import psutil 

def get_system_info():
    hostname = socket.gethostname()
    os_info = f"{sys.platform} {os.name}"
    cpu_usage = f"{psutil.cpu_percent(interval=1)}%"
    memory_usage = f"{psutil.virtual_memory().percent}%"
    disk_usage = f"{psutil.disk_usage('/').percent}%"

    return f"Hostname: {hostname}\nOS: {os_info}\nCPU Usage: {cpu_usage}\nMemory Usage: {memory_usage}\nDisk Usage: {disk_usage}"


if __name__ == '__main__':
    info = get_system_info()
    print(info)
