import tkinter as tk
from tkinter import ttk

# TODO:  select a database to use
# TODO:  integrate the database to the gui


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Medical Database App")
        self.geometry("500x500")
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

    def createLabel(self, text="sometext", masterFrame=None):
        if masterFrame != None:
            self.label = ttk.Label(masterFrame)
        else:
            self.label = ttk.Label(self)
        self.label["text"] = f"{text}"
        self.label.pack()

    def createButton(self, command, itext="click me", masterFrame=None):
        if masterFrame != None:
            self.button = ttk.Button(masterFrame)
        else:
            self.button = ttk.Button(self)
        self.button["command"] = command
        self.button["text"] = itext
        self.button.pack()

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


def welcomeWindow():
    app = App()

    app.mainloop()


if __name__ == "__main__":
    app = loginWindow()
    app.mainloop()
