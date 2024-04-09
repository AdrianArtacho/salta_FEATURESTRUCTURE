import pandas as pd
import resolution

def main(file_paths):
    """combine_csv_files
    """
    # Initialize an empty list to store DataFrames
    dfs = []

    # Iterate over each file path in the list
    for file_path in file_paths:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        df = resolution.main(df, decimal_points=2)
        # Add a new column to identify the source file
        file_name = file_path.split('/')[-1]  # Extract file name from file path
        df['source'] = file_name
        # Append the DataFrame to the list of DataFrames
        dfs.append(df)

    # Concatenate all DataFrames in the list along rows
    combined_df = pd.concat(dfs, ignore_index=True)

    # Group the combined DataFrame by 'x_axis', 'y_axis', 'feature', and 'tuples',
    # then sum the probabilities
    # combined_df = combined_df.groupby(['x_axis', 'y_axis', 'feature', 'tuples']).sum().reset_index()

    print("combined_df:")
    print(combined_df.head())
    # Save the resulting DataFrame to a new CSV file
    # combined_df.to_csv("combined_probabilities.csv", index=False)
    return combined_df

# Example usage:

# result_df = combine_csv_files(file_paths)



if __name__ == "__main__":
    file_paths = [
    "INPUT/testu51/testu51-MFCC9.csv",
    "INPUT/testu51/testu51-MFCC10.csv",
    "INPUT/testu51/testu51-MFCC5.csv"
    ]
    main(file_paths)
