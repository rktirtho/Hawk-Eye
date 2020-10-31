from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import sqlite3


class Register:
    def __init__(self, root):
        self.h1 = 20
        self.reg_text_size = 16
        self.root = root
        self.root.title("Registration")
        self.root.geometry("1350x780+0+0")
        self.emp_id = StringVar()
        self.username = StringVar()
        self.password = StringVar()
        self.conf_password = StringVar()

        # ==============  All Images ==============
        self.bg_icon = ImageTk.PhotoImage(file="images/bg.jpg")
        # self.user_icon = ImageTk.PhotoImage(file="")
        # self.pass_icon = ImageTk.PhotoImage(file="")
        self.placeholder_icon = ImageTk.PhotoImage(file="images/placeholder.png")
        bg_lbl = Label(self.root, image=self.bg_icon).pack()
        title = Label(self.root, text="Registration", font=("times new roman", self.h1, 'bold'), bg='yellow', fg='red', bd=10, relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        login_frame = Frame(self.root, bg='white', pady=20)
        login_frame.place(in_=root, anchor="c", relx=.5, rely=.5)

        logo_label = Label(login_frame, image=self.placeholder_icon, heigh=100, width=100).grid(row=0, columnspan=2, pady=20)

        # ====================== Employee Id Field ====================
        emp_id_name_label = Label(login_frame, text="Employee ID", compound=LEFT, font=("times new roman", self.reg_text_size, "bold"),
                                  bg='white').grid(row=1, column=0, padx=20, pady=10)
        ent_emp_id = Entry(login_frame, textvariable=self.emp_id, bd=5, relief=GROOVE).grid(row=1, column=1,
                                                                                              padx=10)

        # ===================== username Field ================
        user_name_label = Label(login_frame, text="Username", compound=LEFT, font=("times new roman", self.reg_text_size, "bold"), bg='white').grid(row=2, column=0, padx=20, pady=10)
        ent_username =  Entry(login_frame, textvariable=self.username, bd=5, relief=GROOVE).grid(row=2, column=1, padx=10)

        # ====================== password Field ===============
        password_label = Label(login_frame, text= "Password", compound=LEFT, font=("times new roman", self.reg_text_size, "bold"), bg='white').grid(row=3, column=0, padx=20, pady=10)
        ent_password = Entry(login_frame,textvariable=self.password, bd=5, relief=GROOVE).grid(row=3, column=1, padx=10)
        # ======================= Confirm Password Field===================
        password_confirm_label = Label(login_frame, text= "Confirm Password", compound=LEFT, font=("times new roman", self.reg_text_size, "bold"), bg='white').grid(row=4, column=0, padx=20, pady=10)
        ent_password_confirm = Entry(login_frame,textvariable=self.conf_password, bd=5, relief=GROOVE).grid(row=4, column=1, padx=10)
        # ========================= Button Section =======================
        btn_login = Button(login_frame, text="Login", bg='green', fg='white', pady=5, width=20,).grid(row=6, column=0, pady=10)

        btn_register = Button(login_frame, text="Register",command=self.register, bg='red', fg='white', pady=5, width=10).grid(row=6, column=1, pady=10)

    def register(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All field required.")
        elif self.password.get() != self.conf_password.get():
            messagebox.showerror("Password mismatched", "Both Password should same.")
        # print(self.username)
        conn = sqlite3.connect("test.sqlite")
        cur = conn.cursor()
        # cur.execute('CREATE TABLE users (id TEXT, username TEXT, name TEXT, password )')
        cur.execute('INSERT INTO users (id, username,password) VALUES (?,?,?)'
                    , (int(self.emp_id.get()), self.username.get(), self.password.get()))
        conn.commit()


root = Tk()
login = Register(root)
root.mainloop()
