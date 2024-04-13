import os


def main(path):     # list_folders
    """
    List all folders in the specified path.
    
    Args:
    - path (str): The path to search for folders.
    
    Returns:
    - folders (list): A list of folder names.
    """
    folders = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            folders.append(item)
    return folders

if __name__ == "__main__":
    # Change the path to your desired directory
    directory = "INTER/"
    
    folders = main(directory)
    print("Folders in", directory)
    for folder in folders:
        print(folder)