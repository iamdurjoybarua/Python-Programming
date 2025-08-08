import tkinter as tk
from tkinter import messagebox

def calculate_area():
    try:
        length = float(length_entry.get())
        width = float(width_entry.get())
        area = length * width
        result_label.config(text=f"Area: {area:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Area Calculator")

# Create widgets
length_label = tk.Label(root, text="Length:")
length_entry = tk.Entry(root)

width_label = tk.Label(root, text="Width:")
width_entry = tk.Entry(root)

calculate_button = tk.Button(root, text="Calculate", command=calculate_area)

result_label = tk.Label(root, text="Area: ")

# Place widgets in the window
length_label.grid(row=0, column=0, padx=10, pady=5)
length_entry.grid(row=0, column=1, padx=10, pady=5)

width_label.grid(row=1, column=0, padx=10, pady=5)
width_entry.grid(row=1, column=1, padx=10, pady=5)

calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label.grid(row=3, column=0, columnspan=2)

# Start the application
root.mainloop()