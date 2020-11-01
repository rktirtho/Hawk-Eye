import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import sqlite3
import emp_db_helper
from object_model import *


LARGEFONT = ("Verdana", 30)
MEDIAMFONT = ("Verdana", 20)
SMALLFONT = ("Verdana", 16)




class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.BGIMAGE = ImageTk.PhotoImage(file="images/meterial/bg.jpg")
        logo_label = Label(self, image=self.BGIMAGE).grid(row=0, column=2)

        # creating a container
        container = Frame(self)

        container.place(in_=self, anchor="c", relx=.5, rely=.5)

        # container.pack(side="top", fill="both", expand=True)
        #
        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (StartPage, Register):
            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage, "Login")

        # to display the current frame passed as

    # parameter
    def show_frame(self, cont, page):
        self.title(page)
        frame = self.frames[cont]
        frame.tkraise()

    # first window frame startpage


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        self.ent_username = StringVar()
        self.ent_password = StringVar()
        tk.Frame.__init__(self, parent)
        # label of frame Layout 2
        label = ttk.Label(self, text="Login", font=MEDIAMFONT).grid(row=0, column=0, columnspan=2, pady=20)
        # ===== User name Section ======
        lb_user = ttk.Label(self, text="Username").grid(row=1, column=0)
        ent_user = ttk.Entry(self,textvariable=self.ent_username).grid(row=1, column=1)

        # ===== Password Section ======
        lb_pass = ttk.Label(self, text="Password").grid(row=2, column=0)
        ent_pass = ttk.Entry(self,show="*",textvariable=self.ent_password).grid(row=2, column=1, pady=10)

        button1 = Button(self, bg='red', fg='white', text="Register",width=20, command=lambda: controller.show_frame(Register, "Register"))

        # putting the button in its place by
        # using grid
        button1.grid(row=3, column=0, padx=10, pady=10)

        button2 = Button(self, bg='green', fg='white', width=20,text="Login", command=self.login).grid(row=3, column=1, padx=10, pady=10)

    # second window frame page1
    def login(self):
        if self.ent_username.get() == "" or self.ent_password.get() == "":
            messagebox.showerror("Error", "All field required.")
        else:
            records = emp_db_helper.login(self.ent_username.get(), self.ent_password.get())
            if len(records) > 0:
                print("login success")
                messagebox.showinfo("Login Success", "Your Login is has success")
            else:
                print("Denied")
                messagebox.showerror("Login in Failed", "Username or password mismatch. Try Again.")


# class Page1(tk.Frame):
#
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = ttk.Label(self, text="Page 1", font=LARGEFONT,justify='center')
#         label.grid(row=0, column=4, padx=10, pady=10)
#
#         # button to show frame 2 with text
#         # layout2
#         button1 = ttk.Button(self, text="StartPage",
#                              command=lambda: controller.show_frame(StartPage))
#
#         # putting the button in its place
#         # by using grid
#         button1.grid(row=1, column=1, padx=10, pady=10)
#
#         # button to show frame 2 with text
#         # layout2
#         button2 = ttk.Button(self, text="Page 2",
#                              command=lambda: controller.show_frame(Page2))
#
#         # putting the button in its place by
#         # using grid
#         button2.grid(row=2, column=1, padx=10, pady=10)
#
#     # third window frame page2


class Register(tk.Frame):
    def __init__(self, parent, controller):
        self.emp_id= StringVar()
        self.controller =  controller
        self.username = StringVar()
        self.password = StringVar()
        self.conf_pass = StringVar()
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Registration", font=MEDIAMFONT)
        label.grid(row=0, column=0, columnspan=2, pady=20)

        lb_em_id = ttk.Label(self, text="Employee Id").grid(row=1, column=0, padx=20, pady=10,sticky=W)
        ent_id = ttk.Entry(self,  textvariable=self.emp_id,).grid(row=1, column=1, padx=10)
        user_name_label = ttk.Label(self, text="Username").grid(row=2, column=0, padx=20, pady=10,sticky=W)
        ent_username = ttk.Entry(self,  textvariable=self.username).grid(row=2, column=1, padx=10)

        # ====================== password Field ===============
        lb_pass = ttk.Label(self, text="Password", anchor="e").grid(row=3, column=0, padx=20, pady=10,sticky=W)
        ent_pass = ttk.Entry(self, show='*', textvariable=self.password).grid(row=3, column=1, padx=10)
        # ======================= Confirm Password Field===================
        lb_conf_pass = ttk.Label(self,  text="Confirm Password").grid(row=4, column=0, padx=20, pady=10,sticky=W)
        ent_conf_pass = ttk.Entry(self, show='*', textvariable=self.conf_pass).grid(row=4, column=1, padx=10)
        # ========================= Button Section =======================

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text="Login",
                             command=lambda: controller.show_frame(StartPage, "Login"), width=20)

        # putting the button in its place by
        # using grid
        button1.grid(row=10, column=0, pady=10, padx=10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, command=self.registration, text="Registration",width=20)

        # putting the button in its place by
        # using grid
        button2.grid(row=10, column=1)

    def registration(self):
        emp_id = self.emp_id.get()
        username = self.username.get()
        password = self.password.get()
        conf_pass = self.conf_pass.get()

        emp = Employee(int(emp_id),"Ashik", username,"test@test.app", password)

        if emp_id=="" or username == "" or password == "" or conf_pass == "":
            messagebox.showerror("Error", "All Field Required")
        elif password != conf_pass:
            messagebox.showerror("Error", "Password should match")
        else:
            self.emp_id.set("")
            self.username.set("")
            self.password.set("")
            self.conf_pass.set("")
            emp_db_helper.insert(emp)
            messagebox.showinfo("Done")
            self.controller.show_frame(StartPage, "Login")





    # Driver Code


app = tkinterApp()
app.title("Login")
app.minsize(800, 500)
app.maxsize(800, 500)
app.mainloop()
