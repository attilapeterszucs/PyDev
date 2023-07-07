import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class SciFiGUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Set the window title and background color
        self.title("Sci-Fi GUI")
        self.configure(bg="#000080")

        # Create a label for the title
        title_label = ttk.Label(self, text="Welcome to the Future", font=("Arial", 24), foreground="#FFFFFF", background="#000080")
        title_label.pack(padx=20, pady=20)

        # Load and display the space background image
        space_image = Image.open("space.jpg")
        space_photo = ImageTk.PhotoImage(space_image)
        space_label = ttk.Label(self, image=space_photo, background="#000080")
        space_label.image = space_photo  # Keep a reference to prevent garbage collection
        space_label.pack(fill="both", expand=True)

# Create an instance of the GUI and start the main loop


if __name__ == "__main__":
    gui = SciFiGUI()
    gui.mainloop()
