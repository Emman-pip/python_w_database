import tkinter
import customtkinter
import tkinter.messagebox
from db import *
from threading import Timer

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("dark")
customtkinter.deactivate_automatic_dpi_awareness()


class App(customtkinter.CTk):
    def __init__(self):
        padding = 10
        super().__init__()
        self.data = db()
        self.geometry("1000x370")
        self.title("Hospital Records")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.frm = customtkinter.CTkFrame(
            self,
            width=300,
        )
        self.frm.grid(
            row=0,
            column=0,
            # padx=padding,
            # pady=padding,
            sticky="nswe",
        )
        # self.frm_left.columnconfigure(0, weight=0)
        self.frm.grid_columnconfigure(1, weight=3)
        self.frm.grid_rowconfigure(0, weight=1)

        self.frm_left = customtkinter.CTkFrame(
            self.frm,
            width=300,
        )
        self.frm_left.grid(
            row=0,
            column=0,
            padx=padding,
            pady=padding,
            sticky="nswe",
        )

        # elements on the left side

        self.frm_search = customtkinter.CTkFrame(self.frm_left)
        self.frm_search.grid(row=0, padx=padding, pady=padding)
        self.btn_login = customtkinter.CTkButton(
            self.frm_left, text="login", command=lambda: self.open()
        )
        self.btn_login.grid(
            row=1,
            pady=padding,
            padx=padding,
        )
        self.ent_search = customtkinter.CTkEntry(
            self.frm_search,
            placeholder_text="Enter Patient ID",
        )
        self.ent_search.grid(row=0, column=0)
        self.btn_search = customtkinter.CTkButton(
            self.frm_search,
            text="search",
            command=lambda: self.searchFunc(self.ent_search.get()),
        )
        self.btn_search.grid(row=1, column=0, pady=padding / 2)

        self.frm_right_part = customtkinter.CTkFrame(self.frm)
        self.frm_right_part.grid(
            row=0,
            column=1,
            padx=padding,
            pady=padding,
            sticky="nsew",
            # columnspan=3,
        )
        self.frm_right_part.columnconfigure(0, weight=1)
        self.frm_right_part.rowconfigure(0, weight=1)
        # self.frm_right_part.rowconfigure(1, weight=3)

        self.frm_records = customtkinter.CTkScrollableFrame(
            self.frm_right_part, border_color="dark_color", height=200
        )
        # self.frm_records.columnconfigure(1, pad=10)
        self.frm_records.columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.frm_records.grid(
            row=0,
            column=0,
            padx=padding / 2,
            pady=padding / 2,
            sticky="nsew",
            # columnspan=3,
        )

        self.displayRecords()

    def searchFunc(self, id):
        try:
            padding = 10
            result = self.data.select(id)
            blue = "#838383"
            blueish = "#aaaaaa"
            # print(result)

            self.frm_display_result = customtkinter.CTkFrame(
                self.frm_right_part,
            )
            self.frm_display_result.grid(
                row=1, column=0, sticky="new", padx=padding / 2, pady=padding / 2
            )
            self.frm_display_result.columnconfigure((0, 1, 2, 3, 4), weight=1)

            self.lbl_result_text = customtkinter.CTkLabel(
                self.frm_display_result,
                text=f"Result for patientID#{self.ent_search.get()}:",
            )
            self.lbl_result_text.grid(pady=padding / 2, row=0)
            self.records(
                self.frm_display_result,
                "ID",
                "name",
                "diagnosis",
                "prescription",
                "description",
                1,
                blue,
            )

            self.records(
                self.frm_display_result,
                result[0][0],
                result[0][1],
                result[0][2],
                result[0][3],
                result[0][4],
                2,
                blueish,
            )
        except:
            self.lbl_err = customtkinter.CTkLabel(
                self.frm_search, text="Invalid ID", text_color="red"
            )
            self.lbl_err.grid(row=2)
            timeout = Timer(2.0, lambda: self.lbl_err.grid_forget())
            timeout.start()

    def displayRecords(self):
        blue = "#838383"
        blueish = "#aaaaaa"
        whitish = "#d4d4d4"
        self.records(
            self.frm_records,
            "ID",
            "name",
            "diagnosis",
            "prescription",
            "description",
            0,
            blue,
        )
        x = 0
        for i in self.data.select():
            if x % 2 == 1:
                self.records(
                    self.frm_records, i[0], i[1], i[2], i[3], i[4], i[0], blueish
                )
            else:
                self.records(
                    self.frm_records, i[0], i[1], i[2], i[3], i[4], i[0], whitish
                )
            x += 1

    def records(
        self,
        master,
        id,
        name,
        diagnosis,
        prescription,
        description,
        row=0,
        bg="transparent",
    ):
        textColor = "black"
        padding = 20
        self.lbl_id = customtkinter.CTkLabel(
            master, text=id, bg_color=bg, text_color=textColor
        )
        self.lbl_name = customtkinter.CTkLabel(
            master, text=name, bg_color=bg, text_color=textColor
        )
        self.lbl_diagnosis = customtkinter.CTkLabel(
            master, text=diagnosis, bg_color=bg, text_color=textColor
        )
        self.lbl_prescription = customtkinter.CTkLabel(
            master, text=prescription, bg_color=bg, text_color=textColor
        )
        self.lbl_description = customtkinter.CTkLabel(
            master, text=description, bg_color=bg, text_color=textColor
        )
        # to be appplied with grid
        self.lbl_id.grid(column=0, row=row, sticky="ew")
        self.lbl_name.grid(column=1, row=row, sticky="ew")
        self.lbl_diagnosis.grid(column=2, row=row, sticky="ew")
        self.lbl_prescription.grid(column=3, row=row, sticky="ew")
        self.lbl_description.grid(column=4, row=row, sticky="ew")

    def open(self):
        self.destroy()
        login = loginWindow()
        login.mainloop()


class loginWindow(customtkinter.CTk):
    def __init__(self):
        padding = 10
        padding2 = 5
        self.data = db()
        super().__init__()
        self.columnconfigure(0, weight=1)
        # self.geometry("1000x750")
        self.title("Login")
        self.frm_frame = customtkinter.CTkFrame(self)
        self.frm_frame.columnconfigure(0, weight=1)

        self.frm_frame.grid(sticky="nsew", padx=padding, pady=padding2)
        self.columnconfigure(0, weight=1)
        self.ent_username = customtkinter.CTkEntry(
            self.frm_frame, placeholder_text="Username"
        )
        self.ent_username.grid(column=0, row=0, pady=padding, padx=padding2)

        self.ent_password = customtkinter.CTkEntry(
            self.frm_frame, placeholder_text="Password"
        )
        self.ent_password.grid(column=0, row=1)

        self.btn_login = customtkinter.CTkButton(
            self.frm_frame, text="Login", command=lambda: self.credentials()
        )
        self.btn_login.grid(column=0, row=2, pady=padding, padx=padding)

        self.btn_back = customtkinter.CTkButton(
            self.frm_frame, text="Back", command=lambda: self.back()
        )
        self.btn_back.grid(column=0, row=3, pady=padding, padx=padding)

    def credentials(self):
        if self.ent_username.get() == "root" and self.ent_password.get() == "root":
            self.destroy()
            root = RootUser()
            root.mainloop()
        else:
            self.lbl_err = customtkinter.CTkLabel(
                self.frm_frame, text="Invalid ID/PASS", text_color="red"
            )
            self.lbl_err.grid(row=4)
            timeout = Timer(2.0, lambda: self.lbl_err.grid_forget())
            timeout.start()

    def back(self):
        self.destroy()
        app = App()
        app.mainloop()


class RootUser(App):
    def __init__(self):
        self.data = db()
        padding = 10
        super().__init__()
        self.btn_login.grid_forget()
        self.frm_other_buttons = customtkinter.CTkFrame(self.frm_left)
        self.frm_other_buttons.grid(row=1)
        self.btn_insert = customtkinter.CTkButton(
            self.frm_other_buttons,
            text="Add records",
            command=lambda: self.openInsert(),
        )
        self.btn_insert.grid(row=0, pady=padding / 4)

        self.btn_delete = customtkinter.CTkButton(
            self.frm_other_buttons,
            text="Delete records",
            command=lambda: self.openDelete(),
        )
        self.btn_delete.grid(row=1, pady=padding / 4)

        self.btn_update = customtkinter.CTkButton(
            self.frm_other_buttons,
            text="Update records",
            command=lambda: self.openUpdate(),
        )
        self.btn_update.grid(row=2, pady=padding / 4)

        self.btn_logout = customtkinter.CTkButton(
            self.frm_other_buttons,
            text="logout",
            command=lambda: self.openMain(),
        )
        self.btn_logout.grid(row=3, pady=padding / 4)

        self.btn_refresh = customtkinter.CTkButton(
            self.frm_other_buttons,
            text="Refresh records",
            command=lambda: self.deleteWidgets(),
        )
        self.btn_refresh.grid(row=4, pady=padding / 4)

    def deleteWidgets(self):
        for i in self.frm_records.winfo_children():
            i.destroy()
        # self.records(
        #         self.frm_display_result,
        #         "ID",
        #         "name",
        #         "diagnosis",
        #         "prescription",
        #         "description",
        #         1,
        #     )
        self.displayRecords()

    def openInsert(self):
        newWindow = InsertWindow()
        newWindow.mainloop()

    def openDelete(self):
        delete = DeleteWindow()
        delete.mainloop()

    def openUpdate(self):
        delete = UpdateWindow()
        delete.mainloop()

    def openMain(self):
        self.destroy()
        app = App()
        app.mainloop()


class InsertWindow(customtkinter.CTk):
    def __init__(self):
        self.data = db()
        padding = 10
        super().__init__()
        self.title("add records")
        self.resizable(0, 0)

        self.columnconfigure(0, weight=1)
        self.frm_main = customtkinter.CTkFrame(self)
        self.frm_main.grid(row=0, column=0, padx=padding, pady=padding, sticky="nsew")
        self.lbl_name = customtkinter.CTkLabel(self.frm_main, text="Name: ")
        self.ent_name = customtkinter.CTkEntry(self.frm_main)
        self.lbl_diagnosis = customtkinter.CTkLabel(self.frm_main, text="Diagnosis: ")
        self.ent_diagnosis = customtkinter.CTkEntry(self.frm_main)
        self.lbl_prescription = customtkinter.CTkLabel(
            self.frm_main, text="Prescription: "
        )
        self.frm_main.columnconfigure(0, weight=0)
        self.frm_main.columnconfigure(1, weight=1)
        self.ent_prescription = customtkinter.CTkEntry(self.frm_main)
        self.lbl_description = customtkinter.CTkLabel(
            self.frm_main, text="Description: "
        )
        self.ent_description = customtkinter.CTkEntry(self.frm_main)
        self.lbl_name.grid(row=0, column=0, pady=padding / 4, sticky="w")
        self.lbl_diagnosis.grid(row=1, column=0, pady=padding / 4, sticky="w")
        self.lbl_prescription.grid(row=2, column=0, pady=padding / 4, sticky="w")
        self.lbl_description.grid(row=3, column=0, pady=padding / 4, sticky="w")
        self.ent_name.grid(row=0, column=1, pady=padding / 4)
        self.ent_diagnosis.grid(row=1, column=1, pady=padding / 4)
        self.ent_prescription.grid(row=2, column=1, pady=padding / 4)
        self.ent_description.grid(row=3, column=1, pady=padding / 4)
        self.btn_add = customtkinter.CTkButton(
            self.frm_main, text="add record", command=lambda: self.add()
        )
        self.btn_add.grid(row=4, pady=padding / 2, columnspan=2)

        self.btn_done = customtkinter.CTkButton(
            self.frm_main, text="done", command=lambda: self.destroy()
        )
        self.btn_done.grid(row=10, pady=padding / 2, columnspan=2)

    def add(self):
        try:
            if self.ent_name.get() == "":
                raise ValueError("value cannot be black")
            self.data.insertTo(
                self.ent_name.get(),
                self.ent_diagnosis.get(),
                self.ent_prescription.get(),
                self.ent_description.get(),
            )
            self.lbl_err = customtkinter.CTkLabel(
                self.frm_main, text="SUCCESS", text_color="green"
            )
            self.lbl_err.grid(row=5, columnspan=2)
            self.ent_name.delete("0", "end")
            self.ent_diagnosis.delete("0", "end")
            self.ent_prescription.delete("0", "end")
            self.ent_description.delete("0", "end")
            timeout = Timer(1.0, lambda: self.lbl_err.grid_forget())
            timeout.start()
        except:
            self.lbl_err = customtkinter.CTkLabel(
                self.frm_main, text="ERROR", text_color="red"
            )
            self.lbl_err.grid(row=5, columnspan=2)
            timeout = Timer(2.0, lambda: self.lbl_err.grid_forget())
            timeout.start()


class DeleteWindow(customtkinter.CTk):
    def __init__(self):
        padding = 10
        super().__init__()
        self.data = db()
        self.resizable(0, 0)
        self.title("delete records")
        self.frm_main = customtkinter.CTkFrame(self)
        self.frm_main.grid(row=0, column=0, pady=padding, padx=padding)
        self.lbl_label = customtkinter.CTkLabel(self.frm_main, text="Enter patient ID:")
        self.lbl_label.grid(row=0, padx=padding / 4, pady=padding / 4)
        self.ent_id = customtkinter.CTkEntry(self.frm_main)
        self.ent_id.grid(row=1, padx=padding / 4, pady=padding / 4)
        self.btn_delete = customtkinter.CTkButton(
            self.frm_main,
            text="Delete record",
            command=lambda: self.deleteAction(self.ent_id.get()),
        )
        self.btn_delete.grid(row=2, padx=padding / 4, pady=padding / 4)

    def deleteAction(self, id):
        try:
            if self.data.select(id) == []:
                raise ValueError("Out of Index")
            self.data.deleteWithID(id)
            self.lbl_err = customtkinter.CTkLabel(
                self.frm_main, text="RECORD DELETED", text_color="green"
            )
            self.lbl_err.grid(row=5)
            timeout = Timer(2.0, lambda: self.lbl_err.grid_forget())
            timeout.start()
        except:
            self.lbl_err = customtkinter.CTkLabel(
                self.frm_main, text="ERROR", text_color="red"
            )
            self.lbl_err.grid(row=5)
            timeout = Timer(2.0, lambda: self.lbl_err.grid_forget())
            timeout.start()


class UpdateWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.data = db()
        self.resizable(0, 0)
        self.title("update records")
        self.columnconfigure(0, weight=1)
        padding = 10
        self.frm_main = customtkinter.CTkFrame(self)
        self.frm_main.columnconfigure(0, weight=1)

        self.frm_main.grid(row=0, column=0, padx=padding, pady=padding, sticky="nsew")
        self.ent_id = customtkinter.CTkEntry(
            self.frm_main, placeholder_text="Enter patient ID"
        )
        self.ent_id.grid(row=1, columnspan=2, pady=padding, sticky="ew")
        self.btn_id = customtkinter.CTkButton(
            self.frm_main,
            text="See current record with the ID#",
            command=lambda: self.chooseIdToDisplay(self.ent_id.get()),
        )
        self.btn_id.grid(row=2, columnspan=2, pady=padding, sticky="ew")

        self.frm_entries = customtkinter.CTkFrame(self)
        self.frm_entries.grid(row=1, column=0, padx=padding, pady=padding, columnspan=2)

    def chooseIdToDisplay(self, id):
        padding = 10
        try:
            result = self.data.select(id)
            if result == []:
                raise ValueError("out of range")
        except:
            self.lbl_err = customtkinter.CTkLabel(
                self.frm_entries, text="ERROR", text_color="red"
            )
            self.lbl_err.grid(row=5, columnspan=2)
            timeout = Timer(2.0, lambda: self.lbl_err.grid_forget())
            timeout.start()

        self.lbl_name = customtkinter.CTkLabel(self.frm_entries, text="Name:")
        self.ent_name = customtkinter.CTkEntry(self.frm_entries)
        self.ent_name.insert("1", result[0][1])

        self.lbl_diagnosis = customtkinter.CTkLabel(self.frm_entries, text="Diagnosis:")
        self.ent_diagnosis = customtkinter.CTkEntry(self.frm_entries)
        self.ent_diagnosis.insert("1", result[0][2])

        self.lbl_prescription = customtkinter.CTkLabel(
            self.frm_entries, text="Prescription:"
        )
        self.ent_prescription = customtkinter.CTkEntry(self.frm_entries)
        self.ent_prescription.insert("1", result[0][3])

        self.lbl_description = customtkinter.CTkLabel(
            self.frm_entries, text="Description:"
        )
        self.ent_description = customtkinter.CTkEntry(self.frm_entries)
        self.ent_description.insert("1", result[0][4])

        self.lbl_name.grid(row=0, column=0, sticky="w")
        self.ent_name.grid(row=0, column=1, padx=padding / 4, pady=padding / 4)

        self.lbl_diagnosis.grid(row=1, column=0, sticky="w")
        self.ent_diagnosis.grid(row=1, column=1, padx=padding / 4, pady=padding / 4)

        self.lbl_prescription.grid(row=2, column=0, sticky="w")
        self.ent_prescription.grid(row=2, column=1, padx=padding / 4, pady=padding / 4)

        self.lbl_description.grid(row=3, column=0, sticky="w")
        self.ent_description.grid(row=3, column=1, padx=padding / 4, pady=padding / 4)

        self.btn_update = customtkinter.CTkButton(
            self.frm_entries,
            text="update",
            command=lambda: self.updateAction(),
        )
        self.btn_update.grid(row=4, columnspan=2)

    def updateAction(self):
        try:
            self.data.update(
                self.ent_id.get(),
                self.ent_name.get(),
                self.ent_diagnosis.get(),
                self.ent_prescription.get(),
                self.ent_description.get(),
            )
            self.lbl_err = customtkinter.CTkLabel(
                self.frm_entries, text="RECORD UPDATED", text_color="green"
            )
            self.lbl_err.grid(row=5, columnspan=2)
            timeout = Timer(2.0, lambda: self.lbl_err.grid_forget())
            timeout.start()
        except:
            self.lbl_err = customtkinter.CTkLabel(
                self.frm_entries, text="ERROR", text_color="red"
            )
            self.lbl_err.grid(row=5, columnspan=2)
            timeout = Timer(2.0, lambda: self.lbl_err.grid_forget())
            timeout.start()


if __name__ == "__main__":
    app = App()
    app.mainloop()
