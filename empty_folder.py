import os

def main(folder_path, verbose=False): #remove_files_in_folder
    # Walk through the folder and its subdirectories
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for file_name in files:
            if file_name != ".gitkeep":  # Exclude .gitkeep files
                file_path = os.path.join(root, file_name)
                os.remove(file_path)
                print(f"Removed file: {file_path}")
        
        # Remove the empty directories
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            os.rmdir(dir_path)
            print(f"Removed directory: {dir_path}")

# Specify the folder path
# folder_path = "INTER/"

# # Call the function to remove files in the folder
# remove_files_in_folder(folder_path)

if __name__ == "__main__":
    folder_path = "INTER/"
    main(folder_path, verbose=True)