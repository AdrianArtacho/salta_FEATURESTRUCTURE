import json
import pandas as pd

def main(json_file, features = []):
    """
    Extract features from the JSON file.
    
    Args:
    - json_file (str): The path to the JSON file.
    - 
    
    Returns:
    - features (list of dicts): A list of dictionaries, each containing feature, weight, and path.
    """
    with open(json_file, 'r') as f:
        data = json.load(f)
        featuredict = data.get('featuredict', {})
        # features = []
        for feature, properties in featuredict.items():
            weight = properties.get('weight', None)
            path = properties.get('path', None)
            features.append({'feature': feature, 'weight': weight, 'path': path})
    return features

if __name__ == "__main__":
    # Path to the JSON file
    json_file = "INTER/testu52/testu52_json.json"
    
    # Load the JSON file and extract features
    features = main(json_file)
    
    # Create an empty DataFrame
    df = pd.DataFrame(columns=['feature', 'weight', 'path'])
    
    # Add features to the DataFrame
    for feature in features:
        df.loc[len(df)] = feature
    
    # Display the DataFrame
    print(df)