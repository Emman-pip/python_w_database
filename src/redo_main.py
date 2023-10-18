import tkinter
from typing import Optional, Tuple, Union
import customtkinter
import tkinter.messagebox

customtkinter.set_default_color_theme("green")
customtkinter.set_appearance_mode("dark")
customtkinter.deactivate_automatic_dpi_awareness()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x750")
        self.title("Hospital Records")
        # self.frm_left = customtkinter.CTkFrame(self, )


if __name__ == "__main__":
    app = App()
    app.mainloop()
