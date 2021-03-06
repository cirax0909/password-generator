from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generation():
    pass_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)

    pass_input.insert(0, f"{password}")
    pyperclip.copy(password)
# ---------------------------- SEARCH WEBSITE ------------------------------- #


def search():
    website = web_input.get()
    try:
        with open("data.json", "r") as file_data:
            data = json.load(file_data)
    except FileNotFoundError:
        messagebox.showerror(title="Message", message="File is not found")
    else:
        if website in data:
            input_email = data[website]['email']
            input_password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {input_email}\nPassword: {input_password}")
        else:
            messagebox.showerror(title="Message", message="Website is not found")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def insert():
    input_email = mail_input.get()
    input_password = pass_input.get()
    website = web_input.get()
    new_data = {website: {"email": input_email,
                          "password": input_password}}
    if len(web_input.get()) <= 0 or len(pass_input.get()) <= 0:
        messagebox.showwarning(title="Error", message="Please fill all in the information")
    else:
        try:
            with open("data.json", "r") as file_data:
                data = json.load(file_data)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file_data:
                json.dump(new_data, file_data)
        else:
            with open("data.json", "w") as file_data:
                json.dump(data, file_data, indent=4)
        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pass Word Generator")
window.config(padx=50, pady=50)

#logo
canvas = Canvas(width=200, heigh=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#website label
web_label = Label(text="Website: ")
web_label.grid(column=0, row=1)

#text field for website
web_input = Entry(width=37)
web_input.grid(column=1, row=1)

#Email
username = Label(text="Email/User Name: ")
username.grid(column=0, row=2)

#text field for email
mail_input = Entry(width=56)
mail_input.insert(0, "tich@gmail.com")
mail_input.grid(column=1, row=2, columnspan=2)

#password
password = Label(text="Password: ")
password.grid(column=0, row=3)

#text field for password
pass_input = Entry(width=37)
pass_input.grid(column=1, row=3)

#generation button
generation_button = Button(text="Generate Password", command=generation)
generation_button.grid(column=2, row=3)

#add button
add_button = Button(text="Add", width=47, command=insert)
add_button.grid(column=1, row=4, columnspan=2)

#search button
search_button = Button(text="Search", width=15, command=search)
search_button.grid(column=2, row=1)
window.mainloop()
