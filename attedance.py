from tkinter import *
from tkinter import ttk
class AttendanceMan(Tk):

    def make_frame(self):
        self.upper_frame = Frame(self, bg="black")
        self.label = Label(self.upper_frame, text="Names", bg="yellow")
        self.label.place(relx=0.2, rely=0.5)
        co = IntVar()
        self.label = Label(self.upper_frame, text="State", bg="yellow")
        self.label.place(relx=0.55, rely=0.5)
        self.day = ttk.Combobox(self.upper_frame, textvariable=co, state="readonly")
        self.day["values"] = ("monday","Tuesday", "Wednesday", "Thursday", "Friday")
        self.day.current(0)
        self.day.place(relx=0.05, rely=0.2)
        self.upper_frame.place(relx=0, rely=0, relheight=0.05, relwidth=1)

        #self.frame_left = Frame(self,bg="blue")
        #self.frame_left.place(relx=0, rely=0.05, relheight=1, relwidth=0.5)

class NamePart(AttendanceMan):

    def names_placement(self):
        y = 0
        self.frame_name = Frame(self)
        self.color = ["grey", "white"]
        name = "EMEHINOLA SAMUEL"
        for i in range(3,20):
            if y > 1:
                y = 0
            self.label = Label(self.frame_name, text=name, bg=self.color[y])
            self.label.grid(row=i,column=0)
            y += 1
        self.frame_name.place(relx=0, rely=0.085, relheight=1, relwidth=0.5)

class Week(NamePart):

    def monday(self):
        self.week_frame = Frame(self, bg="green")
        x = 0.5
        y = 50
        radVar = StringVar()

        for i in range(3,30):
            state = ttk.Combobox(self.week_frame, state="readonly", textvariable=i)
            state["values"] = ("Present", "Absent")
            state.current(0)
            state.grid(row=i, column=0)
            y += 1

        self.color = ["grey", "white"]
        # admission no
        self.week_label = Label(self.week_frame, text="Registration No", bg="grey")
        self.week_label.grid(row=0, column=0)
        reg = "9536868GF"
        for m in range(3,30):
            if y > 1:
                y = 0
            self.label = Label(self.week_frame, text=f"{reg}{m}", bg=self.color[y])
            self.label.grid(row=m,column=11)
            y += 1

        self.week_frame.place(relx=0.5, rely=0.05, relheight=1, relwidth=0.3)
        win.names_placement()

class Week2():

    """
    weldone
    """

win = Week()
win.make_frame()
win.geometry("800x1000")
win.monday()

win.mainloop()