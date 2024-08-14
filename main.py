
__author__ = "Walter Reeves"

from secrets import choice
from string import ascii_letters, digits
from tkinter import Button, Canvas, Entry, Label, PhotoImage, StringVar, Tk


def generate_password(password_characters=12):
    """Generates a random password."""
    punctuation = "!@#$%^&*"
    alphabet = ascii_letters + digits + punctuation
    new_password = "".join(choice(alphabet) for _ in range(password_characters))

    password.delete(0, 'end')
    password.insert(0, new_password)

    window.clipboard_clear()
    window.clipboard_append(new_password)

    label_clipboard.config(text="Password copied to clipboard!")
    window.after(3000, hide_clipboard_label)


def get_credentials():
    credentials.append(user.get())
    credentials.append(pwd.get())

    site_credentials[name.get()] = credentials

    print(site_credentials)

    site_name.delete(0, 'end')
    username.delete(0, 'end')
    password.delete(0, 'end')


def reveal_text(event):
    password.config(show='')


def hide_text(event):
    password.config(show='*')


def hide_clipboard_label():
    label_clipboard.config(text="")


credentials = []
site_credentials = {}

window = Tk()
window.title("Password Manager")
window.geometry("700x500")

name = StringVar()
user = StringVar()
pwd = StringVar()
name.set("")
user.set("")
pwd.set("")

canvas = Canvas(window, width=700, height=500, background="black")

logo = PhotoImage(file="logo.png")
canvas.create_image(350, 150, image=logo)
canvas.pack()

# ========================= LABELS ========================= #
label_site_name = Label(window, text="Site Name:", justify="center")
canvas.create_window(275, 270, window=label_site_name)

label_username = Label(window, text="Username/Email:", justify="center")
canvas.create_window(260, 300, window=label_username)

label_password = Label(window, text="Password:", justify="center")
canvas.create_window(278, 330, window=label_password)

label_clipboard = Label(window, text="", fg="green", bg="black")
canvas.create_window(350, 425, window=label_clipboard)

# ======================== ENTRIES ======================== #
site_name = Entry(window, textvariable=name)
canvas.create_window(380, 270, window=site_name)

username = Entry(window, textvariable=user)
canvas.create_window(380, 300, window=username)

password = Entry(window, textvariable=pwd, show="*")
canvas.create_window(380, 330, window=password)

# ======================== BUTTONS ======================== #
generate_button = Button(window, text="Generate Password", command=generate_password)
canvas.create_window(505, 330, window=generate_button)

submit_button = Button(window, text="Submit Credential", command=get_credentials)
canvas.create_window(410, 375, window=submit_button)

show_password = Button(window, text="Show Password")
canvas.create_window(300, 375, window=show_password)
show_password.bind("<ButtonPress-1>", reveal_text)
show_password.bind("<ButtonRelease-1>", hide_text)

window.mainloop()
