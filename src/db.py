# TODO: create database, create tables, insert into those tables, update contents, delete contents, select statements
# options for database:
# 1. mysql
# 2. sqlite
# 3. postgreSQL

import mysql.connector as my

con = my.connect(
    host="bfronqa2lmvgzf0kknx2-mysql.services.clever-cloud.com",
    database="bfronqa2lmvgzf0kknx2",
    user="ujx2n1qf7n69vjbg",
    password="qGqc18Xc28aj1G1dvmKo",
)

cur = con.cursor()


def createTable():
    cur.execute(
        "CREATE TABLE patients_tbl (patient_id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(35) NOT NULL, diagnosis VARCHAR(100), prescription VARCHAR(100), description VARCHAR(300));"
    )
    con.commit()
    cur.close()


def insertTo(*args):
    cur.execute(
        f"INSERT INTO patients_tbl (name, diagnosis, prescription, description) VALUES ('{args[0]}', '{args[1]}', '{args[2]}', '{args[3]}');"
    )
    con.commit()
    cur.close()


def select(id=None):
    if id == None:
        rows = cur.execute(
            """
            SELECT * FROM patients_tbl
        """
        )
    else:
        rows = cur.execute(
            f"""
            SELECT * 
            FROM patients_tbl
            WHERE patient_id = {id}
       """
        )
    return cur.fetchall()


def update(id, name, diagnosis, prescription, description):
    cur.execute(
        f"""
        UPDATE patients_tbl
        SET name = '{name}', diagnosis = '{diagnosis}', prescription = '{prescription}', description = '{description}'
        where patient_id = {id};
    """
    )
    con.commit()
    cur.close()


def deleteWithID(id):
    cur.execute(
        f"""
        DELETE FROM patients_tbl
        where patient_id = {id}
    """
    )
    con.commit()
    cur.close()


def closeConnection():
    con.close()
