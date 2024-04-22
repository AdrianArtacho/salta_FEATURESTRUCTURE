import shutil
import os
import pyt.paths.create_folder as create_folder

def main(source_file_path, destination_folder, destination_subfolder):

    ## Create folder if it's not created yet
    # subfolder = 'projectFolder1'
    create_folder.main(destination_subfolder, local_folder = destination_folder)

    destination_path = os.path.join(destination_folder, destination_subfolder)
    
    # Check if source_file_path is the same as the resulting destination path
    destination_file_path = os.path.join(destination_path, os.path.basename(source_file_path))
    if os.path.abspath(source_file_path) != os.path.abspath(destination_file_path):
        # print("Source file path is the same as the resulting destination path. Skipping copy operation.")
        # return

        shutil.copyfile(source_file_path, destination_file_path)
        print("File", source_file_path, "copied over to", destination_path)
    print("!!! going on")

# Example usage:

if __name__ == "__main__":
    working_json_filepath = "INPUT/testu51/testu51_json.json"
    destination_folder = "INTER"
    destination_subfolder = "testu51"
    main(working_json_filepath, destination_folder, destination_subfolder)
