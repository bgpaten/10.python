import mysql.connector

config = {
    'user': 'ahyar',
    'password': 'bismillah1',
    'host': 'localhost',
    'database': 'acme'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()