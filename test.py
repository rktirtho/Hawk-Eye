import tkinter as tk

app = tk.Tk()
app.geometry('150x100')

chkValue = tk.BooleanVar()
chkValue.set(True)
print(chkValue.get())

chkExample = tk.Checkbutton(app, text='Check Box', var=chkValue)
chkExample.grid(column=0, row=0)

app.mainloop()
