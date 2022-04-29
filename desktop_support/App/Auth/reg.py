import random
from tkinter import *
from tkinter import messagebox, simpledialog
from App.Database.database_connection import *
import tkinter as tk
from App import main
from App.Mail.mail import Mail
from App.Security import Security as Sec


class Registration(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.password = StringVar()
        self.parent.geometry("600x600")
        self.parent.title("Registration")
        self.regLabel = Label(self.parent, text="Registration").place(x=210, y=40)
        self.name = Label(self.parent, text="Name").place(x=130, y=150)
        self.username = Label(self.parent, text="Username").place(x=130, y=190)
        self.admin_id = Label(self.parent, text="Admin ID").place(x=130, y=230)
        self.email = Label(self.parent, text="Email").place(x=130, y=270)
        self.passLabel = Label(self.parent, text="Password").place(x=130, y=310)
        self.e1 = Entry(self.parent)
        self.e1.place(x=210, y=150)
        self.e2 = Entry(self.parent)
        self.e2.place(x=210, y=190)
        self.e3 = Entry(self.parent)
        self.e3.place(x=210, y=230)
        self.e4 = Entry(self.parent)
        self.e4.place(x=210, y=270)
        self.e5 = Entry(self.parent, textvariable=self.password, show='*')
        self.e5.place(x=210, y=310)
        self.wait_label = Label(self.parent, text="")
        self.wait_label.place(x=130, y=400)
        self.submit = Button(self.parent, text="Submit", command=self.reg_do).place(x=130, y=350)
        self.cancel = Button(self.parent, text="back", command=self.close_window).place(x=290, y=350)
        self.pack()

    def close_window(self):
        self.parent.destroy()
        new = tk.Tk()
        st = main.Main(new)
        st.mainloop()

    def mail_do(self, name, mail):
        mail1 = Mail()
        m = mail1.auth_mail(name, mail)
        return m

    def reg_do(self):
        na = self.e1.get()
        un = self.e2.get()
        ai = self.e3.get()
        em = self.e4.get()
        p = self.password.get()

        if na and un and ai and em and p:
            db = Database()
            db1 = db.db_connect()
            if db1[0] and db1[1] and db1[2]:
                auth_verify = self.mail_do(na, em)
                use_inp = simpledialog.askstring(title="verification",
                                                 prompt="please type the email verification number: ")
                if auth_verify == use_inp:
                    print("verified")
                else:
                    print("not verified")

                mydb = mysql.connector.connect(
                    host="127.0.0.1",
                    user=db1[0],
                    password=db1[1],
                    database=db1[2]
                )
                cursor = mydb.cursor()
                sql = "INSERT INTO User (Name, Username, admin_id, email, password) VALUES (%s, %s, %s, %s, %s)"
                val = (na, un, ai, em, Sec.encrypt_password(p))
                cursor.execute(sql, val)
                print(mydb.commit())
                cursor.close()
                mydb.close()

            else:
                messagebox.showerror("Error", "Something wrong with your MySQL username or password, want to create "
                                              "user?")

        else:
            messagebox.showerror("Error", "Please fill up all information")


if __name__ == '__main__':
    root = tk.Tk()
    run = Registration(root)
    run.mainloop()
