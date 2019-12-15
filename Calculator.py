import tkinter as tk
#from math import sin, cos, tan

master = tk.Tk()
master.geometry("312x324")
master.title("Calculator")
master.resizable(0,0)

entry_frame = tk.Frame(master, bg="black")
entry_frame.place(relx=0, rely=0, relheight=0.2, relwidth=1)

         # creating buttons frame

btn_frame = tk.Frame(master, bg="grey")
btn_frame.place(relx=0, rely=0.21, relwidth=1, relheight=1)

text_var = tk.StringVar()
expression = text_var.get()

# button click function
def button_click(number):
	if text_var.get() == "Syntax Error":
		clear()
	expression = text_var.get()
	expression += str(number)
	text_var.set(expression)

# equal to button function
def equal_to():
    try:
        global expression
        expression = text_var.get()
        result = eval(str(expression))
        text_var.set(result)

        expression = text_var.get()

    except :
        text_var.set("Syntax Error")

        expression = ""

# clear button function
def clear():
    global expression

    expression = ""
    text_var.set(expression)

# delete button function
def delete():
    global expression

    if text_var.get() == "Syntax Error":
        entry.delete(0, tk.END)
    numbers = text_var.get()
    expression = numbers[0:-1]
    text_var.set(expression)

entry = tk.Entry(entry_frame, font=("arial", 30, "bold"), justify='right', border=1, textvariable=text_var, state="readonly")
entry.place(relx=0.01, rely=0, relwidth=0.98, relheight=0.9)

        # creating buttons

clear_but = tk.Button(btn_frame, bg="#eee", border=1, text='C', command=clear)
clear_but.place(relx=0.01, rely=0, relwidth=0.48, relheight=0.1)

div_but = tk.Button(btn_frame, bg="#eee", border=1, text='/', cursor='hand2', command=lambda:button_click('/'))
div_but.place(relx=0.49, rely=0, relwidth=0.24, relheight=0.1)

sub_but = tk.Button(btn_frame, bg="#eee", border=1, text='-', command=lambda:button_click('-'))
sub_but.place(relx=0.73, rely=0, relwidth=0.26, relheight=0.1)

seven_but = tk.Button(btn_frame, bg="#eee", border=1, text='7', command=lambda:button_click('7'))
seven_but.place(relx=0.01, rely=0.1, relwidth=0.24, relheight=0.15)

eight_but = tk.Button(btn_frame, bg="#eee", border=1, text='8', command=lambda:button_click('8'))
eight_but.place(relx=0.25, rely=0.1, relwidth=0.24, relheight=0.15)

nine_but = tk.Button(btn_frame, bg="#eee", border=1, text='9', command=lambda:button_click('9'))
nine_but.place(relx=0.49, rely=0.1, relwidth=0.24, relheight=0.15)

mult_but = tk.Button(btn_frame, bg="#eee", border=1, text='*', command=lambda:button_click('*'))
mult_but.place(relx=0.73, rely=0.1, relwidth=0.26, relheight=0.15)

four_but = tk.Button(btn_frame, bg="#eee", border=1, text='4', command=lambda:button_click('4'))
four_but.place(relx=0.01, rely=0.25, relwidth=0.24, relheight=0.15)

five_but = tk.Button(btn_frame, bg="#eee", border=1, text='5', command=lambda:button_click('5'))
five_but.place(relx=0.25, rely=0.25, relwidth=0.24, relheight=0.15)

six_but = tk.Button(btn_frame, bg="#eee", border=1, text='6', command=lambda:button_click('6'))
six_but.place(relx=0.49, rely=0.25, relwidth=0.24, relheight=0.15)


one_but = tk.Button(btn_frame, bg="#eee", border=1, text='1', command=lambda:button_click('1'))
one_but.place(relx=0.01, rely=0.4, relwidth=0.24, relheight=0.15)

two_but = tk.Button(btn_frame, bg="#eee", border=1, text='2', command=lambda:button_click('2'))
two_but.place(relx=0.25, rely=0.4, relwidth=0.24, relheight=0.15)

three_but = tk.Button(btn_frame, bg="#eee", border=1, text='3', command=lambda:button_click('3'))
three_but.place(relx=0.49, rely=0.4, relwidth=0.24, relheight=0.15)

plus_but = tk.Button(btn_frame, bg="#eee", border=1, text='+', command=lambda:button_click('+'))
plus_but.place(relx=0.73, rely=0.4, relwidth=0.26, relheight=0.15)

zero_but = tk.Button(btn_frame, bg="#eee", border=1, text='0', command=lambda:button_click('0'))
zero_but.place(relx=0.01, rely=0.55, relwidth=0.24, relheight=0.15)

point_but = tk.Button(btn_frame, bg="#eee", border=1, text='.', command=lambda:button_click('.'))
point_but.place(relx=0.25, rely=0.55, relwidth=0.24, relheight=0.15)

equal_but = tk.Button(btn_frame, border=1, text='=', command=equal_to, bg="pink")
equal_but.place(relx=0.49, rely=0.55, relwidth=0.5, relheight=0.15)

    
ex_but = tk.Button(btn_frame, bg="#eee", border=1, text='del', command=delete)
ex_but.place(relx=0.73, rely=0.25, relwidth=0.26, relheight=0.15)

label = tk.Label(master, text="4G-LTE powered by Samuel", fg="blue")
label.place(relx=0.2, rely=0.95)

master.mainloop()
