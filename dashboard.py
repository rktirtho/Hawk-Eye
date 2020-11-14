# Dashboard for this project
# This is the main part of this system
# Alter successfully login user will come to there.
# Actually this UI handle all kinds of Data
from tkinter import *
import json
import requests

LARGEFONT = ("Verdana", 30)
SMALLFONT = ("Verdana", 16)
MEDIAMFONT = ("Verdana", 20)
MEDIAMFONT_BOLD = ("Verdana", 16, 'bold')


root = Tk()


def click(title):
    root.title(title)

def show_all():
    click("All Person")

    contend.pack_forget()
def clearAll():
    for widget in contend.winfo_children():
        widget.destroy()

def add_emp_frame():
    # content_panel.remove(contend)
    clearAll()

    click("Add Employee")
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


def unauth_acc_wid():
    clearAll()
    click("Unauthorized Access")
    title = Label(contend, text="Unauthorized Access", font=MEDIAMFONT)
    title.pack(pady=20)


def auth_acc_wid():
    clearAll()
    click("Authorized Access")
    title = Label(contend, text="Authorized Access", font=MEDIAMFONT)
    title.pack(pady=20)
    try:
        utr = requests.get('http://127.0.0.1:8080/api/organizations')
        api = json.loads(utr.content)
        for date in api:
            Label(contend, text=date['name']).pack()
        # print(api)
    except Exception as e:
        print("Loading Failed...")


def org_wid():
    clearAll()
    click("Authorized Access")
    title = Label(contend, text="All Organization", font=MEDIAMFONT)
    title.grid(row=0, column=0, columnspan=4, pady=20)
    try:
        utr = requests.get('http://127.0.0.1:8080/api/organizations')
        api = json.loads(utr.content)
        i=2
        c=0

        Label(contend, text="Name", padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=0, pady=10)
        Label(contend, text='Woner', padx=20,font=MEDIAMFONT_BOLD).grid(row=1, column=1)
        Label(contend, text='Address', padx=20,font=MEDIAMFONT_BOLD).grid(row=1, column=2)
        for date in api:
            Label(contend, text=date['name'], padx=20).grid(row=i,column=0, pady=10)
            Label(contend, text=date['woner'],padx=20).grid(row=i,column=1)
            Label(contend, text=date['address'],padx=20).grid(row=i,column=2)
            i+=1


        # print(api)
    except Exception as e:
        print("Loading Failed...")


def all_emp_wid():
    clearAll()
    click("All Employee")
    title = Label(contend, text="All Registered Person", font=MEDIAMFONT)
    title.grid(column=1, row=0, pady=20)
    persons = ["Himel", "Tomal", "jamal", "Habib", "Walid", "Kabir", "Mahir", "Ruma", "Zeen"]
    r=1;
    c=0
    for person in persons:

        Label(contend, text=person).grid(row=r, column=c, padx=10, pady=10)
        c += 1
        if c == 4:
            r += 1
            c = 0


def unknown_person_wid():
    clearAll()
    click("Unknown Person")
    title = Label(contend, text="Unknown Person", font=MEDIAMFONT)
    title.pack(pady=20)


root.minsize(900,500)
root.title("Dashboard")
# Felt Menu sidebar
menu_panel = PanedWindow(bg="gray")
menu_panel.pack(fill=BOTH, expand=2)
# Menu panel content
left_label = Frame(menu_panel)
menu_panel.add(left_label)
# Add Person
btn_add_per = Button(left_label, text="Add New Person", width=20, command=add_emp_frame)
btn_add_per.pack(pady=5, padx=5)

btn_Unauth_acc = Button(left_label, text="Unauthorized Access", command=unauth_acc_wid, width=20)
btn_Unauth_acc.pack(pady=5, padx=5)

btn_auth_acc = Button(left_label, text="Authorized Access", command=auth_acc_wid, width=20)
btn_auth_acc.pack(pady=5, padx=5)

btn_all_emp = Button(left_label, text="Organizations", command=org_wid, width=20)
btn_all_emp.pack(pady=5, padx=5)

btn_all_emp = Button(left_label, text="All Employee", command=all_emp_wid, width=20)
btn_all_emp.pack(pady=5, padx=5)

btn_unknown_per = Button(left_label, text="Unknown Person", command=unknown_person_wid,  width=20)
btn_unknown_per.pack(pady=5, padx=5)


content_panel= PanedWindow(menu_panel, orient=HORIZONTAL)

menu_panel.add(content_panel)

contend = Frame(content_panel,)


content_panel.add(contend)


root.mainloop()