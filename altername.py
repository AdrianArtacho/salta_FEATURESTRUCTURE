import gui.gui_enterstring as enterstring

def main(input_string, charlimit=30, verbose=False): # check_string_length
    max_length = charlimit

    if len(input_string) > max_length:
        if verbose:
            print("too long")
        
        alter_string = enterstring.main("enter a string under "+str(charlimit)+" characters", "string", "Alternative string", 
                                  font = ("Arial", 16), default_text='',verbose=False)
        returning_string = alter_string
    else:
        if verbose:
            print("within limit")
        returning_string = input_string

    if verbose:
        print("returning_string:", returning_string)

    return returning_string

if __name__ == "__main__":
    input_string = "sgsd sbsfbsdbsdb sdb sd bsdbsd bsdbsdb"
    main(input_string)