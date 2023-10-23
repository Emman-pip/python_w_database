# TODO: create database, create tables, insert into those tables, update contents, delete contents, select statements
# options for database:
# 1. mysql
# 2. sqlite
# 3. postgreSQL

import mysql.connector as my

# import redo_main

import customtkinter


class ErrorWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("dark")
        self.grid_columnconfigure(0, weight=1)
        self.title("ERROR")
        self.lbl_error = customtkinter.CTkLabel(
            self, text="ERROR: CHECK YOUR CONNECTION"
        )
        self.lbl_error.grid(row=0, column=0, pady=30, padx=30)


try:
    con = my.connect(
        host="bfronqa2lmvgzf0kknx2-mysql.services.clever-cloud.com",
        database="bfronqa2lmvgzf0kknx2",
        user="ujx2n1qf7n69vjbg",
        password="qGqc18Xc28aj1G1dvmKo",
    )

    cur = con.cursor()
except:
    app = ErrorWindow()
    app.mainloop()


def createTable():
    cur.execute(
        "CREATE TABLE patients_tbl (patient_id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(35) NOT NULL, diagnosis VARCHAR(100), prescription VARCHAR(100), description VARCHAR(300));"
    )
    con.commit()


def insertTo(*args):
    cur.execute(
        f"INSERT INTO patients_tbl (name, diagnosis, prescription, description) VALUES ('{args[0]}', '{args[1]}', '{args[2]}', '{args[3]}');"
    )
    con.commit()


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


def deleteWithID(id):
    cur.execute(
        f"""
        DELETE FROM patients_tbl
        where patient_id = {id}
    """
    )
    con.commit()


def closeConnection():
    con.close()
