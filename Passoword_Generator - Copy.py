from tkinter import *
import string
import random



#password generation function based on inputs

def password_gen():
    password=""
    if sp_character_value.get()==1:
        for i in range(int(password_length_value.get())):
            password+=random.choice(string.ascii_letters + "!@#$%&" + string.digits)
    else:
        for i in range(int(password_length_value.get())):
            password+=random.choice(string.ascii_letters + string.digits)
    result.config(text=f"{password}")
    clipboard.config(state="normal")



#restrict function for entering only numbers

def checknum(a):
    return a.isdigit()



#OK button function

def OK():
    if len(password_length_value.get())!=0:
        password_length_value.config(state="disabled")
        generate.config(state="normal")



#copy function for copying elements to clipboard

def copy():
    windows.clipboard_append(result.cget("text"))



#reset button function

def reset():
    password_length_value.config(state='normal')
    password_length_value.delete(0,END)
    sp_character_value.set(0)
    generate.config(state="disabled")
    result.config(text="")
    clipboard.config(state="disabled")



#main window

windows=Tk()
windows.title("Password Generator")
windows.geometry("300x300")
windows.resizable(False,False)
icon=PhotoImage(file="D:\\Main\\Work\\Programs\\Python\\Projects\\Password Generator\\icon.png")
windows.iconphoto(True,icon)
body_font=("Arial, 14")



#label for "Enter passowrd length"

password_length_label=Label(windows,
                            text="Enter password length",
                            font=body_font)
password_length_label.pack()



#entry point for password length

check=(windows.register(checknum),"%S")
password_length_value=Entry(windows,
                            font=body_font,
                            validate="key",
                            validatecommand=check)
password_length_value.pack()



#OK button

step1=Button(windows,
             text="OK",
             font=body_font,
             command=OK)
step1.pack(pady=7)



#Checkbox for special characters

sp_character_value=IntVar()
sp_character=Checkbutton(windows,
                        text="Special Characters required?",
                        font=body_font,
                        variable=sp_character_value,
                        onvalue=1,
                        offvalue=0)
sp_character.pack()



#Generate button

generate=Button(windows,
                text="Generate",
                font=body_font,
                command=password_gen,
                state="disabled")
generate.pack()



#Result space

result=Label(windows,
            text="",
            font=body_font)
result.pack()


#Clipboard button

clipboard=Button(windows,
                 text="Copy",
                 font="body_font",
                 command=copy,
                 state="disabled")
clipboard.pack()



#Reset Button

reset_icon=PhotoImage(file="D:\\Main\\Work\\Programs\\Python\\Projects\\Password Generator\\reset.png")
reset=Button(windows,
            image=reset_icon,
            command=reset)
reset.pack(pady=5)



#Keeping windows running

windows.mainloop()