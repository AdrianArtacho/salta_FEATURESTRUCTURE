import json

def main(json_path, prefix, separator='_', verbose=False):
    # Load the JSON file
    with open(json_path, 'r') as file:
        data = json.load(file)

    # Get the 'featuredict' dictionary from the loaded JSON data
    feature_dict = data['featuredict']

    # Create a new dictionary with keys prefixed by 'proj_'
    modified_feature_dict = {prefix + separator + key: value for key, value in feature_dict.items()}

    # Update the original dictionary with the new keys
    data['featuredict'] = modified_feature_dict

    # Write the modified data back to a JSON file
    with open(json_path, 'w') as file:
        json.dump(data, file, indent=4)

    if verbose:
        print("The feature names in", json_path, 'have been renamed')

if __name__ == "__main__":
    json_path = 'INTER/testu51/testu51_json.json'
    prefix = 'proj'
    main(json_path, prefix, verbose=True)