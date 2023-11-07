#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 15:04:42 2023

@author: khoung01
"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import QTimer
import subprocess
import time

class DashboardApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dashboard")
        self.setGeometry(100, 100, 400, 200)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.info_label = QLabel()
        self.layout.addWidget(self.info_label)

        self.refresh_label = QLabel()
        self.layout.addWidget(self.refresh_label)

      
        self.update_info()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_info)
        self.timer.start(5000)  # Actualise les données toutes les 5 secondes

    def update_info(self):
        # Exécute le script test.py pour obtenir les informations
        start_time = time.time()
        result = subprocess.run(["/home/khoung01/Téléchargements/test.py"], capture_output=True, text=True)
        end_time = time.time()
        
        if result.returncode == 0:
            system_info = result.stdout
            refresh_time = end_time - start_time
            self.info_label.setText(system_info)
            self.refresh_label.setText(f"Refresh Time: {refresh_time:.2f} seconds")
        else:
            self.info_label.setText("Erreur lors de la récupération des données.")
            self.refresh_label.setText("")

def main():
    app = QApplication(sys.argv)
    window = DashboardApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
