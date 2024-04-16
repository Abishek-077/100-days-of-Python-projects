import random
import tkinter as tk
from tkinter import messagebox

# Function to generate the password
def generate_password():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+'

    nr_letters = int(letters_slider.get())
    nr_symbols = int(symbols_slider.get())
    nr_numbers = int(numbers_slider.get())

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = ''.join(password_list)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Setting up the window
window = tk.Tk()
window.title("Password Generator by abishek ghimire")

# Creating the layout
tk.Label(window, text="Welcome to the Password Generator!", font=("Arial", 15)).pack(pady=10)

# Sliders to select the number of characters
letters_slider = tk.Scale(window, from_=0, to=10, orient='horizontal', label="Letters")
letters_slider.pack()
symbols_slider = tk.Scale(window, from_=0, to=10, orient='horizontal', label="Symbols")
symbols_slider.pack()
numbers_slider = tk.Scale(window, from_=0, to=10, orient='horizontal', label="Numbers")
numbers_slider.pack()

# Entry widget to display the generated password
password_entry = tk.Entry(window, width=40, borderwidth=3)
password_entry.pack(pady=20)

# Button to generate the password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Running the application
window.mainloop()