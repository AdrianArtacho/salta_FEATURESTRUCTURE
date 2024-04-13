import list_folders
import create_folder
import extension_search
import read_features
import pandas as pd


## CREATE A PROJECT FOLDER IN "OUTPUT/"
project_name = 'proj'

create_folder.main(project_name, local_folder = 'OUTPUT')

## LIST FOLDERS IN "INTER/"
directory = "INTER/"

folders = list_folders.main(directory)
json_files = []
aggr_files = []

for folder in folders:
    print(folder)
    json_path = extension_search.main(directory+folder, '.json')
    json_files.append(json_path[0])
    print("json_path:", json_path)

    csv_paths = extension_search.main(directory+folder, '.csv')
    aggr_files.append(csv_paths[0])
    print("csv_paths:", csv_paths)


print("json_files:", json_files)
print("aggr_files:", aggr_files)

## MAKE A LIST OF ALL FEATURES (AND AGGREGATES) WITH THE PATH

# Create an empty DataFrame
df = pd.DataFrame(columns=['feature', 'weight', 'path'])

for json_file in json_files:
    # json_file = "INTER/testu52/testu52_json.json"
    print("json_file:", json_file)

    # Load the JSON file and extract features
    features = read_features.main(json_file)
    print("features:", features)
        
    # Add features to the DataFrame
    for feature in features:
        df.loc[len(df)] = feature

    # exit()

# Display the DataFrame
print(len(df))
# print(df.head())
print(df)


## INTEGRATE ALL FEATURES

## GENERATE A WEIGHTS FILE FOR ALL FEATURES