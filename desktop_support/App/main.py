from App.Auth import login, reg
from tkinter import *
import tkinter as tk

LARGE_FONT = ("Verdana", 12)


class Main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.parent.geometry("600x600")
        self.parent.title("Third Eye")
        self.label = tk.Label(self, text="Tech Eye", font=LARGE_FONT)
        self.label.pack()
        self.button1 = Button(self.parent, text="Admin Login", command=self.login).place(x=130, y=300)
        self.button2 = Button(self.parent, text="Admin Registration", command=self.reg).place(x=260, y=300)
        self.button3 = Button(self.parent, text="Exit", command=self.parent.destroy).place(x=220, y=350)

    def reg(self):
        self.parent.destroy()
        new = tk.Tk()
        st = reg.Registration(new)
        st.mainloop()

    def login(self):
        self.parent.destroy()
        new = tk.Tk()
        st = login.Login(new)
        st.mainloop()
#
# CREATE TABLE `User` (
#   `id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
#   `Name` varchar(255) NOT NULL,
#   `Username` int(255) NOT NULL,
#   `admin_id` int(100) NOT NULL,
#   `email` varchar(255) NOT NULL,
#   `password` varchar(30) NOT NULL
# ) ENGINE=InnoDB DEFAULT CHARSET=latin1;


if __name__ == '__main__':
    root = tk.Tk()
    run = Main(root)
    run.mainloop()
