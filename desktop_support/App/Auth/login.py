from tkinter import *
from tkinter import messagebox
import mysql.connector
from App.Security import Security as sec
import tkinter as tk
from App import main
import time
from App.Database.database_connection import *


class Login(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.password = StringVar()
        self.parent.geometry("600x600")
        self.parent.title("Login")
        self.loginLabel = Label(self.parent, text="Login").place(x=210, y=40)
        self.username = Label(self.parent, text="Username").place(x=130, y=150)
        self.passLabel = Label(self.parent, text="Password").place(x=130, y=190)
        self.wait_label = Label(self.parent, text="")
        self.wait_label.place(x=130, y=360)
        self.e2 = Entry(self.parent)
        self.e2.place(x=210, y=150)
        self.e5 = Entry(self.parent, textvariable=self.password, show='*').place(x=210, y=190)
        self.submit = Bu
        tton(self.parent, text="Submit", command=self.pass_show).place(x=130, y=230)
        self.cancel = Button(self.parent, text="back", command=self.close_window).place(x=290, y=230)
        self.pack()

    def close_window(self):
        self.parent.destroy()
        new = tk.Tk()
        st = main.Main(new)
        st.mainloop()

    def pass_show(self):
        self.wait_label.config(text="Checking ....")
        self.wait_label.update_idletasks()
        time.sleep(1)
        u = self.e2.get()
        p = self.password.get()
        if u and p:
            db = Database()
            db1 = db.db_connect()
            if db1[0] and db1[1] and db1[2]:
                mydb = mysql.connector.connect(
                    host="127.0.0.1",
                    user=db1[0],
                    password=db1[1],
                    database=db1[2]
                )
                cursor = mydb.cursor()
                q = "SELECT * FROM User WHERE Username = %s"
                cursor.execute(q, (u,))
                my_result = cursor.fetchall()
                if my_result:
                    s = sec.check_encrypted_password(p, my_result[0][5])
                    if s:
                        messagebox.showinfo("Information", "successfully logged in. redirected to Dashboard")

                    else:
                        messagebox.showerror("Error", "Password not matched! please try again")
                else:
                    messagebox.showerror("Error", "Username not found :( are you registered?")
                cursor.close()
                mydb.close()

            else:
                messagebox.showerror("Error", "Something wrong with your MySQL username or password, want to create "
                                              "user?")

        else:
            if u:
                self.wait_label.config(text="you didn't provide your password")
            elif p:
                self.wait_label.config(text="you didn't provide your username")
            else:
                self.wait_label.config(text="you didn't provide username & password")


if __name__ == '__main__':
    root = tk.Tk()
    run = Login(root)
    run.mainloop()
