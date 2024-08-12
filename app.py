import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

# List of motivational quotes
quotes = [
    "The best way to predict the future is to invent it.",
    "Believe you can and you're halfway there.",
    "You are never too old to set another goal or to dream a new dream.",
    "Do not wait to strike till the iron is hot, but make it hot by striking.",
    "The only limit to our realization of tomorrow is our doubts of today."
]

# Function to get a random quote
def get_random_quote():
    return random.choice(quotes)

# Function to update the quote on the label
def update_quote():
    quote = get_random_quote()
    quote_label.config(text=quote)

# Function to create a curved button
def create_curved_button(parent, text, command):
    button = tk.Canvas(parent, width=150, height=40, bg='#007bff', bd=0, highlightthickness=0)
    button.create_oval(0, 0, 150, 40, fill='#007bff', outline='#007bff')
    button.create_text(75, 20, text=text, fill='white', font=('Helvetica', 12, 'bold'))
    button.bind('<Button-1>', lambda e: command())
    return button

# Create main application window
root = tk.Tk()
root.title("Motivational Quote Generator")
root.geometry("500x350")
root.configure(bg="#f5f5f5")

# Create a frame for the quote
frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20, borderwidth=2, relief="flat")
frame.pack(pady=30, padx=30, fill="both", expand=True)

# Add a label to display the quote
quote_label = tk.Label(frame, text="", wraplength=400, font=("Helvetica", 16, "italic"), bg="#ffffff", fg="#333333")
quote_label.pack(pady=20)

# Create the curved button
button = create_curved_button(root, "Get New Quote", update_quote)
button.pack(pady=10)

# Initial quote display
update_quote()

# Start the application
root.mainloop()
