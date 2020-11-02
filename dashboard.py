# Dashboard for this project
# This is the main part of this system
# Alter successfully login user will come to there.
# Actually this UI handle all kinds of Data
from tkinter import *

LARGEFONT = ("Verdana", 30)
MEDIAMFONT = ("Verdana", 20)
SMALLFONT = ("Verdana", 16)


root = Tk()
def click(self):
    root.title()
root.minsize(900,500)
root.title("Dashboard")
# Felt Menu sidebar
menu_panel = PanedWindow(bg="gray")
menu_panel.pack(fill=BOTH, expand=2)
# Menu panel content
left_label = Frame(menu_panel)
menu_panel.add(left_label)
# Add Person
btn_add_per = Button(left_label, text="Add New Person", command=click)
btn_add_per.pack()

btn_add_per2 = Button(left_label, text="Add New Person")
btn_add_per2.pack()


content_panel= PanedWindow(menu_panel, orient=HORIZONTAL)
menu_panel.add(content_panel)

contend = Frame(content_panel,)
title = Label(contend, text = "Add Person", font=LARGEFONT)
title.pack(pady=20)

lb_emp_id = Label(contend, text="Employee ID")
lb_emp_id.pack()
ent_em_id = Entry(contend,)
ent_em_id.pack()

lb_name = Label(contend, text="Employee Name*")
lb_name.pack()
ent_name = Entry(contend,)
ent_name.pack()

lb_org = Label(contend, text="Organization ID*")
lb_org.pack()
ent_org_id = Entry(contend,)
ent_org_id.pack()

Button(contend, text="Load Image*").pack(pady=10)
Button(contend, text="Save").pack()


content_panel.add(contend)

root.mainloop()