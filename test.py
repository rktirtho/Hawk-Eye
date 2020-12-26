import tkinter as tk

OptionList = [
"Aries",
"Taurus",
"Gemini",
"Cancer"
]

app = tk.Tk()

app.geometry('100x200')

variable = tk.StringVar(app)
variable.set(OptionList[0])

opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack()

app.mainloop()
