import urllib.request, urllib.parse, urllib.error
import requests
import json
import ssl
from tkinter import *

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

# class Security:
#     def __init__(self, id, name, email, username, password,org_id,last_excess, join_date):
#         self.id = id;
#         self.name = name
#         self.email =  email
#         self.username=username
#         self.password =  password
#         self.last_access = last_excess
#         self.org_id =  org_id
#         self.join_date = join_date
#
#     def get_id(self):
#         return self.id
#
#     def set_id(self, id):
#         self.id = id;
#
#     def get_name(self):
#         return self.name
#
#     def set_id(self, name):
#         self.name = name;
#
#     def get_email(self):
#         return self.email
#
#     def set_email(self, email):
#         self.email = email;
#
#     def get_username(self):
#         return self.username
#
#     def set_id(self, username):
#         self.username = username;
#
#     def get_password(self):
#         return self.password
#
#     def set_password(self, password):
#         self.password = password;
#
#     def get_org_id(self):
#         return self.org_id
#
#     def set_org_id(self, org_id):
#         self.org_id = org_id;
#
#     def get_last_excess(self):
#         return self.last_access
#
#     def set_last_excess(self, time):
#         self.last_access = time;
#
#     def get_join_date(self):
#         return self.join_date
#
#     def set_join_date(self, date):
#         self.join_date = date;
#
#
#
# try:
#     utr = requests.get('http://127.0.0.1:8080/api/organizations')
#     api = json.loads(utr.content)
#     for data in api:
#         print(data['name'])
#         print("")
#     # print(api)
# except Exception as e:
#     print("Loading Failed...")
class Test:
    def __init__(self):
        self.root = Tk()
        self.root.resizable(width=0, height=0)
        self.root.title("some application")

        # menu left
        self.menu_left = Frame(self.root, width=150, bg="#ababab")
        self.menu_left.grid(row=0, column=0, rowspan=2, sticky="ns")

        self.menu_left_upper = Frame(self.menu_left, width=150, height=150, bg="red")
        self.menu_left_upper.grid(row=0, column=0)

        # this label breaks the design
        #self.test = tk.Label(self.menu_left_upper, text="test")
        #self.test.pack()

        self.menu_left_lower = Frame(self.menu_left, width=150, bg="blue")
        self.menu_left_lower.grid(row=1, column=0)

        # right area
        self.some_title_frame = Frame(self.root, bg="#dfdfdf")
        self.some_title_frame.grid(row=0, column=1, sticky="we")

        self.some_title = Label(self.some_title_frame, text="some title", bg="#dfdfdf")
        self.some_title.pack()

        self.canvas_area = Canvas(self.root, width=500, height=400, background="#ffffff")
        self.canvas_area.grid(row=1, column=1)

        self.root.mainloop()

Test()
# import tkinter as Tk
#
# def disappear():
#     but.grid_forget()
#
# root = Tk.Tk()
#
# canvas = Tk.Canvas(root, bg = 'black', width = 500, height = 500)
# canvas.grid(row = 0, column = 0)
#
# frame = Tk.Frame(bg = 'red')
# canvas.create_window(0, 0, window = frame, anchor = Tk.NW)
#
# but = Tk.Button(frame, text = 'Disappear', command = disappear)
# but.grid(row = 0, column = 0)
#
# root.mainloop()



# try:
#     import Tkinter as tk
# except:
#     import tkinter as tk
#
#
# class SampleApp(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         self._frame = None
#         self.switch_frame(StartPage)
#
#     def switch_frame(self, frame_class):
#         new_frame = frame_class(self)
#         if self._frame is not None:
#             self._frame.destroy()
#         self._frame = new_frame
#         self._frame.pack()
#
#
# class StartPage(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         tk.Label(self, text="Start page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
#         tk.Button(self, text="Go to page one",
#                   command=lambda: master.switch_frame(PageOne)).pack()
#         tk.Button(self, text="Go to page two",
#                   command=lambda: master.switch_frame(PageTwo)).pack()
#
#
# class PageOne(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         tk.Frame.configure(self, bg='blue')
#         tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
#         tk.Button(self, text="Go back to start page",
#                   command=lambda: master.switch_frame(StartPage)).pack()
#
#
# class PageTwo(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)
#         tk.Frame.configure(self, bg='red')
#         tk.Label(self, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
#         getButton(self, master)
#
# def getButton(self,master):
#     tk.Button(self, text="Go back to start page",
#               command=lambda: master.switch_frame(StartPage)).pack()
#
# if __name__ == "__main__":
#     app = SampleApp()
#     app.mainloop()

# import PIL
# from PIL import Image,ImageTk
# import pytesseract
# import cv2
# from tkinter import *
# width, height = 800, 600
# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
#
# root = Tk()
# root.bind('<Escape>', lambda e: root.quit())
# lmain = Label(root)
# lmain.pack()
#
# def show_frame():
#     _, frame = cap.read()
#     frame = cv2.flip(frame, 1)
#     cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
#     img = PIL.Image.fromarray(cv2image)
#     imgtk = ImageTk.PhotoImage(image=img)
#     lmain.imgtk = imgtk
#     lmain.configure(image=imgtk)
#     lmain.after(10, show_frame)
#
# show_frame()
# root.mainloop()