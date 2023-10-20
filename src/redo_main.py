import tkinter
import customtkinter
import tkinter.messagebox

customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("dark")
customtkinter.deactivate_automatic_dpi_awareness()


class App(customtkinter.CTk):
    def __init__(self):
        padding = 10
        super().__init__()
        self.geometry("1000x270")
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
        self.btn_login = customtkinter.CTkButton(self.frm_left, text="login")
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
        self.btn_search = customtkinter.CTkButton(self.frm_search, text="search")
        self.btn_search.grid(row=1, column=0, pady=padding / 2)

        self.frm_records = customtkinter.CTkScrollableFrame(
            self.frm, border_color="dark_color", height=200
        )
        # self.frm_records.columnconfigure(1, pad=10)
        self.frm_records.columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.frm_records.grid(
            row=0,
            column=1,
            padx=padding,
            pady=padding,
            sticky="nsew",
            # columnspan=3,
        )

        # self.btn_someButton = customtkinter.CTkButton(self.frm_left, text="click me")
        # self.btn_someButton.grid(row=0, pady=padding, padx=padding)
        self.records(
            self.frm_records, "ID", "name", "diagnosis", "prescription", "description"
        )
        self.records(self.frm_records, 1, "John", "dead", "dead", "dead", 1)
        self.records(self.frm_records, 2, "Emman", "dead", "dead", "dead", 2)
        self.records(self.frm_records, 3, "Emman", "dead", "dead", "dead", 3)
        self.records(self.frm_records, 4, "Emman", "dead", "dead", "dead", 4)
        self.records(self.frm_records, 5, "Emman", "dead", "dead", "dead", 5)
        self.records(self.frm_records, 6, "Emman", "dead", "dead", "dead", 6)
        self.records(self.frm_records, 7, "Emman", "dead", "dead", "dead", 7)
        self.records(self.frm_records, 8, "Emman", "dead", "dead", "dead", 8)
        self.records(self.frm_records, 9, "Emman", "dead", "dead", "dead", 9)

    def records(self, master, id, name, diagnosis, prescription, description, row=0):
        padding = 20
        self.lbl_id = customtkinter.CTkLabel(master, text=id)
        self.lbl_name = customtkinter.CTkLabel(master, text=name)
        self.lbl_diagnosis = customtkinter.CTkLabel(master, text=diagnosis)
        self.lbl_prescription = customtkinter.CTkLabel(master, text=prescription)
        self.lbl_description = customtkinter.CTkLabel(master, text=description)
        # to be appplied with grid
        self.lbl_id.grid(column=0, row=row, sticky="ew", padx=padding)
        self.lbl_name.grid(column=1, row=row, sticky="ew", padx=padding)
        self.lbl_diagnosis.grid(column=2, row=row, sticky="ew", padx=padding)
        self.lbl_prescription.grid(column=3, row=row, sticky="ew", padx=padding)
        self.lbl_description.grid(column=4, row=row, sticky="ew", padx=padding)


if __name__ == "__main__":
    app = App()
    app.mainloop()
