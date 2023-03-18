from tkinter import*
from tkinter.ttk import*
from time import strftime
#setting up the tkinter window and title
root=Tk()
root.title('digital clock')
#This method counttime gives the format of the label and it
#refreshes the label every one thousand mile-seconds
def counttime():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,counttime)
#Here the label is placed inside the window position 
label=Label(root,font=("ds-digital",70),background="black",foreground="green")
label.pack(anchor="center")
#This is the first call of countime method
counttime()

