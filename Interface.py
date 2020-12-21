import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from dbh_emp import EmployeeDBHelper


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
            window.config(bg="black")
            l1= tk.Label(window, text="Employee Id", font=("Arial", 15), bg="black", fg="white")
            l1.place(x=10, y=10)
            t1 = tk.Entry(window, width=30)
            t1.place(x=200, y=10)

            l2 = tk.Label(window, text="Email", font=("Arial", 15), bg="black", fg="white")
            l2.place(x=10, y=60)
            t2 = tk.Entry(window, width=30)
            t2.place(x=200, y=60)

            l3 = tk.Label(window, text="Username", font=("Arial", 15),bg="black", fg="white")
            l3.place(x=10, y=110)
            t3 = tk.Entry(window, width=30)
            t3.place(x=200, y=110)

            l4 = tk.Label(window, text="Password", font=("Arial", 15),bg="black", fg="white")
            l4.place(x=10, y=160)
            t4 = tk.Entry(window, width=30)
            t4.place(x=200, y=160)

            l5 = tk.Label(window, text="Confirm Password", font=("Arial", 15), bg="black", fg="white")
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

        def our_command():
            pass



        Label = tk.Label(self, text="Second Page")
        Label.place(x=230, y=230)
        Button = tk.Button(self, text="Next", command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=650, y=450)

        Button_back = tk.Button(self, text="Back", command=lambda: controller.show_frame(FirstPage))
        Button_back.place(x=100, y=450)


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
        self.show_frame(FirstPage)

    def show_frame(self, page):
        frame = self.frames[page]

        if page == FirstPage:
            self.title("Login")
            self.maxsize(800, 500)
            self.minsize(800, 500)

        if page == SecondPage:
            self.title("Dashboard")
            self.maxsize(1350,720)

            my_menu = tk.Menu(self)
            self.config(menu=my_menu)
            file_menu = tk.Menu(my_menu)
            my_menu.add_cascade(label="File", menu=file_menu)
            file_menu.add_command(label="New Employee")
            file_menu.add_command(label="New Security")
            file_menu.add_command(label="Settings")
            file_menu.add_command(label="Exit")

            edit_menu = tk.Menu(my_menu)
            my_menu.add_cascade(label="Edit", menu=edit_menu)
            edit_menu.add_command(label="Update Security")
            edit_menu.add_command(label="Update Employee")

            statistic_menu = tk.Menu(my_menu)
            my_menu.add_cascade(label="Statistic", menu=statistic_menu)
            statistic_menu.add_command(label="Today")
            statistic_menu.add_command(label="Yesterday")
            statistic_menu.add_command(label="Unknown Person")
            statistic_menu.add_command(label="Authorized Access")
            statistic_menu.add_command(label="Unauthorized Access")

            view_menu = tk.Menu(my_menu)
            my_menu.add_cascade(label="View", menu=view_menu)
            view_menu.add_command(label="All Employee")
            view_menu.add_command(label="All Security")
        frame.tkraise()


app = Application()
app.mainloop()
