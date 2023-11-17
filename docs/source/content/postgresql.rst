=============================================
Documentation PostgreSQL
=============================================   

.. note:: 

    Cette documentation retrace seulement les commandes effectuées pour la partie PostgreSQL (exemple : création des tables, mise en place d'utilisateurs...).

--------------------------------------------
Connexion à la BD PostgreSQL
--------------------------------------------

.. code-block:: bash

    sudo -u posgres -i
    psql

.. code-block:: sql

    ALTER USER postgres PASSWORD 'gtrnet';

--------------------------------------------
Création d'un utilisateur pour l'application
--------------------------------------------

.. code-block:: sql

    CREATE USER application WITH PASSWORD 'gtrnet';

--------------------------------------------
Création et utilisation de la BD PostgreSQL
--------------------------------------------

Pour créer la base de données PostgreSQL sur une de nos VMs : 

.. code-block:: sql

	CREATE DATABASE sae302_monitoring OWNER application;

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
        id SERIAL,
        ip_addr varchar(15) NOT NULL,
        operating_system varchar(50) NOT NULL,
        system_version varchar(50) NOT NULL,
        name varchar(50) NOT NULL,
        cpu_charge float NOT NULL,
        ram_charge float NOT NULL,
        disk_charge float NOT NULL
    );

Puis pour donner certains droits sur la table ``machines`` à l'utilisateur ``application`` : 

.. code-block:: sql

    GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON machines TO application;