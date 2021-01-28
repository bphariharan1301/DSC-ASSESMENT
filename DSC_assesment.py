from tkinter import *

def add_time():
    res=int(e1.get())*3600+int(e2.get())*60
    label_text.set(res)
 
window = Tk()

width_of_window = 300
height_of_window = 300

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_coordinate = (screen_width/2) - (width_of_window/2)
y_coordinate = (screen_height/2) - (height_of_window/2)

window.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

label_text=StringVar();
Label(window, text="Hours :").grid(row=0, sticky=W)
Label(window, text="Minutes :").grid(row=1, sticky=W)
Label(window, text="In Seconds :").grid(row=3, sticky=W)
result=Label(window, text="", textvariable=label_text).grid(row=3,column=1, sticky=W)
 
e1 = Entry(window)
e2 = Entry(window)
 
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
 
b = Button(window, text="Calculate", command=add_time)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
 
 
mainloop()









