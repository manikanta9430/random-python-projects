import tkinter
from tkinter import*
def onclick():
    print("Jan is clicked")
root=tkinter.Tk()
root.geometry("400x400")
root.configure(bg="black")
lb1=tkinter.Listbox(root)
lb1.insert(0,"Jan")
lb1.insert(1,"Feb")
lb1.insert(2,"Mar")
lb1.insert(3,"Apr")
lb1.insert(4,"May")
lb1.insert(5,"Jun")
lb1.pack(command= onclick())
root.mainloop()
