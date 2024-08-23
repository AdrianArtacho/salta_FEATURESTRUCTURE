import webbrowser
import CHECK_SALTA

def open_url(url):
    webbrowser.open_new(url)

def main(font_size=12, text4_width=30,
         text1="1. Upload the text to the SALTA APP",
         text2="SALTA APP Website", hyperlink1="https://adrianartacho.github.io/SALTA",
         text3="2. Click on the URL below to apply the weights",
         text4="This is a very long string that should wrap to multiple lines if it exceeds the specified width limit.",
         hyperlink2="https://yourweightsurl.com"):
    

    # Function to wrap text to a specified width
    def wrap_text(text, width):
        words = text.split()
        lines = []
        current_line = ""
        for word in words:
            if len(current_line) + len(word) + 1 <= width:
                current_line += (word + " ")
            else:
                lines.append(current_line.strip())
                current_line = word + " "
        lines.append(current_line.strip())
        return "\n".join(lines)

    print(f"\n{text1}\n")
    print(f"{text2} (URL: {hyperlink1})\n")
    print(f"{text3}\n")
    print(f"{wrap_text(text4, text4_width)} (URL: {hyperlink2})\n")

    print("Select an option:")
    print("1. Open SALTA APP Website")
    print("2. Open the Weights URL")
    print("3. Run CHECK_SALTA.py")
    print("4. Exit")

    check_afterwards = False

    while True:
        choice = input("\nEnter the number of your choice: ").strip()

        if choice == "1":
            open_url(hyperlink1)
            print(f"Opening {hyperlink1}...\n")
        elif choice == "2":
            open_url(hyperlink2)
            print(f"Opening {hyperlink2}...\n")
        elif choice == "3":
            print("Checking...")
            check_afterwards = True
            # CHECK_SALTA.main()
            break
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    if check_afterwards:
        CHECK_SALTA.main()

if __name__ == "__main__":
    main(font_size=14, text4_width=30)
