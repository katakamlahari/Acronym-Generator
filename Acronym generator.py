import tkinter as tk
from tkinter import messagebox

def create_acronym(text):
    # Split the input text into words ignoring empty parts
    words = [word for word in text.split() if word]
    # Take the first letter of each word, capitalize it and join
    acronym = ''.join(word[0].upper() for word in words)
    return acronym

def generate_acronym():
    input_text = entry.get()
    if not input_text.strip():
        messagebox.showwarning("Input Error", "Please enter a valid input string.")
        return
    result = create_acronym(input_text)
    result_label.config(text=f"Acronym: {result}", bg="grey", fg="white")

# Setup the main window
root = tk.Tk()
root.title("Acronym Generator")
root.geometry("600x300")
root.resizable(False, False)
root.configure(bg="lavender")

# Instructions label
instructions = tk.Label(root, text="Enter a phrase to generate its acronym:", font=("Arial", 14), bg="lavender")
instructions.pack(pady=10)

# Input entry
entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate Acronym", font=("Arial", 12), command=generate_acronym)
generate_button.pack(pady=10)

# Result label (initial background white and black text)
result_label = tk.Label(root, text="Acronym: ", font=("Arial", 16, "bold"), bg="lavender", fg="green")
result_label.pack(pady=10)

# Run the application
root.mainloop()
