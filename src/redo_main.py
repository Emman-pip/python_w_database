import tkinter
from typing import Optional, Tuple, Union
import customtkinter
import tkinter.messagebox

customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("dark")
customtkinter.deactivate_automatic_dpi_awareness()

padding = 10


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # self.geometry("1000x750")
        self.title("Hospital Records")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.frm_left = customtkinter.CTkFrame(self, border_color="dark_color")
        self.frm_left.grid(
            row=0, column=0, padx=padding, pady=padding, sticky="ns", columnspan=1
        )
        # self.frm_left.columnconfigure(0, weight=0)

        self.frm_records = customtkinter.CTkFrame(self, border_color="dark_color")
        # self.frm_records.columnconfigure(0, weight=1)
        self.frm_records.grid(
            row=0, column=1, padx=padding, pady=padding, sticky="nsew", columnspan=3
        )

        self.btn_someButton = customtkinter.CTkButton(self.frm_left, text="click me")
        self.btn_someButton.grid(row=0, pady=padding, padx=padding)


if __name__ == "__main__":
    app = App()
    app.mainloop()
