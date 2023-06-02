GUIDE D'INSTALLATION
Installation de Flask

    sudo apt install python3-flask

Installation de pymysql

    sudo apt install python3-pymysql

Ajuster les paramètres de connexion de la base selon la configuration de la base
Dans crud-rds-mysql.py, modifier les lignes 6,7,8,9
      host, user, password, database 
Dans client-rds-mysql.py, modifier l'URL


Pour éxecuter, lancer python3 crud-rds-mysql.py et puis python3 client-rds-mysql.py
