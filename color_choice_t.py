def main(verbose=False):
    # List of common color names
    color_choices = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "cyan", "brown"]

    # Display the options
    print("Choose a color:\n")
    for idx, color in enumerate(color_choices):
        print(f"{idx + 1}. {color}")

    # Prompt the user to select a color
    while True:
        choice = input("\nEnter the number of your choice: ").strip()

        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(color_choices):
                chosen_color = color_choices[idx]
                break
            else:
                print("Invalid choice. Please enter a number corresponding to a color.")
        else:
            print("Invalid input. Please enter a number.")

    if verbose:
        print("Chosen color:", chosen_color)

    return chosen_color

if __name__ == "__main__":
    chosen_color = main(verbose=False)
    print("You selected:", chosen_color)
