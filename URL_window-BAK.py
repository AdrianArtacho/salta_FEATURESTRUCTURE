import tkinter as tk
from tkinter import font
import webbrowser

def open_url(url):
    webbrowser.open_new(url)

def main(font_size=12, text4_width=20,
               text1="1. Upload the text to the SALTA APP:",
               text2="SALTA APP Website",
               hyperlink1="https://adrianartacho.github.io/SALTA",
               text3="2. Click on the URL below to apply the weights:",
               text4="Apply Weights URL",
               hyperlink2="https://yourweightsurl.com"):
    
    # Initialize the main window
    root = tk.Tk()
    root.title("SALTA APP ↓↓↓")

    # Ensure the window closes completely when the user clicks the close button
    def on_closing():
        root.destroy()

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

    # # Create and place Text4 (another hyperlink)
    # text4 = tk.Label(root, text=text4, font=custom_font, fg="blue", cursor="hand2")
    # text4.pack(pady=(5, 10))
    # text4.bind("<Button-1>", lambda e: open_url(hyperlink2))

    # Create and place Text4 (another hyperlink) with wrapping
    text4 = tk.Label(root, text=hyperlink2, font=custom_font, fg="blue", cursor="hand2", wraplength=text4_width * font_size)
    text4.pack(pady=(5, 10))
    text4.bind("<Button-1>", lambda e: open_url(hyperlink2))

    # Start the Tkinter main loop
    root.mainloop()
    return 'done!'

if __name__ == "__main__":
    # Example usage
    main(font_size=24,
         hyperlink1="https://adrianartacho.github.io/SALTA",
         text4="Apply Weights URL",
         hyperlink2="https://adrianartacho.github.io/SALTA/?file=exp6_SALTA.csv&wleftankle=1.0&wleftheel=0.08&wleftfootindex=0.04&wrightknee=0.03&wrightheel=0.03&wrightpinky1=0.02&wrightankle=0.01&wrightshoulder=0.01&wleftelbow=0.01&wrightwrist=0.01&wleftindex1=0.01&wleftthumb2=0.01&wleftwrist=0.01&wleftpinky1=0.01&wrightfootinde=0.01&wrightindex1=0.01&wrightelbow=0.01&wrightthumb2=0.0&wleftknee=0.0&wrighthip=0.0&wlefthip=0.0&wleftshoulder=0.0&wmouthright=0.0&wrighteyeouter=0.0&wnose=0.0&wrighteye=0.0&wrighteyeinner=0.0&wrightear=0.0&wmouthleft=0.0&wlefteyeinner=0.0&wleftear=0.0")
