from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("Image Viewer")

my_img1 = ImageTk.PhotoImage(Image.open("Images/image 1.webp"))
my_img2 = ImageTk.PhotoImage(Image.open("Images/image 2.webp"))
my_img3 = ImageTk.PhotoImage(Image.open("Images/image 3.webp"))
my_img4 = ImageTk.PhotoImage(Image.open("Images/image 4.webp"))
my_img5 = ImageTk.PhotoImage(Image.open("Images/image 5.webp"))

def forward(x):
    global my_label
    global button_forward
    global button_backward
    my_label.grid_forget()
    my_label = Label(root, image=image_list[x-1])
    button_forward = Button(root,text=">>",command=lambda : forward(x+1) )
    button_backward = Button(root,text="<<",command=lambda : backward(x-1))

    if x==5:
        button_forward["state"]=DISABLED
    my_label.grid(row=0, column=0, columnspan=3)
    button_backward.grid(row=1, column=0, padx=20, pady=20, sticky="sew")
    button_forward.grid(row=1, column=2, padx=20, pady=20, sticky="sew")

def backward(y):
    global my_label
    global button_forward
    global button_backward
    my_label.grid_forget()
    my_label = Label(root, image=image_list[y - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(y + 1))
    button_backward = Button(root, text="<<", command=lambda: backward(y - 1))

    if y==1:
        button_backward["state"] = DISABLED
    my_label.grid(row=0, column=0, columnspan=3)
    button_backward.grid(row=1, column=0, padx=20, pady=20, sticky="sew")
    button_forward.grid(row=1, column=2, padx=20, pady=20, sticky="sew")




button_quit = Button(root,text="Exit",command=root.quit)
button_forward = Button(root,text=">>",command=lambda : forward(2) )
button_backward = Button(root,text="<<",command=backward)
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(root,image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

button_backward.grid(row=1,column=0,padx=20,pady=20,sticky="sew")
button_quit.grid(row=1,column=1, padx=20,pady=20,sticky="sew")
button_forward.grid(row=1,column=2,padx=20,pady=20,sticky="sew")



root.mainloop()