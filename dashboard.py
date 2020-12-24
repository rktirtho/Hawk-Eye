# Dashboard for this project
# This is the main part of this system
# Alter successfully login user will come to there.
# Actually this UI handle all kinds of Data
from tkinter import *
import json
import requests
from dbh_organization import OrganizationDbHelper
from dbh_emp import EmployeeDBHelper
from dbh_person_reg import AuthorizedDbHelper

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

def all_auth_person_wid():

    click("Authorized Access")
    title = Label(contend, text="Authorized Person", font=MEDIAMFONT)
    title.grid(row=0, column=0, columnspan=4, pady=20)
    auth_person = AuthorizedDbHelper()
    orgs = auth_person.find_all_details()
    i = 2
    c = 0
    print(orgs[1])
    Label(contend, text="#Id", padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=0, pady=10)
    Label(contend, text="Name", padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=1, pady=10)
    Label(contend, text='Organization', padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=2)
    # Label(contend, text='Address', padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=3)
    # Label(contend, text='Join Date', padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=4)

    for org in orgs:
        Label(contend, text=org.get_id(), padx=20).grid(row=i, column=0, pady=10)
        Label(contend, text=org.get_name(), padx=20).grid(row=i, column=1, pady=10)
        Label(contend, text=org.get_organization(), padx=20).grid(row=i, column=2)
        # Label(contend, text=org.get_address(), padx=20).grid(row=i, column=3)
        # Label(contend, text=org.get_reg_time(), padx=20).grid(row=i, column=4)
        i += 1


def org_wid():
    click("Organizations")
    title = Label(contend, text="All Organization", font=MEDIAMFONT)
    title.grid(row=0, column=0, columnspan=4, pady=20)
    org = OrganizationDbHelper()
    orgs = org.find_all()
    i=2
    c=0
    print(orgs[1])
    Label(contend, text="#Id", padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=0, pady=10)
    Label(contend, text="Name", padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=1, pady=10)
    Label(contend, text='Woner', padx=20,font=MEDIAMFONT_BOLD).grid(row=1, column=2)
    Label(contend, text='Address', padx=20,font=MEDIAMFONT_BOLD).grid(row=1, column=3)
    Label(contend, text='Registration', padx=20,font=MEDIAMFONT_BOLD).grid(row=1, column=4)

    for org in orgs:
        Label(contend, text=org.get_id(), padx=20).grid(row=i,column=0, pady=10)
        Label(contend, text=org.get_name(), padx=20).grid(row=i,column=1, pady=10)
        Label(contend, text=org.get_woner(),padx=20).grid(row=i,column=2)
        Label(contend, text=org.get_address(),padx=20).grid(row=i,column=3)
        Label(contend, text=org.get_reg_time(),padx=20).grid(row=i,column=4)
        i+=1




def all_emp_wid():
    clearAll()
    click("All Employee")
    title = Label(contend, text="All Registered Person", font=MEDIAMFONT)
    title.grid(column=1, row=0, pady=20)
    emp_helper = EmployeeDBHelper()
    persons = emp_helper.find_all()
    i=2;
    c=0
    Label(contend, text="#Id", padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=0, pady=10)
    Label(contend, text="Name", padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=1, pady=10)
    Label(contend, text='Email', padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=2)
    Label(contend, text='Address', padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=3)
    Label(contend, text='Join Data', padx=20, font=MEDIAMFONT_BOLD).grid(row=1, column=4)

    for person in persons:
        Label(contend, text=person.get_id(), padx=20).grid(row=i, column=0, pady=10)
        Label(contend, text=person.get_name(), padx=20).grid(row=i, column=1, pady=10)
        Label(contend, text=person.get_email(), padx=20).grid(row=i, column=2)
        Label(contend, text=person.get_join_date(), padx=20).grid(row=i, column=3)
        # Label(contend, text=person.last_excess(), padx=20).grid(row=i, column=4)
        i += 1


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

btn_auth_person = Button(left_label, text="Authorized Person", command=all_auth_person_wid, width=20)
btn_auth_person.pack(pady=5, padx=5)

btn_unknown_per = Button(left_label, text="Unknown Person", command=unknown_person_wid,  width=20)
btn_unknown_per.pack(pady=5, padx=5)


content_panel= PanedWindow(menu_panel, orient=HORIZONTAL)

menu_panel.add(content_panel)

contend = Frame(content_panel,)


content_panel.add(contend)


root.mainloop()