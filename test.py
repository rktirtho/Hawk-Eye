from tkinter import Tk, Label
from PIL import Image, ImageTk

root = Tk()

file = 'images/auth/3jisan.jpg'

image = Image.open(file)

zoom = 1.8

#multiple image size by zoom
pixels_x, pixels_y = tuple([int(zoom * x)  for x in image.size])

img = ImageTk.PhotoImage(image.resize((100, 100)))
label = Label(root, image=img)
label.image = img
label.pack()

root.mainloop()