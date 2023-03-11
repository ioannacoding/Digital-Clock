from tkinter import*
from tkinter.ttk import*
from time import strftime
root=Tk()
root.title('digital clock')

def counttime():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,counttime)
    
label=Label(root,font=("ds-digital",70),background="black",foreground="green")
label.pack(anchor="center")
counttime()
mainloop()
