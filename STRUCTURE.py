import gui.gui_enterstring as gui_enterstring
import gui.gui_menu as gui_menu
import os
import json
import pandas as pd

## ENTER PROJECT NAME AND DESCRIPTION
proj_name = gui_enterstring.main('This string will identify all files generated from here...', 
                                    'enter string:', 
                                    'Merge Name',
                                    default_text='test')

proj_description = gui_enterstring.main('You may enter a short description here...', 
                                            'Description:', 
                                            'Description',
                                            default_text='Just doing some tests over here...')

# Select input path
input_path_options = ['INPUT/', '../plotly/OUTPUT', '../../plotly/OUTPUT']
input_path = gui_menu.main(input_path_options, 
                        "Where should we look for input files?", 
                        "Input Path", 
                        default_option=0, 
                        font=('Arial Bold', 14))

def find_json_files(folder_path):
    json_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith("json.json"):
                json_files.append(os.path.join(root, file))
    return json_files

folder_path = "INPUT/testu51"
json_files = find_json_files(folder_path)

if json_files:
    print("Found JSON files:")
    for file in json_files:
        print(file)
else:
    print("No JSON files found in the specified folder.")


##

def extract_features_from_json(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
        features = data.get("featuredict", {})
        feature_list = []
        for key, value in features.items():
            weight = value.get("weight", None)
            path = value.get("path", None)
            feature_list.append({"Feature": key, "Weight": weight, "Path": path})
        return feature_list

def json_to_dataframe(folder_path):
    json_files = [file for file in os.listdir(folder_path) if file.endswith("json.json")]
    all_features = []
    for file in json_files:
        file_path = os.path.join(folder_path, file)
        features = extract_features_from_json(file_path)
        all_features.extend(features)
    df = pd.DataFrame(all_features)
    return df

# folder_path = "/path/to/your/json/files"
df = json_to_dataframe(folder_path)
print(df)



# exit()