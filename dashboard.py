# Dashboard for this project
# This is the main part of this system
# Alter successfully login user will come to there.
# Actually this UI handle all kinds of Data
from tkinter import *

menu = ["Text1", "rtjke"]

root = Tk()
root.minsize(900,500)
# Felt Menu sidebar
panel_1 = PanedWindow(bg="gray")
panel_1.pack(fill=BOTH, expand=1)
# Menu panel content
left_label = Frame(panel_1)
panel_1.add(left_label)
# Add Person
btn_add_per = Button(left_label, text="Add New Person")
btn_add_per.pack()

btn_add_per2 = Button(left_label, text="Add New Person")
btn_add_per2.pack()


panel_2= PanedWindow(panel_1, orient=HORIZONTAL)
panel_1.add(panel_2)

top = Label(panel_2,text="Top Panner")
panel_2.add(top)

root.mainloop()