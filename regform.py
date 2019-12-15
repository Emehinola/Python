import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import csv
import re

win = tk.Tk()
win.title('PYTHON COURSE REG FORM')
win.geometry('400x400')

frame = tk.Frame(win, bg='black')
frame.place(relx=0, rely=0, relheight=1, relwidth=1)

fullname_label = tk.Label(frame, text='Full Name', bg='#80c1ff')
fullname_label.place(relx=0.1, rely=0.1)

fullname_var = tk.StringVar()
fullname = tk.Entry(frame, textvariable=fullname_var, width=20)
fullname.place(relx=0.35, rely=0.1, relheight=0.046)

email_lab = tk.Label(frame, text='Email', bg='#80c1ff')
email_lab.place(relx=0.1, rely=0.2, relheight=0.046)

email_var = tk.StringVar()
email = tk.Entry(frame, textvariable=email_var, width=20)
email.place(relx=0.35, rely=0.2, relheight=0.046)

phone_lab = tk.Label(frame, text='Phone', bg='#80c1ff')
phone_lab.place(relx=0.1, rely=0.3)

phone_var = tk.StringVar()
phone_number = tk.Entry(frame, textvariable=phone_var, width=20)
phone_number.place(relx=0.35, rely=0.3, relheight=0.046)

gender_label = tk.Label(frame, text='Gender', bg='#80c1ff')
gender_label.place(relx=0.1, rely=0.4)

gender_var = tk.StringVar()
gender = ttk.Combobox(frame, textvariable=gender_var, state='readonly', width=5)
gender['values'] = ('Male', 'Female')
gender.current(0)
gender.place(relx=0.35, rely=0.4)

dob_label = tk.Label(frame, text='D O B', bg='#80c1ff')
dob_label.place(relx=0.1, rely=0.5)

day_label_var = tk.IntVar()
day_combo = ttk.Combobox(frame, textvariable=day_label_var, state='readonly') 
day_combo['values'] = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
day_combo.current(0)
day_combo.place(relx=0.35, rely=0.5, relwidth=0.15)

m_var = tk.IntVar()
month_combo = ttk.Combobox(frame, textvariable=m_var, state='readonly')
month_combo['values'] = (1,2,3,4,5,6,7,8,9,10,11,12)
month_combo.current(0)
month_combo.place(relx=0.5, rely=0.5, relwidth=0.15)

y_var = tk.IntVar()
year_combo = ttk.Combobox(frame, textvariable=y_var, state='readonly')
year_combo['values'] = (1999, 2000, 2001, 2002, 2003)
year_combo.current(0)
year_combo.place(relx=0.65, rely=0.5, relwidth=0.2)

language_label = tk.Label(frame, text='Choose your programming language(s)', bg='#80c1ff')
language_label.place(relx=0.1, rely=0.6)

py_var = tk.IntVar()
py_but = ttk.Checkbutton(frame, text='Pyhon', variable=py_var)
py_but.place(relx=0.3, rely=0.7)

jav_var = tk.StringVar()
jav_but = ttk.Checkbutton(frame, text='Java', variable=jav_var)
jav_but.place(relx=0.6, rely=0.7)

count_lab = tk.Label(frame, text='Country', bg='#80c1ff')
count_lab.place(relx=0.1, rely=0.8)

count = ["Algeria", "Moscow", "Nigeria", "China", "USA", "Korea"]
count_var = tk.StringVar()
country_combo = ttk.Combobox(frame, textvariable=count_var, state='readonly')
country_combo['values'] = [i for i in count]
country_combo.current(0)
country_combo.place(relx=0.35, rely=0.8)


def submit_but():
    timenow = datetime.date.today()
    thentime = datetime.date(y_var.get(), m_var.get(), day_label_var.get())
    current_time = timenow.year - thentime.year
    age = current_time

    if not fullname_var.get():
        tk.messagebox.showwarning('Warning', 'Please enter your full names')
        return fullname_var
    
    if not phone_var.get():
        tk.messagebox.showwarning('Warning', 'Please enter your phone number')
        return phone_var
    if not re.match(r"\d{3}-\d{4}-\d{2,3}", phone_var.get()):
    		tk.messagebox.showwarning("Watning", "Invalid phone format")
    		return phone_var
    	  
    
    
    if not email_var.get():
        tk.messagebox.showwarning('Warning', 'Please enter your email')
        return email_var

#    result = (f"Time submitted: {datetime.datetime.now()} \n \nWelcome, {fullname_var.get()} \nName: {fullname_var.get()} \nEmail: {email_var.get()} \nGender: {gender_var.get()} \nPhone: {phone_var.get()} \nLanguages: {py_var.get()} \nAge: {age} years")

    with open("prog_file.csv", "r") as num:
       reader = csv.DictReader(num)
       for phone in reader:
       	ph = phone["Phone number"]
       	if phone_var.get() in ph:
            	tk.messagebox.showwarning("Warning", "Contact has been used by another user")
            	return phone_var

    with open("prog_file.csv", "a") as tkform:
    	fieldnames = ["Name", "Phone number", "Country", "Age"]
    	writer = csv.DictWriter(tkform, fieldnames=fieldnames)
    	#writer.writeheader()
    	writer.writerow({"Name":fullname_var.get(), "Phone number":phone_var.get(), "Country":count_var.get(), "Age":age})
        

    fullname.delete(0, tk.END)
    email.delete(0, tk.END)
    phone_number.delete(0, tk.END)

sub_button = tk.Button(frame, text="Submit", bg="grey", command=submit_but)
sub_button.place(relx=0.35, rely=0.9)


win.mainloop()