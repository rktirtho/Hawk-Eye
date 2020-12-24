import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from dbh_emp import EmployeeDBHelper
from dbh_person_reg import AuthorizedDbHelper
from dbh_organization import OrganizationDbHelper


class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        self.emp_db_helper = EmployeeDBHelper()

        tk.Frame.__init__(self, parent)


        load = Image.open("images/meterial/bg.jpg")
        photo = ImageTk.PhotoImage(load)
        bg = tk.Label(self, image=photo)
        bg.image = photo
        bg.place(x=0,y=0)

        border = tk.LabelFrame(self, text="login", bg="ivory", bd=10, font=("Arial", 20))
        border.pack(fill="both", expand="yes", padx=150, pady=140)

        l1 = tk.Label(border,  bg="ivory", text="Username")
        l1.place(x=50, y=20)
        t1 = tk.Entry(border, width=30, bd=5)
        t1.place(x=180, y=20)

        l2 = tk.Label(border, bg="ivory", text="password")
        l2.place(x=50, y=80)
        t2 = tk.Entry(border, show="*", width=30, bd=5)
        t2.place(x=180, y=80)

        def verify():
            if t1.get() == "" or t2.get =="":
                messagebox.showwarning("Warning", "Username and password required")
            else:
                record = self.emp_db_helper.login(t1.get(), t2.get())
                if record:
                    controller.show_frame(SecondPage)
                else:
                    messagebox.showerror("Login Failed","Username or Password mismatch.")

        def register():
            window = tk.Tk()
            window.title("Register")
            window.config(bg="#0D1117")
            l1= tk.Label(window, text="Employee Id", font=("Arial", 15), bg="#0D1117", fg="#AFB5BB")
            l1.place(x=10, y=10)
            t1 = tk.Entry(window, width=30)
            t1.place(x=200, y=10)

            l2 = tk.Label(window, text="Email", font=("Arial", 15), bg="#0D1117", fg="#AFB5BB")
            l2.place(x=10, y=60)
            t2 = tk.Entry(window, width=30)
            t2.place(x=200, y=60)

            l3 = tk.Label(window, text="Username", font=("Arial", 15),bg="#0D1117", fg="#AFB5BB")
            l3.place(x=10, y=110)
            t3 = tk.Entry(window, width=30)
            t3.place(x=200, y=110)

            l4 = tk.Label(window, text="Password", font=("Arial", 15),bg="#0D1117", fg="#AFB5BB")
            l4.place(x=10, y=160)
            t4 = tk.Entry(window, width=30)
            t4.place(x=200, y=160)

            l5 = tk.Label(window, text="Confirm Password", font=("Arial", 15), bg="#0D1117", fg="#AFB5BB")
            l5.place(x=10, y=210)
            t5 = tk.Entry(window, width=30)
            t5.place(x=200, y=210)

            def check():
                if t1.get() != "" or t2.get() != "" or t3.get() != "" or t4.get() != "" or t5.get() !="":
                    if t4.get() == t5.get():
                        messagebox.showinfo("Success", "Registration Success")
                        window.destroy()
                    else:
                        messagebox.showerror("Error", "Password and confirm password mismatch")
                else:
                    messagebox.showwarning("Error", "All fields required")



            btn_register = tk.Button(window, text="Register", command=check, font=("Arial", 15), bg="gray", fg="black")
            btn_register.place(x=190, y=250)

            window.geometry("470x300")
            window.minsize(470,300)
            window.maxsize(470,300)
            window.resizable(0,0)
            window.mainloop()

        btn_submit = tk.Button(border, text="Submit", font=("Arial", 15), command=verify)
        btn_submit.place(x=320, y=130)

        btn_register = tk.Button(self, text="Register", bg ="dark orange",  font=("Arial", 15), command=register)
        btn_register.place(x=650, y=20)


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def add_title(text):
            Title = tk.Label(frame_content, text=text, font=("Arial", 15), pady=15)
            Title.pack()
            controller.title(text)

        def hide_all_frame():
            for widget in frame_content.winfo_children():
                widget.destroy()

        def settings():
            messagebox.showinfo("Service Not Available", "Settings will be added in commercial release")

        def add_person_menu():

            hide_all_frame()
            add_title("Register Person")
            lb_emp_id = tk.Label(frame_content, text="Employee ID")
            lb_emp_id.pack()
            ent_em_id = tk.Entry(frame_content, )
            ent_em_id.pack()

            lb_name = tk.Label(frame_content, text="Employee Name*")
            lb_name.pack()
            ent_name = tk.Entry(frame_content, )
            ent_name.pack()

            lb_org = tk.Label(frame_content, text="Organization ID*")
            lb_org.pack()
            ent_org_id = tk.Entry(frame_content, )
            ent_org_id.pack()

            tk.Button(frame_content, text="Load Image*").pack(pady=10)
            tk.Button(frame_content, text="Save", bg="#0D1117", fg="#AFB5BB", width=20).pack(padx=20)
            # content_panel.add(frame_content)

        def add_employee_menu():
            hide_all_frame()
            add_title("Register Employee")

            lb_emp_id = tk.Label(frame_content, text="Employee ID")
            lb_emp_id.pack()
            ent_em_id = tk.Entry(frame_content, )
            ent_em_id.pack()

            lb_name = tk.Label(frame_content, text="Employee Name*")
            lb_name.pack()
            ent_name = tk.Entry(frame_content, )
            ent_name.pack()

            lb_org = tk.Label(frame_content, text="Organization ID*")
            lb_org.pack()
            ent_org_id = tk.Entry(frame_content, )
            ent_org_id.pack()

            tk.Button(frame_content, text="Load Image*").pack(pady=10)
            tk.Button(frame_content, text="Save", bg="#0D1117", fg="#AFB5BB", width=20).pack(padx=20)

        # ==================== Statistic Menu Function========================
        # ============================== View Menu =============================
        def view_all_employee():
            hide_all_frame()
            # add_title("All Security Person")



        def view_all_security():
            hide_all_frame()
            # add_title("All Security Person")
            emp = EmployeeDBHelper()
            emps = emp.find_all()

            x=1
            y=0

            f1 = tk.Frame(frame_content)
            for em in emps:
                l1 = tk.Frame(f1, bg="ivory",highlightthickness=2, bd=10, width=200, height=200)
                l1.config(highlightbackground = "black", highlightcolor= "black")
                l1.grid(row=x, column=y, padx=10, pady=20)

                load = Image.open("images/meterial/bg.jpg")
                photo = ImageTk.PhotoImage(load)
                bg = tk.Label(l1, image=photo, height=100, width=100)
                bg.image = photo
                bg.pack()

                name = tk.Label(l1, text=em.get_name())
                name.pack()
                email = tk.Label(l1, text=em.get_email())
                email.pack()
                org = tk.Label(l1, text=em.get_org_id())
                org.pack()
                btn = tk.Button(l1, text="View", bg="green")
                btn.pack()

                y+=1
                f1.grid_columnconfigure(y, weight=1)

            f1.pack(fill="both")


        def view_all_org():
            hide_all_frame()
            # add_title("All Organization")

            title = tk.Label(frame_content, text="All Organizations", font=("Arial", 20)).grid(row=0, column=2, columnspan=2, pady=10)

            org = OrganizationDbHelper()
            orgs = org.find_all()
            i = 2
            c = 0
            print(orgs[1])
            tk.Label(frame_content, text="#Id", padx=20).grid(row=1, column=0, pady=10)
            tk.Label(frame_content, text="Name", padx=20).grid(row=1, column=1, pady=10)
            tk.Label(frame_content, text='Woner', padx=20).grid(row=1, column=2)
            tk.Label(frame_content, text='Address', padx=20).grid(row=1, column=3)
            tk.Label(frame_content, text='Registration', padx=20).grid(row=1, column=4)

            for org in orgs:
                tk.Label(frame_content, text=org.get_id(), padx=20).grid(row=i, column=0, pady=10)
                tk.Label(frame_content, text=org.get_name(), padx=20).grid(row=i, column=1, pady=10)
                tk.Label(frame_content, text=org.get_woner(), padx=20).grid(row=i, column=2)
                tk.Label(frame_content, text=org.get_address(), padx=20).grid(row=i, column=3)
                tk.Label(frame_content, text=org.get_reg_time(), padx=20).grid(row=i, column=4)
                i += 1



        my_menu = tk.Menu(self)
        controller.config(menu=my_menu)
        file_menu = tk.Menu(my_menu)
        my_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New Employee", command=add_person_menu)
        file_menu.add_command(label="New Security", command=add_employee_menu)
        file_menu.add_separator()
        file_menu.add_command(label="Settings", command=settings)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        edit_menu = tk.Menu(my_menu)
        my_menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Update Security")
        edit_menu.add_command(label="Update Employee")

        statistic_menu = tk.Menu(my_menu)
        my_menu.add_cascade(label="Statistic", menu=statistic_menu)
        statistic_menu.add_command(label="Today")
        statistic_menu.add_command(label="Yesterday")
        statistic_menu.add_separator()
        statistic_menu.add_command(label="Unknown Person")
        statistic_menu.add_separator()
        statistic_menu.add_command(label="Authorized Access")
        statistic_menu.add_command(label="Unauthorized Access")

        view_menu = tk.Menu(my_menu)
        my_menu.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="All Employee", command=view_all_employee)
        view_menu.add_command(label="All Security", command=view_all_security)
        view_menu.add_command(label="All Organization", command=view_all_org)



        # Label = tk.Label(self, text="Dashboard" , font=("Ariel", 15))
        # Label.place(x=350, y=20)
        # Button = tk.Button(self, text="Next", command=lambda: controller.show_frame(ThirdPage))
        # Button.place(x=650, y=450)
        #
        # Button_back = tk.Button(self, text="Back", command=lambda: controller.show_frame(FirstPage))
        # Button_back.place(x=100, y=450)

        frame_content = tk.Frame(self)
        frame_content.pack(fill="both", expand=1, pady=50)
        #
        # new_person = tk.Frame(frame_content, width=500, height=500, bg="blue")
        # frame_new_employee = tk.Frame(frame_content, width=500, height=500, bg="green")



class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        Label = tk.Label(self, text="Third Page")
        Label.place(x=230, y=230)
        Button = tk.Button(self, text="Next", command=lambda: controller.show_frame(FirstPage))
        Button.place(x=650, y=450)

        Button_back = tk.Button(self, text="Back", command=lambda: controller.show_frame(SecondPage))
        Button_back.place(x=100, y=450)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)
        self.frames = {}

        for F in (FirstPage, SecondPage, ThirdPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="NSEW")
        self.show_frame(SecondPage)

    def show_frame(self, page):
        frame = self.frames[page]

        if page == FirstPage:
            self.title("Login")
            self.minsize(800, 500)

        if page == SecondPage:
            self.title("Dashboard")
            self.minsize(1200,600)
            self.maxsize(1300, 700)

        if page == ThirdPage:
            print('test')

        frame.tkraise()


app = Application()
app.geometry("0x0")
app.mainloop()
