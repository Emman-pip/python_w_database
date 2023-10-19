# TODO: create database, create tables, insert into those tables, update contents, delete contents, select statements
# options for database:
# 1. mysql
# 2. sqlite
# 3. postgreSQL

import sqlite3

con = sqlite3.connect("data.db")
cur = con.cursor()


def createTable():
    cur.execute(
        "CREATE TABLE patients_tbl (patient_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, diagnosis TEXT, prescription TEXT, description TEXT);"
    )
    con.commit


def insertTo(*args):
    cur.execute(
        f"INSERT INTO patients_tbl(name, diagnosis, prescription, description) VALUES ({args[0]}, {args[1]}, {args[2]}, {args[3]});"
    )
    con.commit()


insertTo("john", "cancer", "none", "alreadydead")
# insertTo("John2", "cancer", "none", "already dead")
# insertTo("John3", "cancer", "none", "already dead")
# insertTo("John4", "cancer", "none", "already dead")
