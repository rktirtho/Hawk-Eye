import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
from dbh_emp import EmployeeDBHelper
import json
import requests
from dbh_organization import OrganizationDbHelper
from dbh_emp import EmployeeDBHelper
from dbh_person_reg import AuthorizedDbHelper



# import dbh_emp
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
        for F in (StartPage, Register, Dashboard):
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



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        self.emp_db_helper = EmployeeDBHelper()
        self.ent_username = StringVar()
        self.ent_password = StringVar()
        self.controller = controller
        tk.Frame.__init__(self, parent)

    def login(self):
        if self.ent_username.get() == "" or self.ent_password.get() == "":
            messagebox.showerror("Error", "All field required.")
        else:
            record = self.emp_db_helper.login(self.ent_username.get(), self.ent_password.get())
            if record:
                self.controller.show_frame(Dashboard, "Dashboard")
            else:
                messagebox.showerror("Login Failed.", "Invalid username or password.")

    def next_page(self):
        print("nextPage called")


class Dashboard(tk.Frame):
    def __init__(self, parent, controller,):
        tk.Frame.__init__(self, parent)
        menu_panel = PanedWindow(self,bg="gray")
        menu_panel.pack(fill=BOTH, expand=2)
        # Menu panel content
        left_label = Frame(menu_panel)
        menu_panel.add(left_label)
        # Add Person
        btn_add_per = Button(left_label, text="Add New Person", width=20)
        btn_add_per.pack(pady=5, padx=5)

        btn_Unauth_acc = Button(left_label, text="Unauthorized Access",  width=20)
        btn_Unauth_acc.pack(pady=5, padx=5)

        btn_auth_acc = Button(left_label, text="Authorized Access",  width=20)
        btn_auth_acc.pack(pady=5, padx=5)

        btn_all_emp = Button(left_label, text="Organizations", width=20)
        btn_all_emp.pack(pady=5, padx=5)

        btn_all_emp = Button(left_label, text="All Employee",  width=20)
        btn_all_emp.pack(pady=5, padx=5)

        btn_auth_person = Button(left_label, text="Authorized Person",  width=20)
        btn_auth_person.pack(pady=5, padx=5)

        btn_unknown_per = Button(left_label, text="Unknown Person",  width=20)
        btn_unknown_per.pack(pady=5, padx=5)

        content_panel = PanedWindow(menu_panel, orient=HORIZONTAL)

        menu_panel.add(content_panel)

        contend = Frame(content_panel, )

        content_panel.add(contend)

    # def clear_all(self):
    #     for widget in self.winfo_children():
    #         widget.destroy()
    #
    # def click(sefl, title):
    #     root.title(title)
    #
    # def show_all(sefl):
    #     click("All Person")
    #
    #     contend.pack_forget()
    #
    # def clearAll(sefl):
    #     for widget in contend.winfo_children():
    #         widget.destroy()
    #
    # def add_emp_frame(sefl):
        # content_panel.remove(contend)
        # clearAll()
        #
        # click("Add Employee")
        title = Label(contend, text="Add Person", font=MEDIAMFONT)
        title.pack(pady=20)

        lb_emp_id = Label(contend, text="Employee ID")
        lb_emp_id.pack()
        ent_em_id = Entry(contend, )
        ent_em_id.pack()

        lb_name = Label(contend, text="Employee Name*")
        lb_name.pack()
        ent_name = Entry(contend, )
        ent_name.pack()

        lb_org = Label(contend, text="Organization ID*")
        lb_org.pack()
        ent_org_id = Entry(contend, )
        ent_org_id.pack()

        Button(contend, text="Load Image*").pack(pady=10)
        Button(contend, text="Save").pack()
        # content_panel.add(contend)

    # def unauth_acc_wid(sefl):
    #     clearAll()
    #     click("Unauthorized Access")
    #     title = Label(contend, text="Unauthorized Access", font=MEDIAMFONT)
    #     title.pack(pady=20)
    #
    # def auth_acc_wid(sefl):
    #     clearAll()
    #     click("Authorized Access")
    #     title = Label(contend, text="Authorized Access", font=MEDIAMFONT)
    #     title.pack(pady=20)
    #     try:
    #         utr = requests.get('http://127.0.0.1:8080/api/organizations')
    #         api = json.loads(utr.content)
    #         for date in api:
    #             Label(contend, text=date['name']).pack()
    #         # print(api)
    #     except Exception as e:
    #         print("Loading Failed...")
    #
    # def all_auth_person_wid(sefl):
    #     clearAll()
    #     click("Authorized Access")
    #     title = Label(contend, text="Authorized Person", font=MEDIAMFONT)
    #     title.grid(row=0, column=0, columnspan=4, pady=20)
    #     auth_person = AuthorizedDbHelper()
    #     orgs = auth_person.find_all_details()
    #     i = 2
    #     c = 0
    #     print(orgs[1])
    #     Label(contend, text="#Id", padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=0, pady=10)
    #     Label(contend, text="Name", padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=1, pady=10)
    #     Label(contend, text='Organization', padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=2)
    #     # Label(contend, text='Address', padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=3)
    #     # Label(contend, text='Join Date', padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=4)
    #
    #     for org in orgs:
    #         Label(contend, text=org.get_id(), padx=20).grid(row=i, column=0, pady=10)
    #         Label(contend, text=org.get_name(), padx=20).grid(row=i, column=1, pady=10)
    #         Label(contend, text=org.get_organization(), padx=20).grid(row=i, column=2)
    #         # Label(contend, text=org.get_address(), padx=20).grid(row=i, column=3)
    #         # Label(contend, text=org.get_reg_time(), padx=20).grid(row=i, column=4)
    #         i += 1

    # def org_wid(sefl, contend):
    #     # clearAll()
    #     # click("Organizations")
    #     title = Label(contend, text="All Organization", font=MEDIAMFONT)
    #     title.grid(row=0, column=0, columnspan=4, pady=20)
    #     org = OrganizationDbHelper()
    #     orgs = org.find_all()
    #     i = 2
    #     c = 0
    #     print(orgs[1])
    #     Label(contend, text="#Id", padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=0, pady=10)
    #     Label(contend, text="Name", padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=1, pady=10)
    #     Label(contend, text='Woner', padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=2)
    #     Label(contend, text='Address', padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=3)
    #     Label(contend, text='Registration', padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=4)
    #
    #     for org in orgs:
    #         Label(contend, text=org.get_id(), padx=20).grid(row=i, column=0, pady=10)
    #         Label(contend, text=org.get_name(), padx=20).grid(row=i, column=1, pady=10)
    #         Label(contend, text=org.get_woner(), padx=20).grid(row=i, column=2)
    #         Label(contend, text=org.get_address(), padx=20).grid(row=i, column=3)
    #         Label(contend, text=org.get_reg_time(), padx=20).grid(row=i, column=4)
    #         i += 1

    # def all_emp_wid(sefl):
    #     clearAll()
    #     click("All Employee")
    #     title = Label(contend, text="All Registered Person", font=MEDIAMFONT)
    #     title.grid(column=1, row=0, pady=20)
    #     emp_helper = EmployeeDBHelper()
    #     persons = emp_helper.find_all()
    #     i = 2;
    #     c = 0
    #     Label(contend, text="#Id", padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=0, pady=10)
    #     Label(contend, text="Name", padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=1, pady=10)
    #     Label(contend, text='Email', padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=2)
    #     Label(contend, text='Address', padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=3)
    #     Label(contend, text='Join Data', padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=4)
    #
    #     for person in persons:
    #         Label(contend, text=person.get_id(), padx=20).grid(row=i, column=0, pady=10)
    #         Label(contend, text=person.get_name(), padx=20).grid(row=i, column=1, pady=10)
    #         Label(contend, text=person.get_email(), padx=20).grid(row=i, column=2)
    #         Label(contend, text=person.get_join_date(), padx=20).grid(row=i, column=3)
    #         # Label(contend, text=person.last_excess(), padx=20).grid(row=i, column=4)
    #         i += 1
    #
    # def unknown_person_wid(sefl):
    #     clearAll()
    #     click("Unknown Person")
    #     title = Label(contend, text="Unknown Person", font=MEDIAMFONT)
    #     title.pack(pady=20)


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


        button1 = ttk.Button(self, text="Login",
                             command=lambda: controller.show_frame(StartPage, "Login"), width=20)


        button1.grid(row=10, column=0, pady=10, padx=10)


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
            # dbh_emp.insert(emp)
            messagebox.showinfo("Done")
            self.controller.show_frame(StartPage, "Login")




app = tkinterApp()
app.title("Login")
app.minsize(800, 500)
app.mainloop()
