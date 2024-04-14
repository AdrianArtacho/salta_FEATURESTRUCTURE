import pandas as pd
import json
import os

def main(json_files):
    # Initialize an empty list to store extracted feature items
    feature_items = []

    # Iterate over each JSON file
    for json_file in json_files:
        # Load the JSON data from the file
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        # Extract feature items from the 'featuredict' key
        if 'featuredict' in data:
            for feature_name, feature_data in data['featuredict'].items():
                # Extract feature name, weight, and path
                feat_name = feature_name
                feat_weight = feature_data.get('weight', None)
                feat_path = feature_data.get('path', None)
                
                # Append the extracted information to the feature_items list
                feature_items.append({
                    'name': feat_name,
                    'weight': feat_weight,
                    'path': feat_path
                })

    # Create a DataFrame from the extracted feature items
    df = pd.DataFrame(feature_items)
    return df

# Example usage:
if __name__ == "__main__":
    import sys

    # Check if the user provided the list of JSON files as an argument
    if len(sys.argv) < 2:
        print("Usage: python extract_features.py <json_file1> <json_file2> ...")
        sys.exit(1)

    # Extract JSON file paths from command line arguments
    json_files = sys.argv[1:]

    # Check if the provided paths are valid files
    for json_file in json_files:
        if not os.path.isfile(json_file):
            print(f"Error: File not found: {json_file}")
            sys.exit(1)

    # Extract features from JSON files and create a DataFrame
    df = main(json_files)

    # Display the DataFrame
    print(df)
