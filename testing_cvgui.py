import cv2
import numpy as np
from tkinter import*
from PIL import Image, ImageTk

win = Tk()
win.geometry("670x600+200+30")
win.resizable(False, False)
w = 300
h = 200
color = "#581845"
frame_1 = Frame(win, width=670, height=700, bg=color).place(x=0, y=0)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()

W = 150
l_h = Scale(frame_1, label="l_h", from_=0, to=255, orient=HORIZONTAL, variable=var1, activebackground='#339999')
l_h.set(0)
l_h.place(x=10, y=10, width=W)
l_s = Scale(frame_1, label="l_s", from_=0, to=255, orient=HORIZONTAL, variable=var2, activebackground='#339999')
l_s.set(0)
l_s.place(x=170, y=10, width=W)
l_v = Scale(frame_1, label="l_v", from_=0, to=255, orient=HORIZONTAL, variable=var3, activebackground='#339999')
l_v.set(0)
l_v.place(x=330, y=10, width=W)

u_h = Scale(frame_1, label="u_h", from_=255, to=0, orient=HORIZONTAL, variable=var4, activebackground='#339999')
u_h.set(255)
u_h.place(x=10, y=80, width=W)
u_s = Scale(frame_1, label="u_s", from_=255, to=0, orient=HORIZONTAL, variable=var5, activebackground='#339999')
u_s.set(255)
u_s.place(x=170, y=80, width=W)
u_v = Scale(frame_1, label="u_v", from_=255, to=0, orient=HORIZONTAL, variable=var6, activebackground='#339999')
u_v.set(255)
u_v.place(x=330, y=80, width=W)

thresh = Scale(frame_1, label="thresh1", from_=0, to=255, orient=HORIZONTAL, variable=var7, activebackground='#339999')
thresh.set(0)
thresh.place(x=500, y=10, width=W)
thresh2 = Scale(frame_1, label="thresh2", from_=255, to=0, orient=HORIZONTAL, variable=var8, activebackground='#339999')
thresh2.set(255)
thresh2.place(x=500, y=80, width=W)


cap = cv2.VideoCapture(0)

label1 = Label(frame_1, width=w, height=h)
label1.place(x=10, y=160)
label2 = Label(frame_1, width=w, height=h)
label2.place(x=350, y=160)
label3 = Label(frame_1, width=w, height=h)
label3.place(x=10, y=370)
label4 = Label(frame_1, width=w, height=h)
label4.place(x=350, y=370)


def select_img():
    _, img = cap.read()
    img = cv2.resize(img, (w, h))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, thresh.get(), thresh2.get())
    l_b = np.array([l_h.get(), l_s.get(), l_v.get()])
    u_b = np.array([u_h.get(), u_s.get(), u_v.get()])
    mask = cv2.inRange(hsv, l_b, u_b)
    file = open('color.txt', 'w')
    file.write("l_b = " + str(l_b) + '\n' + "u_b = " + str(u_b))
    file.close()
    res = cv2.bitwise_and(img, img, mask=mask)
    rgb2 = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)

    image = Image.fromarray(rgb)
    iago = ImageTk.PhotoImage(image)
    label1.configure(image=iago)
    label1.image = iago

    image_2 = Image.fromarray(mask)
    iago_2 = ImageTk.PhotoImage(image_2)
    label2.configure(image=iago_2)
    label2.image = iago_2

    image3 = Image.fromarray(rgb2)
    iago3 = ImageTk.PhotoImage(image3)
    label3.configure(image=iago3)
    label3.image = iago3

    image4 = Image.fromarray(edges)
    iago4 = ImageTk.PhotoImage(image4)
    label4.configure(image=iago4)
    label4.image = iago4

    win.after(10, select_img)

select_img()
win.mainloop()
