from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import sqlite3



class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        # self.root.iconbitmap("logo.ico")
        self.root.geometry("1350x780+0+0")
        self.root.minsize(850, 500)

        self.ent_username = StringVar()
        self.ent_password = StringVar()

        # ==============  All Images ==============
        self.bg_icon = ImageTk.PhotoImage(file="images/bg.jpg")
        self.user_icon = ImageTk.PhotoImage(file="images/icons8-user-male-26.png")
        self.pass_icon = ImageTk.PhotoImage(file="images/icons8-forgot-password-26.png")
        self.placeholder_icon = ImageTk.PhotoImage(file="images/placeholder.png")
        bg_lbl = Label(self.root, image=self.bg_icon).pack()
        title = Label(self.root, text="Login System", font=("times new roman", 30, 'bold'), relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        login_frame = Frame(self.root, bg='white', pady=20)
        login_frame.place(in_=root, anchor="c", relx=.5, rely=.5)

        logo_label = Label(login_frame, image=self.placeholder_icon, heigh=100, width=100).grid(row=0, columnspan=2, pady=20)

        user_name_label = Label(login_frame, image=self.user_icon, text="Username", compound=LEFT, font=("times new roman", 20, "bold"), bg='white').grid(row=1, column=0, padx=20, pady=10)
        ent_username = Entry(login_frame, textvariable=self.ent_username, bd=5, relief=GROOVE).grid(row=1, column=1, padx=10)

        password_label = Label(login_frame, image=self.pass_icon, text= "Password", compound=LEFT, font=("times new roman", 20, "bold"), bg='white').grid(row=2, column=0, padx=20, pady=10)
        ent_password = Entry(login_frame, textvariable=self.ent_password, bd=5, relief=GROOVE).grid(row=2, column=1, padx=10)

        btn_register = Button(login_frame, text="Register", bg='red', fg='white', pady=5, width=10).grid(row=3, column=0, pady=10)
        btn_login = Button(login_frame, text="Login", bg='green', fg='white', pady=5, width=20, command=self.login).grid(row=3, column=1, pady=10)

    def login(self):
        print(self.ent_username.get())
        print(self.ent_password.get())
        if self.ent_username.get() == "" or self.ent_password.get() == "":
            messagebox.showerror("Error", "All field required.")
        else:
            sql_select_query = """select * from users"""
            conn = sqlite3.connect("test.sqlite")
            cur = conn.cursor()
            cur.execute(sql_select_query)
            records = cur.fetchall()
            for r in records:
                print(r)
            cur.close()
        # print(self.username)


root = Tk()
login = LoginSystem(root)
root.mainloop()
