# TODO: create database, create tables, insert into those tables, update contents, delete contents, select statements
# options for database:
# 1. mysql
# 2. sqlite
# 3. postgreSQL

import sqlite3

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


class database:
    def __init__(self):
        pass

    def connect(self):
        self.con = sqlite3.connect("data.db")
        self.cur = self.con.cursor()

    def createTable(self):
        self.connect()

        self.cur.execute(
            "CREATE TABLE patients_tbl (patient_id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(35) NOT NULL, diagnosis VARCHAR(100), prescription VARCHAR(100), description VARCHAR(300));"
        )
        self.con.commit()
        self.closeConnection()

    def insertTo(self, *args):
        self.connect()
        self.cur.execute(
            f"INSERT INTO patients_tbl (name, diagnosis, prescription, description) VALUES ('{args[0]}', '{args[1]}', '{args[2]}', '{args[3]}');"
        )
        self.con.commit()
        self.closeConnection()

    def select(self, id=None):
        self.connect()
        if id == None:
            rows = self.cur.execute(
                """
                SELECT * FROM patients_tbl
            """
            )
            data = self.cur.fetchall()
            self.closeConnection()
        else:
            rows = self.cur.execute(
                f"""
                SELECT * 
                FROM patients_tbl
                WHERE patient_id = {id}
        """
            )
            data = self.cur.fetchall()
            self.closeConnection()
        return data

    def update(self, id, name, diagnosis, prescription, description):
        self.connect()

        self.cur.execute(
            f"""
            UPDATE patients_tbl
            SET name = '{name}', diagnosis = '{diagnosis}', prescription = '{prescription}', description = '{description}'
            where patient_id = {id};
        """
        )
        self.con.commit()
        self.closeConnection()

    def deleteWithID(self, id):
        self.connect()

        self.cur.execute(
            f"""
            DELETE FROM patients_tbl
            where patient_id = {id}
        """
        )
        self.con.commit()
        self.closeConnection

    def closeConnection(self):
        self.con.close()


if __name__ != "__main__":
    try:
        database()
    except:
        app = ErrorWindow()
        app.mainloop()
