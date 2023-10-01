# TODO: create database, create tables, insert into those tables, update contents, delete contents, select statements
# options for database:
# 1. mysql
# 2. sqlite
# 3. postgreSQL

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="108996eE@emman", database="sampledb"
)

myCursor = mydb.cursor()


def showDBs():
    myCursor.execute("SHOW DATABASES")
    for i in myCursor:
        print(i)


def createDB(databaseName):
    myCursor.execute(f"CREATE DATABASE {databaseName}")


def createTABLE(tablename, *name):
    values = ""
    for i in name:
        if i == name[-1]:
            values += f"{i}"
            break
        values += f"{i},"
    command = f"CREATE TABLE {tablename} ({values})"
    mydb.start_transaction()
    myCursor.execute(command)
    mydb.commit()
    mydb.close()


def select(tablename, columns):
    mydb.start_transaction()
    myCursor.execute(f"SELECT {columns} FROM {tablename}")
    myResult = myCursor.fetchall()
    for i in myResult:
        print(i)
    mydb.close()


def insert(tablename, parameters, *values):
    columns = ""
    data = ""
    for i in parameters:
        if i == parameters[-1]:
            columns += f"{i}"
            break
        columns += f"{i},"
    for x in values:
        if x == values[-1]:
            data += f"('{x}')"
            break
        data += f"('{x}'),"
    print(parameters[0], columns, data)

    command = f"INSERT INTO {tablename}({columns}) VALUES{data};"
    print(command)
    mydb.start_transaction()
    myCursor.execute(command)
    mydb.commit()
    mydb.close()


# insert("sample_table", ["name"], ("Juju"), ("Jumanji"))
# select("sample_table", "*")
