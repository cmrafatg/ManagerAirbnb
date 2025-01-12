import tkinter as tk
import subprocess

def open_user():
    """Open the user.py script."""
    subprocess.Popen(["python", "user.py"])

def open_booking():
    """Open the booking.py script."""
    subprocess.Popen(["python", "booking.py"])

def open_property():
    """Open the property.py script."""
    subprocess.Popen(["python", "property.py"])

# Create the main window
root = tk.Tk()
root.title("Main Window")
root.geometry("800x1200")

# Title Label
title_label = tk.Label(root, text="Welcome to the Management System", font=("Arial", 14), pady=10)
title_label.pack()

# Buttons for each script
btn_user = tk.Button(root, text="User Management", font=("Arial", 12), command=open_user)
btn_user.pack(pady=10)

btn_booking = tk.Button(root, text="Booking Management", font=("Arial", 12), command=open_booking)
btn_booking.pack(pady=10)

btn_property = tk.Button(root, text="Property Management", font=("Arial", 12), command=open_property)
btn_property.pack(pady=10)

btn_exit = tk.Button(root, text="Exit", font=("Arial", 12), command=root.destroy)
btn_exit.pack(pady=10)

# Run the main event loop
root.mainloop()
