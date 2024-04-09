import os

def main(subfolder, local_folder = ''):
    # Define the name of the local folder and the subfolder to be created
    # local_folder = 'OUTPUT'
    # subfolder = 'projectFolder'

    # Check if the local folder exists, if not, create it
    if not os.path.exists(local_folder):
        os.makedirs(local_folder)
        print(f"Local folder '{local_folder}' created.")

    # Define the path of the subfolder within the local folder
    subfolder_path = os.path.join(local_folder, subfolder)

    # Check if the subfolder exists, if not, create it
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
        print(f"Subfolder '{subfolder}' created within '{local_folder}'.")
    else:
        print(f"Subfolder '{subfolder}' already exists within '{local_folder}'.")

if __name__ == "__main__":
    subfolder = 'projectFolder1'
    main(subfolder, local_folder = 'OUTPUT')