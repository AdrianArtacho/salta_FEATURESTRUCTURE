import json
import shutil

def main(json_file_path, features_to_remove, feature_to_include, output_json_file_path):
    """
    remove_features_from_json
    """
    # Load the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Access the featuredict and remove selected features
    featuredict = data.get('featuredict', {})
    for feature in features_to_remove:
        featuredict.pop(feature, None)

    # Update the data with modified featuredict
    data['featuredict'] = featuredict

    # Add new feature to the featuredict
    name, aggr_path, aggregated_weight = feature_to_include
    data['featuredict'][name] = {"weight":aggregated_weight,
                                 "path": aggr_path}

    # Write the updated data to a new JSON file
    with open(output_json_file_path, 'w') as output_json_file:
        json.dump(data, output_json_file, indent=4)

    return output_json_file_path


# remove_features_from_json(json_file_path, features_to_remove, output_json_file_path)

if __name__ == "__main__":
    # Example usage:
    json_file_path = "INPUT/testu51/testu51_json.json"  # Path to the input JSON file
    output_json_file_path = "INTER/testu51/inter.json"  # Path to the output JSON file
    features_to_remove = ["Energy", "EntropyEnergy"]  # List of features to remove
    main(json_file_path, features_to_remove, output_json_file_path)