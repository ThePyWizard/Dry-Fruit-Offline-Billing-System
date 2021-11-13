from PIL import ImageTk,Image
from tkinter import*

root=Tk()

root.configure(bg="red")

root.title("Image placement")
root.iconbitmap(r"E:\JISHNU'S STUDIOUS WORLD\CS EXPERT LESSONS\PROJECT\shopping_cart.ico")

my_img=ImageTk.PhotoImage(file=r"E:\JISHNU'S STUDIOUS WORLD\CS EXPERT LESSONS\PROJECT\nuts 2.jpg")
my_label=Label(root,image=my_img,width=250,height=250)
my_label.pack()
root.mainloop()
