from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
web_input = Entry(width=56)
web_input.grid(column=1, row=1, columnspan=2)

#Email
username = Label(text="Email/User Name: ")
username.grid(column=0, row=2)

#text field for email
mail_input = Entry(width=56)
mail_input.grid(column=1, row=2, columnspan=2)

#password
password = Label(text="Password: ")
password.grid(column=0, row=3)

#text field for password
pass_input = Entry(width=37)
pass_input.grid(column=1, row=3)

#generation button
generation_button = Button(text="Generate Password")
generation_button.grid(column=2, row=3)

#add button
add_button = Button(text="Add", width=47)
add_button.grid(column=1, row=4, columnspan=2)
window.mainloop()
