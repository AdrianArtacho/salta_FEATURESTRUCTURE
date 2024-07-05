import tkinter as tk
from tkinter import font
import webbrowser

def open_url(url):
    webbrowser.open_new(url)

def create_gui(font_size=12):
    # Initialize the main window
    root = tk.Tk()
    root.title("SALTA APP GUI")

    # Define custom font
    custom_font = font.Font(size=font_size)

    # Create and place Text1
    text1 = tk.Label(root, text="Upload the text to the SALTA APP", font=custom_font)
    text1.pack(pady=(10, 5))

    # Create and place Text2 (hyperlink)
    text2 = tk.Label(root, text="SALTA APP Website", font=custom_font, fg="blue", cursor="hand2")
    text2.pack(pady=(5, 10))
    text2.bind("<Button-1>", lambda e: open_url("https://adrianartacho.github.io/SALTA"))

    # Create and place Text3
    text3 = tk.Label(root, text="Click on the URL below to apply the weights", font=custom_font)
    text3.pack(pady=(10, 5))

    # Create and place Text4 (another hyperlink)
    text4 = tk.Label(root, text="Apply Weights URL", font=custom_font, fg="blue", cursor="hand2")
    text4.pack(pady=(5, 10))
    text4.bind("<Button-1>", lambda e: open_url("https://yourweightsurl.com"))

    # Start the Tkinter main loop
    root.mainloop()

# Example usage
create_gui(font_size=14)
