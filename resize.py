import pandas as pd
import sys

def filter_tuples(csv_path, output_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path)
    
    # Ensure that the 'tuples' column exists in the DataFrame
    if 'tuples' not in df.columns:
        print("The specified column 'tuples' does not exist in the DataFrame.")
        return
    
    # Replace values in the 'tuples' column except 'lower_limit' and 'higher_limit' with an empty string
    df['tuples'] = df['tuples'].apply(lambda x: x if x in ['lower_limit', 'higher_limit'] else '-')
    
    # Save the modified DataFrame to a new CSV file
    df.to_csv(output_path, index=False)
    print(f"Modified DataFrame saved to {output_path}")

def modify_features_and_return_dict(csv_path, output_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path)
    
    # Ensure that the 'feature' column exists in the DataFrame
    if 'feature' not in df.columns:
        print("The specified column 'feature' does not exist in the DataFrame.")
        return
    
    # Get the unique values in the 'feature' column
    unique_features = df['feature'].unique()
    
    # Initialize the dictionary to store the mappings
    feature_mapping = {}
    
    # Iterate through the unique values and prompt the user for replacement
    for feature in unique_features:
        new_value = input(f"Enter an alternative for '{feature}' (or press Enter to keep it unchanged): ").strip()
        if new_value:
            df['feature'] = df['feature'].replace(feature, new_value)
            feature_mapping[feature] = new_value
        else:
            feature_mapping[feature] = feature  # Keep the original if unchanged
    
    # Save the modified DataFrame to a new CSV file
    df.to_csv(output_path, index=False)
    print(f"Modified DataFrame saved to {output_path}")
    
    # Return the dictionary with original and new values
    return feature_mapping

def apply_replacements(csv_path, replacement_dict):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path)
    # exit()
    
    # Ensure that the 'feature' column exists in the DataFrame
    if 'feature' not in df.columns:
        print("The specified column 'feature' does not exist in the DataFrame.")
        return
    
    # Replace the 'feature' values based on the dictionary
    df['feature'] = df['feature'].replace(replacement_dict)
    
    # Save the modified DataFrame, replacing the original CSV file
    new_csv_path = csv_path#+'xxx.csv'
    df.to_csv(new_csv_path, index=False)
    print(f"Modified DataFrame saved and replaced the original file at {new_csv_path}")

def round_y_axis(csv_path, decimal_points=7):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_path)
    
    # Ensure that the 'y_axis' column exists in the DataFrame
    if 'y_axis' not in df.columns:
        print("The specified column 'y_axis' does not exist in the DataFrame.")
        return
    
    # Round the floats in the 'y_axis' column to 7 decimal places
    df['y_axis'] = df['y_axis'].round(decimal_points)
    
    # Save the modified DataFrame back to the original CSV file
    df.to_csv(csv_path, index=False)
    print(f"Rounded 'y_axis' column saved back to the original file at {csv_path}")

if __name__ == "__main__":
    # Check if the user provided the path to the CSV file as an argument
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_csv_path> <output_csv_path>")
    else:
        input_csv_path = sys.argv[1]
        output_csv_path = sys.argv[2]
        filter_tuples(input_csv_path, output_csv_path)
