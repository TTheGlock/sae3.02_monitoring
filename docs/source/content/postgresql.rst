=============================================
Documentation PostgreSQL
=============================================   

--------------------------------------------
Création et Utilisation de la BD PostreSQL
--------------------------------------------

Pour créer la base de données PostgreSQL sur une de nos VMs : 

.. code-block:: sql
			
	CREATE DATABASE sae302-monitoring;

Pour utiliser cette base de données : 

.. code-block:: sql
			
	USE sae302-monitoring;

--------------------------------------------
Création de la table principale : ``machines``
--------------------------------------------

.. code-block:: sql

    CREATE TABLE machines (
        id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        operating_system varchar(50) NOT NULL,
        version_system varchar(50) NOT NULL,
        name varchar(50) NOT NULL,
        cpu_charge float NOT NULL,
        heuredepart timestamp NOT NULL,
        heurearrivee timestamp NOT NULL
    );