# Dashboard for this project
# This is the main part of this system
# Alter successfully login user will come to there.
# Actually this UI handle all kinds of Data
from tkinter import *


root = Tk()
def click(self):
    root.title()
root.minsize(900,500)
root.title("Dashboard")
# Felt Menu sidebar
menu_panel = PanedWindow(bg="gray")
menu_panel.pack(fill=BOTH, expand=1)
# Menu panel content
left_label = Frame(menu_panel)
menu_panel.add(left_label)
# Add Person
btn_add_per = Button(left_label, text="Add New Person", command=click)
btn_add_per.pack(pady=10, padx=20)

btn_add_per2 = Button(left_label, text="Add New Person")
btn_add_per2.pack()


content_panel= PanedWindow(menu_panel, orient=HORIZONTAL)
menu_panel.add(content_panel)

top = Label(content_panel, text="Top Panner")
content_panel.add(top)

root.mainloop()