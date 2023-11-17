=============================================
Documentation PostgreSQL
=============================================   

--------------------------------------------
Création et Utilisation de la BD PostgreSQL
--------------------------------------------

Pour se connecter à PostgreSQL :

.. code-block:: bash
			
	sudo -u posgres -i
    psql 

.. code-block:: sql
    
    ALTER USER postgres PASSWORD 'gtrnet';

Pour créer la base de données PostgreSQL sur une de nos VMs : 

.. code-block:: sql
			
	CREATE DATABASE sae302-monitoring OWNER admin;

Pour utiliser cette base de données : 

.. code-block:: sql
			
	\c sae302-monitoring;

--------------------------------------------
Création de la table principale : ``machines``
--------------------------------------------

La table devra accueillir, dans l'ordre : 
- Le système utilisé (OS)
- La version du système utilisé
- Le nom de l'hôte
- La charge du CPU
- La charge mémoire (RAM)
- La charge du(des) disque(s)

.. code-block:: sql

    CREATE TABLE machines (
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        operating_system varchar(50) NOT NULL,
        system_version varchar(50) NOT NULL,
        name varchar(50) NOT NULL,
        cpu_charge float NOT NULL,
        ram_charge float NOT NULL,
        disk_charge float NOT NULL
    );