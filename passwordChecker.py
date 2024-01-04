import math
import re
import tkinter as tk
from tkinter import messagebox


def calculate_entropy(password):
    # Calculate entropy of the password
    char_set_size = 94  # Assuming printable ASCII characters
    entropy = len(password) * math.log2(char_set_size)
    return entropy


def calculate_variance(password):
    # Convert the password characters to ASCII values
    ascii_values = [ord(char) for char in password]
    # Calculate the mean
    mean = sum(ascii_values) / len(ascii_values)
    # Calculate the squared differences from the mean
    squared_diff = [(x - mean) ** 2 for x in ascii_values]
    # Calculate the variance
    variance = sum(squared_diff) / len(ascii_values)
    return variance


def check_password_strength(password):
    # Define the complexity rules

    if len(password) < 8:
        messagebox.showinfo("Error", "Please enter a password with 8 or more characters")
        return 'weak'

    complexity_rules = {
        'uppercase': lambda x: bool(re.search(r'[A-Z]', x)),
        'lowercase': lambda x: bool(re.search(r'[a-z]', x)),
        'numbers': lambda x: bool(re.search(r'\d', x)),
        'special_chars': lambda x: bool(re.search(r'\W', x)),
        'entropy': lambda x: calculate_entropy(x) >= 40,
        'variance': lambda x: calculate_variance(x) >= 50
    }

    # Assess the password against the complexity rules
    strength = 0
    for rule, condition in complexity_rules.items():
        if condition(password):
            strength += 1

    # return strength based on how many rules it passed
    if strength < 3:
        return 'Weak'
    elif strength < 5:
        return 'Medium'
    else:
        return 'Strong'


def validate_password():
    password = entry.get()
    strength = check_password_strength(password)
    color = "green" if strength == "Strong" else ("gold" if strength == "Medium" else "red")
    label.config(text=f'{strength} Password!', fg=color)


# Create the main tkinter window
window = tk.Tk()
window.title('Password Strength Checker')
window.minsize(width=300, height=200)
window.eval('tk::PlaceWindow . center')
window.resizable(False, False)
# Create a label for the password entry field
label = tk.Label(window, text='Enter a password:')
label.pack()
# Create an entry field for the password
entry = tk.Entry(window, show="*")
entry.pack()
# Create a button to check the password strength
button = tk.Button(window, text='Check Password Strength', command=validate_password)
button.pack()
# Start the tkinter event loop
window.mainloop()
