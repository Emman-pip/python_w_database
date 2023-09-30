import tkinter as tk
from tkinter import ttk

# TODO:  select a database to use
# TODO:  integrate the database to the gui


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Medical Database App")
        self.geometry("500x500")
        # TO put function as a parameter
        # self.createButton(lambda: self.createLabel("YAHU"), "click?")

    def rawLabel(self, text):
        self.label = ttk.Label(self, text=f"{text}")
        self.label.pack()

    def createLabel(self, text="sometext"):
        self.rawLabel(text)

    def createButton(self, command, itext="click me"):
        self.button = ttk.Button(self, text=itext)
        self.button["command"] = command
        self.button.pack()

    # def button_clicked(self):
    #     self.label2 = ttk.Label(self, text="YOUCLICKED!!")
    #     self.label2.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
