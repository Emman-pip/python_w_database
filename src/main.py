import tkinter as tk
from tkinter import ttk
from db import *
import os
import sys
from threading import Timer

# TODO: see if it is possible to show all in a text bo so it will be scrollable


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Medical Database App")
        # self.rowconfigure(0, weight=100)
        # self.columnconfigure(0, weight=100)

        # self.geometry("500x200")
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
            if height != None:
                self.frame = ttk.Frame(masterFrame, height=height)
                return self.frame
            self.frame = ttk.Frame(masterFrame)

        else:
            self.frame = ttk.Frame(self)
        self.frame.pack()
        return self.frame

    def createLabel(
        self, text="sometext", masterFrame=None, bwidth=None, relief=None, pack=None
    ):
        if masterFrame != None:
            self.label = ttk.Label(masterFrame, padding=5)
        else:
            self.label = ttk.Label(self)
        self.label["text"] = f"{text}"
        if bwidth != None and relief != None:
            self.label["borderwidth"] = bwidth
            self.label["relief"] = relief
        if pack != None:
            self.label.pack()

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

    # def createScrollbar(self, frame):
    #     self.scrollbar = ttk.Scrollbar(frame, orient="vertical")
    #     self.scrollbar.grid(row=0, column=100, sticky=tk.NS, rowspan=5)
    #     # self.scrollbar.pack(side="right", fill="y")
    #     return self.scrollbar

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

    def restart(self):
        os.execl(sys.executable, sys.executable, *sys.argv)


class loginWindow(App):
    def __init__(self):
        super().__init__()
        self.title("LOGIN PAGE")
        frm = self.createFrame()
        frm.pack()
        user = self.username = self.createEntry("username")
        password = self.password = self.createEntry("password")
        # label = lambda: self.printthis()
        self.login = self.createButton(lambda: self.printthis(), "log in")
        # login.show = "*"
        # back = self.createButton(lambda: launchMainApp(self), "go back")
        back = self.createButton(lambda: self.restart(), "go back")
        user.pack()
        password.pack()
        self.login.pack()

    def printthis(self):
        if self.username.get() == "root" and self.password.get() == "root":
            self.destroy()
        # print(
        #     f"username: {self.username.get()}\npassword:{self.password.get()}\nLOGGEDIN!"
        # )
        text = self.createLabel("Invalid credentials")
        text["foreground"] = "red"
        text.pack()
        disappearingText = Timer(1.0, lambda: text.pack_forget())
        disappearingText.start()

        # pass


class mainWindow(App):
    def __init__(self):
        super().__init__()
        # top components
        self.frm1 = self.createFrame()
        self.someHospital = self.createLabel("Some Hospital", self.frm1)
        self.patientRecLabel = self.createLabel("Patient records", self.frm1)
        self.someHospital.pack()
        self.patientRecLabel.pack()

        btn = self.createButton(
            lambda: launchLogin(self),
            "Add/Remove/update Data",
            self.frm1,
        )

        # main screen components
        self.frm2 = self.createFrame()
        # self.frm2.height = 2
        # scroll = self.createScrollbar(self.frm2)
        # self.frm2.yscrollcommand = scroll.set

        data = selectAll()
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
        for i in data:
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


def launchLogin(self):
    self.destroy()
    app = loginWindow()
    app.mainloop()


def launchMainApp(self):
    self.destroy()
    app = mainWindow()
    app.mainloop()


if __name__ == "__main__":
    app = mainWindow()
    app.mainloop()
