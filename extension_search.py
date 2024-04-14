import os
import sys

def main(path, extension, except_string="weight"): # find_files_with_extension
    """
    Find all files with the specified extension in the specified path.
    
    Args:
    - path (str): The path to search for files.
    - extension (str): The extension of the files to search for.
    
    Returns:
    - file_paths (list): A list of paths to files with the specified extension.
    """
    file_paths = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path) and item.endswith(extension) and not item.startswith(except_string):
            file_paths.append(item_path)
    return file_paths

if __name__ == "__main__":
    # Check if the user provided both the path and extension arguments
    if len(sys.argv) != 3:
        print("Usage: python find_files.py <path> <extension>")
        sys.exit(1)

    # Extracting arguments
    directory = sys.argv[1]
    extension = sys.argv[2]
    
    files = main(directory, extension, except_string="weight") # find_files_with_extension
    if files:
        print(f"Files with extension '{extension}' found in {directory}:")
        for file_path in files:
            print(file_path)
    else:
        print(f"No files with extension '{extension}' found in {directory}")
