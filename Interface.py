import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from functools import partial

from tkinter import filedialog
from PIL import Image, ImageTk

from cl_permitted import Permitted
from cl_monitoring import Monitoring, Access
from cl_permit_area import PermitArea
from cl_stranger import Stranger
from dbh_stranger import StrangerDbHelper






from dbh_emp import EmployeeDBHelper
from dbh_person_reg import AuthorizedDbHelper
from dbh_organization import OrganizationDbHelper
from dbh_permit_area import PermitAreaDbHelper
from dbh_monitoring import MonitoringDbHelper, StrangerMonitoringDatabaseHelper
import os
from shutil import copyfile





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
                id = t1.get()
                email = t2.get()
                username = t3.get()
                password = t4.get()
                if t1.get() != "" or t2.get() != "" or t3.get() != "" or t4.get() != "" or t5.get() !="":
                    if t4.get() == t5.get():
                        emp_db = EmployeeDBHelper()
                        is_found_emp=emp_db.find_by_email_and_pass(id,email)
                        if len(is_found_emp)>0:
                            emp_db.register(id, username, password)
                            messagebox.showinfo("Success", "Registration Success")
                            window.destroy()
                        else:
                            messagebox.showerror("User Not Found", "Email or User id does not exist")
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

        org_db = OrganizationDbHelper()
        per_db = AuthorizedDbHelper()
        sec_db = EmployeeDBHelper()
        monitoring_dbh = MonitoringDbHelper()
        str_mon_dbh = StrangerMonitoringDatabaseHelper()
        stranger_dbh = StrangerDbHelper()


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
            permitted_location = []


            # def on_select(cb):
            #
            org_db = OrganizationDbHelper()
            orgs = org_db.find_all()
            orgs_name = []
            for ors in orgs:
                orgs_name.append(str(ors.get_id())+" "+ors.get_name())

            selected_org = tk.StringVar()
            selected_org.set(orgs_name[0])

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
            ent_org_id = tk.OptionMenu(frame_content, selected_org, *orgs_name)
            ent_org_id.config(width=15, font=('Helvetica', 12))
            ent_org_id.pack()

            tk.Label(frame_content, text="Select Permitted Area", font=("Arial", 20)).pack(pady=20)

            floor1 = tk.StringVar()
            floor2 = tk.StringVar()
            floor3 = tk.StringVar()
            floor4 = tk.StringVar()
            floor5 = tk.StringVar()
            floor6 = tk.StringVar()
            floor7 = tk.StringVar()
            floor8 = tk.StringVar()
            floor9 = tk.StringVar()

            cb1 = tk.Checkbutton(frame_content, text="1st Floor",variable=floor1, onvalue="1st Floor", offvalue="").place(x=0, y=250)
            cb2 = tk.Checkbutton(frame_content, text="2nd Floor",variable=floor2, onvalue="2nd Floor", offvalue="").place(x=100, y=250)
            cb3 = tk.Checkbutton(frame_content, text="3rd Floor",variable=floor3, onvalue="3th Floor", offvalue="").place(x=200, y=250)
            cb4 = tk.Checkbutton(frame_content, text="4th Floor",variable=floor4, onvalue="4th Floor", offvalue="").place(x=300, y=250)
            cb5 = tk.Checkbutton(frame_content, text="5th Floor",variable=floor5, onvalue="5th Floor", offvalue="").place(x=400, y=250)
            cb6 = tk.Checkbutton(frame_content, text="6th Floor",variable=floor6, onvalue="6th Floor", offvalue="").place(x=500, y=250)
            cb7 = tk.Checkbutton(frame_content, text="7th Floor",variable=floor7, onvalue="7th Floor", offvalue="").place(x=600, y=250)
            cb8 = tk.Checkbutton(frame_content, text="8th Floor",variable=floor8, onvalue="8th Floor", offvalue="").place(x=700, y=250)
            cb9 = tk.Checkbutton(frame_content, text="9th Floor",variable=floor9, onvalue="9th Floor", offvalue="").pack(pady=20)

            def check_permitted(value):
                if value != "":
                    permitted_location.append(value)

            def brows_image():
                img_loc = filedialog.askopenfilename(initialdir="/home/rktirtho/", title="Select Image", filetypes=(("JPG Files", "*.jpg"), ("PNG Files", "*.png")))

                global image_file
                image_file = img_loc


            def save():
                check_permitted(floor1.get())
                check_permitted(floor2.get())
                check_permitted(floor3.get())
                check_permitted(floor4.get())
                check_permitted(floor5.get())
                check_permitted(floor6.get())
                check_permitted(floor7.get())
                check_permitted(floor8.get())
                check_permitted(floor9.get())
                print(permitted_location)
                prossesing_org_id = selected_org.get().split(" ")

                emp_id = ent_em_id.get()
                emp_name = ent_name.get()
                org_id = prossesing_org_id[0]
                img = image_file

                if emp_id.strip() == "" or emp_name.strip() == "" or org_id.strip() == "":
                    messagebox.showwarning("All Field Required", "* Marked Field Required")
                else:

                    names = emp_name.strip(" ")
                    file_name = names[0]
                    auth_db = AuthorizedDbHelper()
                    permitted = Permitted(emp_name, str(emp_id)+str(org_id)+file_name, "Hawk Eye", int(org_id),emp_id)
                    auth_db.save(permitted)

                    copyfile(img, os.path.join("/home/rktirtho/PycharmProjects/Hawk-Eye/images/auth/"+str(emp_id)+str(org_id)+file_name+".jpg"))
                    copyfile(img, os.path.join("/home/rktirtho/Documents/workspace-spring-tool-suite-4-4.7.1.RELEASE/hawk-eye-serversite/src/main/resources/static/images/"+str(emp_id)+str(org_id)+file_name+".jpg"))
                    permit_area_dbh = PermitAreaDbHelper()

                    for area in permitted_location:
                        permit_area_dbh.add(emp_id, area)

                    permitted_location.clear()




            tk.Button(frame_content, text="Load Image*", command=brows_image).pack(pady=10)
            tk.Button(frame_content, text="Save", command=save, bg="#0D1117", fg="#AFB5BB", width=20).pack(padx=20)
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

            lb_org = tk.Label(frame_content, text="Email*")
            lb_org.pack()
            ent_email = tk.Entry(frame_content, )
            ent_email.pack()



            def brows_image():
                img_loc = filedialog.askopenfilename(initialdir="/home/rktirtho/", title="Select Image", filetypes=(("JPG Files", "*.jpg"), ("PNG Files", "*.png")))

                global image_file
                image_file = img_loc

            def save():
                img = image_file

                id = ent_em_id.get()
                name = ent_name.get()
                email = ent_email.get()

                if id.strip() == "" or name.strip() == "" or email.strip() == "":
                    messagebox.showwarning("All Field Required", "* Marked Field Required")
                else:

                    names = name.strip(" ")
                    file_name = names[0]
                    emp_db = EmployeeDBHelper()
                    auth_db = AuthorizedDbHelper()
                    emp_db.save(id, name, email)
                    permitted = Permitted(name, str(id)+str(1)+file_name, "Hawk Eye", 1,id)
                    auth_db.save(permitted)

                    copyfile(img, os.path.join("/home/rktirtho/PycharmProjects/Hawk-Eye/images/auth/"+str(id)+str(1)+file_name+".jpg"))
                    copyfile(img, os.path.join("/home/rktirtho/Documents/workspace-spring-tool-suite-4-4.7.1.RELEASE/hawk-eye-serversite/src/main/resources/static/images/"+str(id)+str(1)+file_name+".jpg"))




                # except:
                #     messagebox.showwarning("All Field Required", "Image Required")

            tk.Button(frame_content, text="Browse Image*", command=brows_image).pack(pady=10)
            tk.Button(frame_content, text="Save", command=save, bg="#0D1117", fg="#AFB5BB", width=20).pack(padx=20)
        def add_org_menu():
            hide_all_frame()
            add_title("New Organization")

            lb_name = tk.Label(frame_content, text="Organization Name*")
            lb_name.pack()
            ent_name = tk.Entry(frame_content, )
            ent_name.pack()

            lb_org = tk.Label(frame_content, text="Owner Name")
            lb_org.pack()
            ent_owner = tk.Entry(frame_content, )
            ent_owner.pack()

            lb_emp_id = tk.Label(frame_content, text="Address")
            lb_emp_id.pack()
            ent_address = tk.Entry(frame_content, )
            ent_address.pack()

            def save():
                name= ent_name.get()
                owner = ent_owner.get()
                address = ent_address.get()
                s="dfd"

                if name == "" or owner == "" or address=="":
                    messagebox.showerror("Required", "All Field required.")
                else:
                    org_db_helper = OrganizationDbHelper()
                    org_db_helper.save(name, owner, address)
                    ent_name.delete(0, "end")
                    ent_address.delete(0, "end")
                    ent_owner.delete(0, "end")
                    messagebox.showinfo("Saved!!", "Information added")



            tk.Button(frame_content, text="Save", command=save, bg="#0D1117", fg="#AFB5BB", width=20).pack(pady=20)

        # ============================= Edit Menu  ============================

        def edit_person():
            hide_all_frame()
            add_title("Edit Person")
            lb_emp_id = tk.Label(frame_content, text="Person Id")
            lb_emp_id.pack()
            ent_em_id = tk.Entry(frame_content, )
            ent_em_id.pack()

            def search_person():

                person_id = ent_em_id.get()
                person_db = AuthorizedDbHelper()
                person = person_db.find_one(person_id)
                print(person_id)
                print(person)

                if(person != None):

                    lb_name = tk.Label(frame_content, text="Employee Name*")
                    lb_name.pack()
                    ent_name = tk.Entry(frame_content, textvariable="person.get_name()")
                    ent_name.pack(pady=10)
                    ent_name.insert(0, person.get_name())

                    lb_org = tk.Label(frame_content,  text="Organization ID*")
                    lb_org.pack()
                    ent_org_id = tk.Entry(frame_content, text=person.get_organization())
                    ent_org_id.pack(pady=10)
                    ent_org_id.insert(0, person.get_organization())

                    tk.Button(frame_content, text="Change Image*").pack(pady=10)
                    tk.Button(frame_content, text="Save", bg="#0D1117", fg="#AFB5BB", width=20).pack(padx=20)

                else:
                    messagebox.showerror("Not Found", "Employee not found")

            src = tk.Button(frame_content, text="Search", command=search_person,  bg="green", fg="#AFB5BB", width=20).pack(padx=20,pady=20)

        def edit_employee():
            hide_all_frame()
            add_title("Edit Employee")
            lb_emp_id = tk.Label(frame_content, text="Person Id")
            lb_emp_id.pack()
            ent_em_id = tk.Entry(frame_content, )
            ent_em_id.pack()

            def search_person():

                person_id = ent_em_id.get()
                person_db = AuthorizedDbHelper()
                person = person_db.find_one(person_id)
                print(person_id)
                print(person)

                if(person != None):

                    lb_name = tk.Label(frame_content, text="Employee Name*")
                    lb_name.pack()
                    ent_name = tk.Entry(frame_content, textvariable="person.get_name()")
                    ent_name.pack(pady=10)
                    ent_name.insert(0, person.get_name())

                    lb_org = tk.Label(frame_content,  text="Organization ID*")
                    lb_org.pack()
                    ent_org_id = tk.Entry(frame_content, text=person.get_organization())
                    ent_org_id.pack(pady=10)
                    ent_org_id.insert(0, person.get_organization())

                    tk.Button(frame_content, text="Change Image*").pack(pady=10)
                    tk.Button(frame_content, text="Save", bg="#0D1117", fg="#AFB5BB", width=20).pack(padx=20)

                else:
                    messagebox.showerror("Not Found", "Employee not found")

            src = tk.Button(frame_content, text="Search", command=search_person,  bg="green", fg="#AFB5BB", width=20).pack(padx=20,pady=20)



        # ==================== Statistic Menu Function=========================

        def today_info():
            hide_all_frame()
            add_title("Today")
            persons = monitoring_dbh.get_today()

            x = 1
            y = 0

            f1 = tk.Frame(frame_content)
            if len(persons) == 0:
                name = tk.Label(f1, text="No data found", fg="red", font=("Arial", 18))
                name.pack(pady=30)

            for person in persons:
                l1 = tk.Frame(f1, bg="ivory", highlightthickness=2, bd=10, width=200, height=200)
                l1.config(highlightbackground="#eeeeee", highlightcolor="#eeeeee")
                l1.grid(row=x, column=y, padx=10, pady=20)

                file = 'images/auth/' + person.get_image() + '.jpg'
                image = Image.open(file)
                img = ImageTk.PhotoImage(image.resize((100, 100)))

                bg = tk.Label(l1, image=img, height=100, width=100)
                bg.image = img
                bg.pack()

                name = tk.Label(l1, text=person.get_name())
                name.pack()
                email = tk.Label(l1, text=person.get_image())
                email.pack()
                org = tk.Label(l1, text=person.get_organization())
                org.pack()
                btn = tk.Button(l1, text="View", bg="green", command=partial(show_today_info, person.get_name(), person.get_id()))
                btn.pack()

                y += 1
                if y > 5:
                    x += 1
                    y = 0
                f1.grid_columnconfigure(y, weight=1)

            f1.pack(fill="both")

        def yesterday_info():
            hide_all_frame()
            add_title("Yesterday")
            persons = monitoring_dbh.get_yesterday()

            x = 1
            y = 0

            f1 = tk.Frame(frame_content)
            for person in persons:
                l1 = tk.Frame(f1, bg="ivory", highlightthickness=2, bd=10, width=200, height=200)
                l1.config(highlightbackground="#eeeeee", highlightcolor="#eeeeee")
                l1.grid(row=x, column=y, padx=10, pady=20)

                file = 'images/auth/' + person.get_image() + '.jpg'
                image = Image.open(file)
                img = ImageTk.PhotoImage(image.resize((100, 100)))

                bg = tk.Label(l1, image=img, height=100, width=100)
                bg.image = img
                bg.pack()

                name = tk.Label(l1, text=person.get_name())
                name.pack()
                email = tk.Label(l1, text=person.get_image())
                email.pack()
                org = tk.Label(l1, text=person.get_organization())
                org.pack()
                btn = tk.Button(l1, text="View", bg="green", command=partial(show_yesterday_info, person.get_name(), person.get_id()))
                btn.pack()

                y += 1
                if y > 5:
                    x += 1
                    y = 0
                f1.grid_columnconfigure(y, weight=1)

            f1.pack(fill="both")

        def show_stranger_info(name, id):
            root = tk.Tk(className="Hawk Eye")
            root.title(name)

            moves = str_mon_dbh.get_access_by_id(id)
            tk.Label(root, text="Area", font=("Ariel", 15, "bold"), padx=30).grid(row=2, column=0, padx=30)
            tk.Label(root, text="Time", font=("Ariel", 15,"bold")).grid(row=2, column=1, padx=30)
            # tk.Label(root, text="Access", font=("Ariel", 15,"bold")).grid(row=2, column=2, padx=30)
            count =3
            for move in moves:
                name = tk.Label(root, text=move.get_area(), font=("Ariel", 12)).grid(row=count, column=0)
                name1 = tk.Label(root, text=move.get_time(), font=("Ariel", 12)).grid(row=count, column=1, pady=5)
                # if move.is_permit() ==1:
                #     tk.Label(root, text="Permitted", width=20,bg="green", fg="white", font=("Ariel", 12)).grid(row=count, column=2)
                # else:
                #     tk.Label(root, text="Illegal",width=20, bg="red", fg="white", font=("Ariel", 12)).grid(row=count, column=2)
                count += 1

            root.minsize(500,400)
            root.mainloop()

        def show_info(name, id):
            root = tk.Tk(className="Hawk Eye")
            root.title(name)

            moves = monitoring_dbh.get_access_by_id(id)
            tk.Label(root, text="Area", font=("Ariel", 15, "bold"), padx=30).grid(row=2, column=0, padx=30)
            tk.Label(root, text="Time", font=("Ariel", 15,"bold")).grid(row=2, column=1, padx=30)
            tk.Label(root, text="Access", font=("Ariel", 15,"bold")).grid(row=2, column=2, padx=30)
            count =3
            for move in moves:
                name = tk.Label(root, text=move.get_area(), font=("Ariel", 12)).grid(row=count, column=0)
                name1 = tk.Label(root, text=move.get_time(), font=("Ariel", 12)).grid(row=count, column=1, pady=5)
                if move.is_permit() ==1:
                    tk.Label(root, text="Permitted", width=20,bg="green", fg="white", font=("Ariel", 12)).grid(row=count, column=2)
                else:
                    tk.Label(root, text="Illegal",width=20, bg="red", fg="white", font=("Ariel", 12)).grid(row=count, column=2)
                count += 1

            root.minsize(500,400)
            root.mainloop()

        def show_today_info(name, id):
            root = tk.Tk(className="Hawk Eye")
            root.title(name)

            moves = monitoring_dbh.get_today_access_by_id(id)
            tk.Label(root, text="Area", font=("Ariel", 15, "bold"), padx=30).grid(row=2, column=0, padx=30)
            tk.Label(root, text="Time", font=("Ariel", 15,"bold")).grid(row=2, column=1, padx=30)
            tk.Label(root, text="Access", font=("Ariel", 15,"bold")).grid(row=2, column=2, padx=30)
            count =3
            for move in moves:
                name = tk.Label(root, text=move.get_area(), font=("Ariel", 12)).grid(row=count, column=0)
                name1 = tk.Label(root, text=move.get_time(), font=("Ariel", 12)).grid(row=count, column=1, pady=5)
                if move.is_permit() ==1:
                    tk.Label(root, text="Permitted", width=20,bg="green", fg="white", font=("Ariel", 12)).grid(row=count, column=2)
                else:
                    tk.Label(root, text="Illegal",width=20, bg="red", fg="white", font=("Ariel", 12)).grid(row=count, column=2)
                count += 1

            root.minsize(500,400)
            root.mainloop()

        def show_yesterday_info(name, id):
            root = tk.Tk(className="Hawk Eye")
            root.title(name)

            moves = monitoring_dbh.get_yesterday_access_by_id(id)
            tk.Label(root, text="Area", font=("Ariel", 15, "bold"), padx=30).grid(row=2, column=0, padx=30)
            tk.Label(root, text="Time", font=("Ariel", 15,"bold")).grid(row=2, column=1, padx=30)
            tk.Label(root, text="Access", font=("Ariel", 15,"bold")).grid(row=2, column=2, padx=30)
            count =3
            for move in moves:
                name = tk.Label(root, text=move.get_area(), font=("Ariel", 12)).grid(row=count, column=0)
                name1 = tk.Label(root, text=move.get_time(), font=("Ariel", 12)).grid(row=count, column=1, pady=5)
                if move.is_permit() ==1:
                    tk.Label(root, text="Permitted", width=20,bg="green", fg="white", font=("Ariel", 12)).grid(row=count, column=2)
                else:
                    tk.Label(root, text="Illegal",width=20, bg="red", fg="white", font=("Ariel", 12)).grid(row=count, column=2)
                count += 1

            root.minsize(500,400)
            root.mainloop()
        def show_auth_info(name, id):
            root = tk.Tk(className="Hawk Eye")
            root.title(name)

            moves = monitoring_dbh.get_auth_access_by_id(id)
            tk.Label(root, text="Area", font=("Ariel", 15, "bold"), padx=30).grid(row=2, column=0, padx=30)
            tk.Label(root, text="Time", font=("Ariel", 15,"bold")).grid(row=2, column=1, padx=30)
            tk.Label(root, text="Access", font=("Ariel", 15,"bold")).grid(row=2, column=2, padx=30)
            count =3
            for move in moves:
                name = tk.Label(root, text=move.get_area(), font=("Ariel", 12)).grid(row=count, column=0)
                name1 = tk.Label(root, text=move.get_time(), font=("Ariel", 12)).grid(row=count, column=1, pady=5)
                if move.is_permit() ==1:
                    tk.Label(root, text="Permitted", width=20,bg="green", fg="white", font=("Ariel", 12)).grid(row=count, column=2)
                else:
                    tk.Label(root, text="Illegal",width=20, bg="red", fg="white", font=("Ariel", 12)).grid(row=count, column=2)
                count += 1

            root.minsize(500,400)
            root.mainloop()

        def show_unauth_info(name, id):
            root = tk.Tk(className="Hawk Eye")
            root.title(name)

            moves = monitoring_dbh.get_unauth_access_by_id(id)
            tk.Label(root, text="Area", font=("Ariel", 15, "bold"), padx=30).grid(row=2, column=0, padx=30)
            tk.Label(root, text="Time", font=("Ariel", 15,"bold")).grid(row=2, column=1, padx=30)
            tk.Label(root, text="Access", font=("Ariel", 15,"bold")).grid(row=2, column=2, padx=30)
            count =3
            for move in moves:
                name = tk.Label(root, text=move.get_area(), font=("Ariel", 12)).grid(row=count, column=0)
                name1 = tk.Label(root, text=move.get_time(), font=("Ariel", 12)).grid(row=count, column=1, pady=5)
                if move.is_permit() ==1:
                    tk.Label(root, text="Permitted", width=20,bg="green", fg="white", font=("Ariel", 12)).grid(row=count, column=2)
                else:
                    tk.Label(root, text="Illegal",width=20, bg="red", fg="white", font=("Ariel", 12)).grid(row=count, column=2)
                count += 1

            root.minsize(500,400)
            root.mainloop()

        def show_info(name, id):
            root = tk.Tk(className="Hawk Eye")
            root.title(name)

            moves = monitoring_dbh.get_access_by_id(id)
            tk.Label(root, text="Area", font=("Ariel", 15, "bold"), padx=30).grid(row=2, column=0, padx=30)
            tk.Label(root, text="Time", font=("Ariel", 15,"bold")).grid(row=2, column=1, padx=30)
            tk.Label(root, text="Access", font=("Ariel", 15,"bold")).grid(row=2, column=2, padx=30)
            count =3
            for move in moves:
                name = tk.Label(root, text=move.get_area(), font=("Ariel", 12)).grid(row=count, column=0)
                name1 = tk.Label(root, text=move.get_time(), font=("Ariel", 12)).grid(row=count, column=1, pady=5)
                if move.is_permit() ==1:
                    tk.Label(root, text="Permitted", width=20,bg="green", fg="white", font=("Ariel", 12)).grid(row=count, column=2)
                else:
                    tk.Label(root, text="Illegal",width=20, bg="red", fg="white", font=("Ariel", 12)).grid(row=count, column=2)
                count += 1

            root.minsize(500,400)
            root.mainloop()


        def all_info():
            hide_all_frame()
            add_title("All Info")
            persons = monitoring_dbh.get_all()
            x = 1
            y = 0
            f1 = tk.Frame(frame_content)
            for person in persons:
                l1 = tk.Frame(f1, bg="ivory", highlightthickness=2, bd=10, width=200, height=200)
                l1.config(highlightbackground="#eeeeee", highlightcolor="#eeeeee")
                l1.grid(row=x, column=y, padx=10, pady=20)

                file = 'images/auth/' + person.get_image() + '.jpg'
                image = Image.open(file)
                img = ImageTk.PhotoImage(image.resize((100, 100)))

                bg = tk.Label(l1, image=img, height=100, width=100)
                bg.image = img
                bg.pack()

                name = tk.Label(l1, text=person.get_name())
                name.pack()
                email = tk.Label(l1, text=person.get_image())
                email.pack()
                org = tk.Label(l1, text=person.get_organization())
                org.pack()
                btn = tk.Button(l1, text="View", bg="green", command=partial(show_info, person.get_name(), person.get_id()))
                btn.pack()

                y += 1
                if y > 5:
                    x += 1
                    y = 0
                f1.grid_columnconfigure(y, weight=1)

            f1.pack(fill="both")

        def auth_access():
            hide_all_frame()
            add_title("Authorized Access")
            hide_all_frame()
            add_title("All Info")
            access = monitoring_dbh.get_auth_access()

            x = 1
            y = 0

            f1 = tk.Frame(frame_content)
            for acc in access:
                l1 = tk.Frame(f1, bg="ivory", highlightthickness=2, bd=10, width=200, height=200)
                l1.config(highlightbackground="#eeeeee", highlightcolor="#eeeeee")
                l1.grid(row=x, column=y, padx=10, pady=20)

                file = 'images/auth/' + acc.get_image_id() + '.jpg'
                image = Image.open(file)
                img = ImageTk.PhotoImage(image.resize((100, 100)))

                bg = tk.Label(l1, image=img, height=100, width=100)
                bg.image = img
                bg.pack()
                org = org_db.find_one(acc.get_org_id())

                name = tk.Label(l1, text=acc.get_name())
                name.pack()
                email = tk.Label(l1, text=org.get_name())
                email.pack()
                # org = tk.Label(l1, text=person.get_organization())
                # org.pack()
                btn = tk.Button(l1, text="View", bg="green", command=partial(show_auth_info, acc.get_name(), acc.get_id()))
                btn.pack()

                y += 1
                if y > 5:
                    x += 1
                    y = 0
                f1.grid_columnconfigure(y, weight=1)

            f1.pack(fill="both")

        def strangers_access():
            hide_all_frame()
            add_title("Strangers Access")
            hide_all_frame()
            add_title("Strangers Access")
            access = str_mon_dbh.get_all()

            x = 1
            y = 0

            f1 = tk.Frame(frame_content)
            for acc in access:
                l1 = tk.Frame(f1, bg="ivory", highlightthickness=2, bd=10, width=200, height=200)
                l1.config(highlightbackground="#eeeeee", highlightcolor="#eeeeee")
                l1.grid(row=x, column=y, padx=10, pady=20)

                file = 'images/strangers/' + acc.get_image() + '.jpg'
                image = Image.open(file)
                img = ImageTk.PhotoImage(image.resize((100, 100)))

                bg = tk.Label(l1, image=img, height=100, width=100)
                bg.image = img
                bg.pack()

                name = tk.Label(l1, text=acc.get_image())
                name.pack()
                org = tk.Label(l1, text=acc.get_visited())
                org.pack()
                btn = tk.Button(l1, text="View", bg="green", command=partial(show_stranger_info, acc.get_image(), acc.get_id()))
                btn.pack()

                y += 1
                if y > 5:
                    x += 1
                    y = 0
                f1.grid_columnconfigure(y, weight=1)

            f1.pack(fill="both")

        def unauth_access():
            hide_all_frame()
            add_title("Unauthorized Access")
            hide_all_frame()
            add_title("All Info")
            access = monitoring_dbh.get_unauth_access()

            x = 1
            y = 0

            f1 = tk.Frame(frame_content)
            for acc in access:
                l1 = tk.Frame(f1, bg="ivory", highlightthickness=2, bd=10, width=200, height=200)
                l1.config(highlightbackground="#eeeeee", highlightcolor="#eeeeee")
                l1.grid(row=x, column=y, padx=10, pady=20)

                file = 'images/auth/' + acc.get_image_id() + '.jpg'
                image = Image.open(file)
                img = ImageTk.PhotoImage(image.resize((100, 100)))

                bg = tk.Label(l1, image=img, height=100, width=100)
                bg.image = img
                bg.pack()
                org = org_db.find_one(acc.get_org_id())

                name = tk.Label(l1, text=acc.get_name())
                name.pack()
                email = tk.Label(l1, text=org.get_name())
                email.pack()
                # org = tk.Label(l1, text=person.get_organization())
                # org.pack()
                btn = tk.Button(l1, text="View", bg="green",command=partial(show_unauth_info, acc.get_name(), acc.get_id()))
                btn.pack()

                y += 1
                if y > 5:
                    x += 1
                    y = 0
                f1.grid_columnconfigure(y, weight=1)

            f1.pack(fill="both")

        def show_statistics():
            hide_all_frame()
            f1 = tk.Frame(frame_content)
            x = 1
            y = 0
            for i in range(5):

                l1 = tk.Frame(f1, bg="ivory", highlightthickness=2, bd=10, width=800, height=400, relief="raised")
                l1.config(highlightbackground="#eeeeee", highlightcolor="#eeeeee", width=800)
                l1.grid(row=x, column=y, padx=10, pady=20)

                if i == 0:
                    name = tk.Label(l1, text="Today's Visitors", width=30, bg="ivory", fg="red",
                                    font=("ariel", 10, "bold"))
                    today_visitors = str_mon_dbh.count_today_strangers()

                    email = tk.Label(l1, text=str(today_visitors[0]), bg="ivory", font=("ariel", 15, "bold"))
                    email.pack(pady=30)
                elif i == 1:
                    name = tk.Label(l1, text="Today's Employee", width=30, bg="ivory", fg="red",
                                    font=("ariel", 10, "bold"))
                    today_employee = monitoring_dbh.count_today_employee()

                    email = tk.Label(l1, text=str(today_employee[0]), bg="ivory", font=("ariel", 15, "bold"))
                    email.pack(pady=30)
                elif i == 2:
                    count = per_db.count_registered_employee()
                    name = tk.Label(l1, text="Total Employee", width=30, bg="ivory", fg="red",
                                    font=("ariel", 10, "bold"))

                    email = tk.Label(l1, text=str(count[0]), bg="ivory", font=("ariel", 15, "bold"))
                    email.pack(pady=30)
                elif i == 3:
                    count = sec_db.count_security()
                    name = tk.Label(l1, text="Security Person", width=30, bg="ivory", fg="red",
                                    font=("ariel", 10, "bold"))
                    email = tk.Label(l1, text=str(count[0]), bg="ivory", font=("ariel", 15, "bold"))
                    email.pack(pady=30)
                elif i == 4:
                    name = tk.Label(l1, text="Organizations", width=30, bg="ivory", fg="red",
                                    font=("ariel", 10, "bold"))
                    number_of_org = org_db.count_organizaton()
                    email = tk.Label(l1, text=str(number_of_org[0]), bg="ivory", font=("ariel", 15, "bold"))
                    email.pack(pady=30)

                name.pack()

                org = tk.Label(l1, text="Option")

                y += 1
                if y > 2:
                    x += 1
                    y = 0
                f1.grid_columnconfigure(y, weight=1)

            f1.pack(fill="both")
        # ============================== View Menu =============================
        def view_all_employee():
            hide_all_frame()
            add_title("All Security Person")
            per = AuthorizedDbHelper()
            persons = per.find_all_details()

            x = 1
            y = 0

            f1 = tk.Frame(frame_content)
            for person in persons:
                l1 = tk.Frame(f1, bg="ivory", highlightthickness=2, bd=10, width=200, height=200)
                l1.config(highlightbackground="#eeeeee", highlightcolor="#eeeeee")
                l1.grid(row=x, column=y, padx=10, pady=20)

                file = 'images/auth/'+person.get_image()+'.jpg'
                image = Image.open(file)
                img = ImageTk.PhotoImage(image.resize((100, 100)))

                bg = tk.Label(l1, image=img, height=100, width=100)
                bg.image = img
                bg.pack()

                name = tk.Label(l1, text=person.get_name(),bg="ivory")
                name.pack()
                # email = tk.Label(l1, text=person.get_image(),bg="ivory")
                # email.pack()
                org = tk.Label(l1, text=person.get_organization(),bg="ivory")
                org.pack()
                btn = tk.Button(l1, text="View", bg="green", fg="white", command=partial(show_info,person.get_name(), person.get_id()))
                btn.pack()

                y += 1
                if y>5:
                    x+=1
                    y=0
                f1.grid_columnconfigure(y, weight=1)

            f1.pack(fill="both")

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

                file = 'images/meterial/placeholder.png'
                image = Image.open(file)
                img = ImageTk.PhotoImage(image.resize((100, 100)))
                bg = tk.Label(l1, image=img, height=100, width=100)
                bg.image = img
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

        def view_all_stranger():
            hide_all_frame()
            add_title("All Security Person")
            strangers = stranger_dbh.get_all_strangers()

            x = 1
            y = 0

            f1 = tk.Frame(frame_content)
            for stn in strangers:
                l1 = tk.Frame(f1, bg="ivory", highlightthickness=2, bd=10, width=200, height=200)
                l1.config(highlightbackground="#eeeeee", highlightcolor="#eeeeee")
                l1.grid(row=x, column=y, padx=10, pady=20)

                file = 'images/strangers/' + stn.get_image() + '.jpg'
                image = Image.open(file)
                img = ImageTk.PhotoImage(image.resize((100, 100)))

                bg = tk.Label(l1, image=img, height=100, width=100)
                bg.image = img
                bg.pack()

                name = tk.Label(l1, text=stn.get_image(), bg="ivory")
                name.pack()
                # email = tk.Label(l1, text=person.get_image(),bg="ivory")
                # email.pack()
                org = tk.Label(l1, text="Visited : 41 Times", bg="ivory")
                org.pack()
                btn = tk.Button(l1, text="View", bg="green", fg="white",
                                command=partial(show_stranger_info, stn.get_image(), stn.get_id()))
                btn.pack()

                y += 1
                if y > 5:
                    x += 1
                    y = 0
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

        # if parent == SecondPage:
        my_menu = tk.Menu(self)
        controller.config(menu=my_menu)
        file_menu = tk.Menu(my_menu)
        my_menu.add_cascade(label="New", menu=file_menu)
        file_menu.add_command(label="Employee", command=add_person_menu)
        file_menu.add_command(label="Security", command=add_employee_menu)
        file_menu.add_command(label="Organization", command=add_org_menu)
        file_menu.add_separator()
        file_menu.add_command(label="Settings", command=settings)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        edit_menu = tk.Menu(my_menu)
        my_menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Update Security" , command=edit_employee)
        edit_menu.add_command(label="Update Employee", command=edit_person)


        statistic_menu = tk.Menu(my_menu)
        my_menu.add_cascade(label="Statistic", menu=statistic_menu)
        statistic_menu.add_command(label="Today", command=today_info)
        statistic_menu.add_command(label="Yesterday",command=yesterday_info)
        statistic_menu.add_separator()
        statistic_menu.add_command(label="All Access", command=all_info)
        statistic_menu.add_separator()
        statistic_menu.add_command(label="Authorized Access",command=auth_access)
        statistic_menu.add_command(label="Unauthorized Access", command = unauth_access)
        statistic_menu.add_separator()
        statistic_menu.add_command(label="Strangers", command = strangers_access)
        statistic_menu.add_separator()
        statistic_menu.add_command(label="Statistics", command = show_statistics)

        view_menu = tk.Menu(my_menu)
        my_menu.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="All Employee", command=view_all_employee)
        view_menu.add_command(label="All Security", command=view_all_security)
        view_menu.add_command(label="All Strangers", command=view_all_stranger)
        view_menu.add_command(label="All Organization", command=view_all_org)


        frame_content = tk.Frame(self)
        frame_content.pack(fill="both", expand=1, pady=50)

        show_statistics()


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


app = Application(className="Hawk Eye")
ico = Image.open('images/meterial/logo.png')
photo = ImageTk.PhotoImage(ico)
app.wm_iconphoto(False, photo)
app.geometry("0x0")
app.mainloop()
