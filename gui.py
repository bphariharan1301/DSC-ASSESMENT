from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, StringVar, RIGHT
from tkinter.constants import BOTTOM
from tkinter.ttk import Frame, Label, Entry, Button


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Convert the Hour:Minutes format to seconds")
        self.pack(fill=BOTH, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Hours :", width=10)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(frame1)
        entry1.pack(fill=X, padx=5, expand=True)

        frame2 = Frame(self)
        frame2.pack(fill=X)

        lbl2 = Label(frame2, text="Mintues :", width=10)
        lbl2.pack(side=LEFT, padx=5, pady=5)

        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=BOTH, expand=True)

        myText=StringVar();

        lbl3 = Label(frame3, text="Seconds:", width=10)
        lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)
        result=Label(frame3, text="", textvariable=myText)

        # txt = Text(frame3)
        # txt.pack(fill=BOTH, pady=5, padx=5, expand=True)
        def addTime():
            a = int(entry1.get())
            b = int(entry2.get())

            a = a*3600
            b = b*60
            res = a+b

            myText.set(res)


        b = Button(frame3, text="Calculate", command=addTime).pack(side=BOTTOM, padx=5, pady=5)

def main():

    root = Tk()
    root.geometry("300x300+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
