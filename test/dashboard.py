#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 15:04:42 2023

@author: khoung01
"""
#Importation des modules utiles à la compilation du code
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QTimer
import subprocess
import time

#Création de la classe
class DashboardApp(QWidget):
    #Constructeur
    def __init__(self):
        """
        Constructeur de la classe DashboardApp

        Il réalise la mise en place de l'interface graphique sur laquelle sera afficher les informations récupérer 
        dans test.py
        
        La particularité ici c'est que les données récupérer dans test.py sont actualiser selon une durée donnée de 
        manière automatique. Le refresh time est affiché totalement en bas de la fenêtre.
        
        Returns
        -------
        Domnnées de test.py
            hostname:string 
            os_info:string
            cpu_usage:float
            memory_usage:float
            disk_usage:float
        
        """
        
        
        super().__init__()
        
        #Nom et dimension de la fenêtre
        self.setWindowTitle("Dashboard")
        self.setGeometry(100, 100, 400, 200)
        
        #Mise en place des infos sur la fenêtre
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.info_label = QLabel()
        self.layout.addWidget(self.info_label)

        self.refresh_label = QLabel()
        self.layout.addWidget(self.refresh_label)

      
        self.update_info()
        
        #Gestion du timming d'exécution de la fenêtre
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_info)
        self.timer.start(5000)  # Actualise les données toutes les 5 secondes

    def update_info(self):
        """
        Gère l'actualisation des données reçues de test.py
        
        Il recompile test.py et calcule le refresh time
        
        Une condition a été mise en place pour n'afficher le résultat que quand la compilation se passe bien. En cas 
        d'erreur, un message d'erreur est envoyeé.
        
        Returns
        -------
        Novelles Domnnées de test.py
            hostname:string 
            os_info:string
            cpu_usage:float
            memory_usage:float
            disk_usage:float


        
        """
        # Exécute le script test.py pour obtenir les informations
        start_time = time.time()
        result = subprocess.run(["/home/khoung01/Téléchargements/test.py"], capture_output=True, text=True)
        end_time = time.time()
        
        #Exécution du code en cas d'exécution réussie du script
        if result.returncode == 0:
            system_info = result.stdout
            refresh_time = end_time - start_time
            self.info_label.setText(system_info)
            self.refresh_label.setText(f"Refresh Time: {refresh_time:.2f} seconds")
       
        #Exécution du code en cas de mauvaise exécution du script
        else:
            self.info_label.setText("Erreur lors de la récupération des données.")
            self.refresh_label.setText("")

#Compilation
def main():
    app = QApplication(sys.argv)
    window = DashboardApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
