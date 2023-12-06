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
Création et utilisation de la BD PostgreSQL : ``sae302_monitoring``
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
        id SERIAL NOT NULL,
        ip_addr varchar(15) NOT NULL,
        operating_system varchar(50) NOT NULL,
        system_version varchar(50) NOT NULL,
        name varchar(50) NOT NULL,
        cpu_charge numeric(4,2) NOT NULL,
        ram_charge numeric(4,2) NOT NULL,
        disk_charge numeric(4,2) NOT NULL
    );

Puis pour donner certains droits sur la table ``machines`` à l'utilisateur ``application`` : 

.. code-block:: sql

    GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES ON machines TO application;

--------------------------------------------
Insertion de données dans la table principale
--------------------------------------------

Exemple d'insertion dans la table ``machines`` :

.. code-block:: sql

    INSERT INTO machines VALUES (DEFAULT, '192.168.1.39', 'Linux', '2.4.19', 'PC de Colin', 58.88, 46.96, 32.00);
