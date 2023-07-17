import tkinter as tk
from tkinter import messagebox as msgbox
import pyperclip
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project


def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(2, 10)]
    password_symbol = [random.choice(symbols) for _ in range(2, 4)]
    password_numbers = [random.choice(letters) for _ in range(2, 4)]

    password_list = password_letters + password_symbol + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    input_pass.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def find_pass():
    web = input_web.get()
    try:
        with open("data.json", mode="r") as f:
            d = json.load(f)
    except FileNotFoundError:
        msgbox.showinfo(title="Error", message="Not data file found")
    else:
        if web in d:
            em = d[web]["Email"]
            ps = d[web]["Password"]
            msgbox.showinfo(title=web, message=f"Email: {em}\n Password: {ps}")
        else:
            msgbox.showinfo(title="Error", message=f"No details found for {web}.")

def save_data():
    web = input_web.get()
    email = input_email.get()
    pswrd = input_pass.get()
    new_dec = {
        web: {
            "Email": email,
            "Password": pswrd
        }
    }

    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        with open("data.json", mode="w") as file:
            json.dump(new_dec, file, indent=4)
    else:
        data.update(new_dec)

        with open("data.json", mode="w") as new_file:
            json.dump(data, new_file, indent=4)
    finally:
        input_web.delete(0, tk.END)
        input_email.delete(0, tk.END)
        input_pass.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = tk.Canvas(height=200, width=200)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website = tk.Label(text="Website: ")
website.grid(column=0, row=1)
website.focus()

input_web = tk.Entry(width=25)
input_web.grid(column=1, row=1)

search = tk.Button(text="Search", command=find_pass)
search.grid(column=2, row=1)

emai_user = tk.Label(text="Email/Username: ")
emai_user.grid(column=0, row=2)

input_email = tk.Entry(width=25)
input_email.grid(column=1, row=2)

pas = tk.Label(text="Password: ")
pas.grid(column=0, row=3)

input_pass = tk.Entry(width=25)
input_pass.grid(column=1, row=3)

gen_btn = tk.Button(text="Generate Password", bg="red", command=generate_pass)
gen_btn.grid(column=2, row=3)

add_btn = tk.Button(text="Add", width=21, command=save_data)
add_btn.grid(column=1, row=4)

window.mainloop()
