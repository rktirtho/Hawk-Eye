from tkinter import *
from PIL import ImageTk, Image
import os

from tkinter.filedialog import askopenfilename


def donothing():
    print("It's yet to come !")


def findfile():
    # top.withdraw()
    # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

    img = Image.open(filename)
    img.show()


top = Tk()

top.title("Brain Segmentation")
top.configure(background='black')
top.minsize(400, 400)
top.maxsize(500, 500)

menu = Menu(top, background='#000099', foreground='white', activebackground='#004c99', activeforeground='white')
top.config(menu=menu)
submenu = Menu(top, background="#fff719", foreground='black', activebackground='#eae319', activeforeground='black')
menu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="New Project", command=donothing)
submenu.add_command(label="Find more", command=donothing)
# submenu.add_separator()


view = Menu(menu, background="#03a303", foreground='black', activebackground='#05bc05', activeforeground='black')
menu.add_cascade(label="View", menu=view)
view.add_command(label="View Source", command=donothing)

exit = Menu(menu, background="#d60202", foreground='white', activebackground='#7c2704', activeforeground='white')
menu.add_cascade(label="Exit", menu=exit)
exit.add_command(label="Exit", command=top.quit)

label1 = Label(top, text="First You need to select a file !\nPress the button to select a file", bg="red", fg="black")
label1.pack(padx=50, pady=10)

button1 = Button(top, text="Browse File", bg="green", fg="black", command=findfile)
button1.pack(padx=50, pady=40)

img = Image.open("brain.png")
img2 = img.resize((200, 200), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(img2)

panel = Label(top, image=img3)
panel.pack()

# img = ImageTk.PhotoImage(Image.open("brain.png"))
# img.resize((40,40),Image.ANTIALIAS)
# panel = Label(top, image = img)
# panel.pack()

top.mainloop()