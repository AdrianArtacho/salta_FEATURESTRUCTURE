import tkinter as tk
from tkinter import font
import webbrowser
import sys

def open_url(url):
    webbrowser.open_new(url)

def main(font_size=12, text4_width=30,
         text1="1. Upload the text to the SALTA APP",
         text2="SALTA APP Website", hyperlink1="https://adrianartacho.github.io/SALTA",
         text3="2. Click on the URL below to apply the weights",
         text4="This is a very long string that should wrap to multiple lines if it exceeds the specified width limit.",
         hyperlink2="https://yourweightsurl.com"):
    
    # Initialize the main window
    root = tk.Tk()
    root.title("SALTA APP GUI")

    # Ensure the window closes completely when the user clicks the close button
    def on_closing():
        root.destroy()
        sys.exit()  # Ensure the script terminates

    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Define custom font
    custom_font = font.Font(size=font_size)

    # Create and place Text1
    text1 = tk.Label(root, text=text1, font=custom_font)
    text1.pack(pady=(10, 5))

    # Create and place Text2 (hyperlink)
    text2 = tk.Label(root, text=text2, font=custom_font, fg="blue", cursor="hand2")
    text2.pack(pady=(5, 10))
    text2.bind("<Button-1>", lambda e: open_url(hyperlink1))

    # Create and place Text3
    text3 = tk.Label(root, text=text3, font=custom_font)
    text3.pack(pady=(10, 5))

    # Create and place Text4 (another hyperlink) with wrapping
    text4 = tk.Label(root, text=text4, font=custom_font, fg="blue", cursor="hand2", wraplength=text4_width * font_size)
    text4.pack(pady=(5, 10))
    text4.bind("<Button-1>", lambda e: open_url(hyperlink2))

    # Start the Tkinter main loop
    root.mainloop()

# Example usage
if __name__ == "__main__":
    main(font_size=14, text4_width=30)
