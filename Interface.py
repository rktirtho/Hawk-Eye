import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Label = tk.Label(self, text="FirstPage")
        Label.place(x=230, y=230)
        Button = tk.Button(self, text="Next", command=lambda: controller.show_frame(SecondPage))
        Button.place(x=650, y=450)

        Button_back = tk.Button(self, text="Back", command=lambda: controller.show_frame(ThirdPage))
        Button_back.place(x=100, y=450)


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
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
        self.frames={}

        for F in (FirstPage, SecondPage, ThirdPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="NSEW")
        self.show_frame(FirstPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


app = Application()
app.mainloop()