import os

def main(df, file_path, column_name='feature', separator='_'): 

    # Extract the directory path from the full file path
    directory_path = os.path.dirname(file_path)

    # Get the name of the folder
    folder_name = os.path.basename(directory_path)

    # Print the folder name
    print("The file is located in a folder named:", folder_name)

    last_bit = folder_name.rsplit('_', 1)[-1]   # gets the last bit of the folder name, after the last underscore
    # exit()

    # Modify the names in the dataframe
    # df[column_name] = last_bit + separator + df[column_name]
    df[column_name] = folder_name + separator + df[column_name]
    
    return df


if __name__ == "__main__":
    file_path = 'INPUT/testu51/testu51-Energy.csv'
    main(file_path)