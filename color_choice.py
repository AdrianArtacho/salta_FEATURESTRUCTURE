import easygui

def main(verbose=False):
    # List of common color names
    color_choices = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "cyan", "brown"]

    chosen_color = easygui.choicebox("Choose a color:", "Choose Color", choices=color_choices)

    if verbose:
        print("Chosen color:", chosen_color)

    return chosen_color

if __name__ == "__main__":
    main(verbose=False)