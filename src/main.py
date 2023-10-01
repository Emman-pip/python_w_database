import tkinter as tk
from tkinter import ttk
from db import *

# TODO:  select a database to use
# TODO:  integrate the database to the gui


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Medical Database App")
        # self.geometry("500x500")
        # # TO put function as a parameter
        # self.lol = lambda: self.createFrame("red")
        # self.createButton(lambda: self.createEntry(), "click?")

    # def createFrame(self, bgColor, height=None, width=None):
    #     self.frame = ttk.Frame(bg=bgColor)
    #     if height != None and width != None:
    #         self.frame["height"] = height
    #         self.frame["width"] = width
    #     self.frame.pack()

    def createFrame(self, masterFrame=None):
        if masterFrame != None:
            self.frame = ttk.Frame(masterFrame)
        else:
            self.frame = ttk.Frame(self)
        self.frame.pack()
        return self.frame

    def createLabel(self, text="sometext", masterFrame=None, bwidth=None, relief=None):
        if masterFrame != None:
            self.label = ttk.Label(masterFrame, padding=5)
        else:
            self.label = ttk.Label(self)
        self.label["text"] = f"{text}"
        if bwidth != None and relief != None:
            self.label["borderwidth"] = bwidth
            self.label["relief"] = relief

        # needs to be positioned
        return self.label

    def createButton(self, command, itext="click me", masterFrame=None):
        if masterFrame != None:
            self.button = ttk.Button(masterFrame)
        else:
            self.button = ttk.Button(self)
        self.button["command"] = command
        self.button["text"] = itext
        self.button.pack()
        return self.button

    def createEntry(self, ltext="label", masterFrame=None):
        if masterFrame != None:
            self.frame = ttk.Frame(masterFrame)
        else:
            self.frame = ttk.Frame(self)
        self.frame.pack()
        self.label = self.label = ttk.Label(self.frame, text=f"{ltext}:")
        self.label.pack(side="left")
        self.entry = ttk.Entry(self.frame, width=30)
        self.entry.pack(side="right")
        return self.entry


class loginWindow(App):
    def __init__(self):
        super().__init__()
        self.createFrame()
        self.username = self.createEntry("username")
        self.password = self.createEntry("password")
        label = lambda: self.printthis()
        login = self.createButton(label, "log in")

    def printthis(self):
        print(
            f"username: {self.username.get()}\npassword:{self.password.get()}\nLOGGEDIN!"
        )


class mainWindow(App):
    def __init__(self):
        super().__init__()
        self.frm1 = self.createFrame()
        self.someHospital = self.createLabel("Some Hospital", self.frm1)
        self.patientRecLabel = self.createLabel("Patient records", self.frm1)
        self.someHospital.pack()
        self.patientRecLabel.pack()

        self.frm2 = self.createFrame()
        self.frm2.highlightbackground = "blue"
        self.frm2.highlightthickness = 2
        self.data = selectAll()
        padding = [7]
        bwidth = 1
        idLabel = self.createLabel("ID", self.frm2, 2, "solid")
        nameLabel = self.createLabel("NAME", self.frm2, 2, "solid")
        diagnosisLabel = self.createLabel("DIAGNOSIS", self.frm2, 2, "solid")
        prescriptionLabel = self.createLabel("PRESCRIPTION", self.frm2, 2, "solid")
        descriptionLabel = self.createLabel("DESCRIPTION", self.frm2, 2, "solid")

        idLabel.grid(column=0, row=0)
        nameLabel.grid(column=1, row=0)
        diagnosisLabel.grid(column=2, row=0)
        prescriptionLabel.grid(column=3, row=0)
        descriptionLabel.grid(column=4, row=0)
        for i in self.data:
            id = self.createLabel(i[0], self.frm2)
            name = self.createLabel(i[1], self.frm2)
            diagnosis = self.createLabel(i[2], self.frm2)
            prescription = self.createLabel(i[3], self.frm2, 1)
            description = self.createLabel(i[4], self.frm2, 1)

            # print(i[0], i[1], i[2], i[3], i[4])
            id.grid(column=0, row=i[0] + 1)
            name.grid(column=1, row=i[0] + 1)
            diagnosis.grid(column=2, row=i[0] + 1)
            prescription.grid(column=3, row=i[0] + 1)
            description.grid(column=4, row=i[0] + 1)


def welcomeWindow():
    app = App()

    app.mainloop()


if __name__ == "__main__":
    app = mainWindow()
    app.mainloop()
