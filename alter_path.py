"""
Here's how the script works:

It first checks if the file exists at the original path.
If the file doesn't exist at the original path, it constructs 
the alternative path by replacing the root folder "OUTPUT" with "INPUT".
Then, it checks if the file exists at the alternative path.
If the file is found at either the original or alternative path, 
it prints the path where the file was found. 
Otherwise, it prints "File not found".

"""

import os

def main(original_path, orig_folder="OUTPUT", alter_folder="INPUT", verbose=True):
    # Original file path
    # original_path = "OUTPUT/testu51/testu51-MFCC2.csv"
    if verbose:
        print("original_path:", original_path)
        
    # Check if the file exists at the original path
    if os.path.exists(original_path):
        if verbose:
            print(f"File found at original path: {original_path}")
        return original_path
    else:
        # If the file doesn't exist at the original path, construct the alternative path
        alternative_path = os.path.join(alter_folder, os.path.relpath(original_path, orig_folder))
        # Check if the file exists at the alternative path
        if verbose:
            print("alternative_path:", alternative_path)
        if os.path.exists(alternative_path):
            if verbose:
                print(f"File found at alternative path: {alternative_path}")
            return alternative_path
        else:
            print("File not found.")
            exit()

if __name__ == "__main__":
    original_path = "OUTPUT/testu51/testu51-MFCC2.csv"
    main(original_path)