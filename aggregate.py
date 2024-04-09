import pandas as pd

def combine_csv_files(file_paths):
    # Initialize an empty list to store DataFrames
    dfs = []

    # Iterate over each file path in the list
    for file_path in file_paths:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        # Add a new column to identify the source file
        file_name = file_path.split('/')[-1]  # Extract file name from file path
        df['source'] = file_name
        # Append the DataFrame to the list of DataFrames
        dfs.append(df)

    # Concatenate all DataFrames in the list along rows
    combined_df = pd.concat(dfs, ignore_index=True)

    # Group the combined DataFrame by 'x_axis', 'y_axis', 'feature', and 'tuples',
    # then sum the probabilities
    combined_df = combined_df.groupby(['x_axis', 'y_axis', 'feature', 'tuples']).sum().reset_index()

    return combined_df

# Example usage:
file_paths = [
    "INPUT/testu51/testu51-MFCC9.csv",
    "INPUT/testu51/testu51-MFCC10.csv",
    "INPUT/testu51/testu51-MFCC5.csv"
]
result_df = combine_csv_files(file_paths)

# Save the resulting DataFrame to a new CSV file
result_df.to_csv("combined_probabilities.csv", index=False)
