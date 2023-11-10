oimport tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

# Creating a full-screen window
root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg='#4d4d4d')  # Background color

# Load the logo and position it
logo_photo = ImageTk.PhotoImage(Image.open('logo.png'))
logo_label = tk.Label(root, image=logo_photo, bg='#4d4d4d')
logo_label.pack(fill="both", expand=True)

# Welcome message
text_above_buttons = tk.Label(root, text="Welcome to our company!\nPlease select an option:", font=("Helvetica", 24), bg='#4d4d4d', fg='white')
text_above_buttons.pack(fill="both", expand=True)

# Create buttons with custom actions
buttons = [
    {"text": "I'm a Customer", "action": "action_button1"},
    {"text": "Deliveries", "action": "action_button2"},
    {"text": "Pickups", "action": "action_button3"},
    {"text": "Other inquiries", "action": "action_button4"},
]

# Place the buttons on the screen
for button_data in buttons:
    button = tk.Button(root, text=button_data["text"], font=("Helvetica", 36), bg='#4d4d4d', fg='white',
                       command=lambda action=button_data["action"]: button_click(action))
    button.pack(fill="both", expand=True)

# Button actions (when clicked)
def button_click(action):
    if action == "action_button1":
        # Define action
        pass
    elif action == "action_button2":
        # Define action
        pass
    elif action == "action_button3":
        # Define action
        pass
    elif action == "action_button4":
        # Define action
        pass

    # Show the message popup
    messagebox.showinfo("All set!", "We are on our way, and you will be attended to shortly.")

# Run in a loop
root.mainloop()
