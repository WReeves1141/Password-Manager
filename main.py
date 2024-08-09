
__author__ = "Walter Reeves"

from secrets import choice
from string import ascii_letters, digits, punctuation
from tkinter import Button, Canvas, Entry, Label, messagebox, PhotoImage, Tk


def generate(password_characters=12):
    """Generates a random password."""
    alphabet = ascii_letters + digits + punctuation
    new_password = "".join(choice(alphabet) for _ in range(password_characters))

    print(new_password)


def test():
    print("hello")


window = Tk()
window.title("Password Manager")
window.geometry("700x500")

canvas = Canvas(window, width=700, height=500, background="black")

logo = PhotoImage(file="logo.png")
canvas.create_image(350, 150, image=logo)
canvas.pack()

label_site_name = Label(window, text="Site Name:", justify="center")
canvas.create_window(265, 270, window=label_site_name)

label_username = Label(window, text="Username/Email:", justify="center")
canvas.create_window(250, 300, window=label_username)

site_name = Entry(window)
canvas.create_window(400, 270, window=site_name)

username = Entry(window)
canvas.create_window(400, 300, window=username)


generate_button = Button(text="Generate Password", command=generate)
canvas.create_window(350, 250, window=generate_button)

window.mainloop()
