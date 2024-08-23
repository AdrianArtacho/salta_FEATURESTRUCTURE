import pandas as pd
import os
import gui.gui_button_t as gui_button

def read_folderpath(file_path="INTER/folderpath.txt"):
    
    # Open the file in read mode ('r') and read its content
    with open(file_path, "r") as file:
        file_content = file.read()

    # Print the content of the file
    print(file_content, type(file_content))
    return file_content

def find_txt_in_folder(folder_path):
    # List all files in the folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".txt"):
            print(file_name)
            return file_name

def add_summary_to_txt(summary_df, description_path):
    # Convert DataFrame to string
    df_string = summary_df.to_string(index=False)

    # Specify the file path
    # file_path = "output.txt"

    # Open the file in append mode ('a') and write the DataFrame string at the bottom
    with open(description_path, "a") as file:
        file.write("\n\n")  # Add some space before the DataFrame content
        file.write("Summary DataFrame:\n")
        file.write(df_string)

    print("DataFrame content has been appended to the file.")    

def get_filesize(file_path="INTER/salta.csv"):
    # Get the file size in bytes
    file_size_bytes = os.path.getsize(file_path)

    # Convert the size to megabytes (1 MB = 1,048,576 bytes)
    file_size_mb = file_size_bytes / (1024 * 1024)

    print(f"File size: {file_size_mb:.2f} MB")    

    return file_size_bytes, file_size_mb

def add_line_to_txt(file_path, add_line):
    # The line you want to add
    # add_line = "This is the new line added at the end of the file."

    # Open the file in append mode ('a') and write the new line
    with open(file_path, "a") as file:
        file.write("\n\n")  # Add a newline character before the additional line
        file.write(add_line)

    print("New line has been added to the file.")    

def analyze_file(input_path, output_path='check.csv'):
    # Load the CSV file
    df = pd.read_csv(input_path)

    # Prepare the DataFrame
    features = df['feature'].unique()
    data = []

    for feature in features:
        feature_df = df[df['feature'] == feature]
        instance_count = len(feature_df)
        min_x = feature_df['x_axis'].min()
        min_y = feature_df['y_axis'].min()
        range_x = feature_df['x_axis'].max() - min_x
        range_y = feature_df['y_axis'].max() - min_y
        data.append([feature, instance_count, min_x, min_y, range_x, range_y])

    # Create a new DataFrame with the required information
    summary_df = pd.DataFrame(data, columns=['feature', 'instance_count', 'min_x', 'min_y', 'range_x', 'range_y'])

    # Save the summary DataFrame to a CSV file
    summary_df.to_csv(output_path, index=False)

    print(f"Summary saved to {output_path}")

    return summary_df

def feature_lengths(summary_df, col='feature'):
    # 1. Total number of features in the 'feature' column
    total_features = len(summary_df[col])

    # 2. Number of distinct features
    distinct_features = summary_df[col].nunique()

    # 3. Length of the longest string in the 'feature' column
    longest_string_length = summary_df[col].apply(len).max()

    # Display the results
    print(f"Total number of features: {total_features}")
    print(f"Number of distinct features: {distinct_features}")
    print(f"Length of the longest string: {longest_string_length}")

    return total_features, distinct_features, longest_string_length

def main(input_file_path='INTER/salta.csv',
         output_file_path='INTER/salta_check.csv'):

    folder_path = read_folderpath()
    description_file = find_txt_in_folder(folder_path)
    description_path = os.path.join(folder_path, description_file)
    print("description_path:", description_path)

    # Ask user
    answer = gui_button.main(('Yes','No'), default_option=0,     
         dialog_text="Did it work on the SALTA App GUI?",
         title="Choice", size=(20, 1))

    add_line_to_txt(description_path, f"Did it work? {answer}.")

    # Calculate summary
    summary_df = analyze_file(input_file_path, output_file_path)
    add_summary_to_txt(summary_df, description_path)

    file_size_bytes, file_size_mb = get_filesize()
    add_line_to_txt(description_path, f"The size of the CSV file is {file_size_bytes}bytes ({file_size_mb} Mb)")
    
    total_features, distinct_features, longest_string_length = feature_lengths(summary_df)
    add_line_to_txt(description_path, f"total_features: {total_features}, distinct_features: {distinct_features}, longest_string_length: {longest_string_length}")
    



    print("\nClick below to see the summary:")
    print(description_path)
    print("\n")

if __name__ == "__main__":
    # Example usage
    # input_file_path = 'INTER/salta.csv'
    # output_file_path = 'INTER/salta_check.csv'
    main()
