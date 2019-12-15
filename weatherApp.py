from tkinter import *

class Weather(Tk):

        
# frame for entry box and button
    def make_frame(self):

        self.entry_frame = Frame(self, bg="#c180ff")

        entry_var = StringVar()
        entry = Entry(self.entry_frame, textvariable=entry_var, font=("arial",15))
        entry.place(relx=0.01, rely=0.05, relheight=0.9, relwidth=0.6)

        self.entry_frame.place(relx=0.1, rely=0.1, relheight=0.1, relwidth=0.8)

# label to get weather results
    def label_display(self):
        
        self.text_frame = Frame(self, bg="#c180ff")
        self.text_frame.place(relx=0.1, rely=0.25, relheight=0.7, relwidth=0.8)
        
        txt_lab = Label(self.text_frame)
        txt_lab.place(relx=0.1, rely=0.1, relheight=0.8, relwidth=0.8)
        

root = Weather()

root.geometry("500x500")
root.title("Weather App")

image = PhotoImage(file="sololearn.png")
background_image = Label(root, image=image)
        
background_image.place(relx=0,rely=0, relheight=1, relwidth=1)

root.label_display()
root.make_frame()

button = Button(root.entry_frame, text="Get Weather", fg="blue", border="5")
button.place(relx=0.63, rely=0.05, relheight=0.9, relwidth=0.35)

root.mainloop()