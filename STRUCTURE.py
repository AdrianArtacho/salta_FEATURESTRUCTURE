import gui.gui_enterstring as gui_enterstring
import gui.gui_menu as gui_menu
import gui.gui_browse as gui_browse
import gui.gui_check as gui_check
import os
import json
import pandas as pd
import write_weights
import color_choice
import resolution
import aggregate
import create_folder

# label_list = ['Numbers of pulses:', 'Frequency (Hz):', 'Pulse width (ms):', 'Amplitude (V):']
# values_list = ['11', '22', '33', '44']
# selected_labels, selected_values = gui_check.main(label_list, values_list)
# print(selected_labels)
# print(selected_values)
# # exit()

## ENTER PROJECT NAME AND DESCRIPTION
proj_name = gui_enterstring.main('This string will identify the overall project.', 
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
                        "Path to CLASS/SUBSET", 
                        default_option=0, 
                        font=('Arial Bold', 14))

print("input_path:", input_path)

path_to_file_in_folder = gui_browse.main(params_title='Browse files', 
         params_initbrowser=input_path,
         params_extensions='.csv',               # E.g. '.csv'
         size=(40,20),
         verbose=False
         )

print("path_to_file_in_folder:", path_to_file_in_folder)

selected_folder_path = os.path.dirname(path_to_file_in_folder)
selected_folder_name = os.path.basename(selected_folder_path)
selected_folder_parent = os.path.dirname(selected_folder_path)
print("selected_folder_path:", selected_folder_path)
print("selected_folder_path:", selected_folder_name)
print("selected_folder_parent:", selected_folder_parent)
# exit()

class_name = gui_enterstring.main('Is this the right name of the class you are about to process?', 
                                    'enter string:', 
                                    'Merge Name',
                                    default_text=selected_folder_name)

print("class_name:", class_name)
# exit()

def find_json_files(folder_path):
    json_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith("json.json"):
                json_files.append(os.path.join(root, file))
    return json_files


json_files = find_json_files(selected_folder_path)

if json_files:
    print("Found JSON files:")
    for file in json_files:
        print(file)
else:
    print("No JSON files found in the specified folder.")


## EXTRACT FROM JSON

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
df = json_to_dataframe(selected_folder_path)
# print(df)

# Assuming df is your DataFrame with the 'Weight' column containing floats as strings
df['Weight'] = df['Weight'].astype(float)  # Convert the 'Weight' column to float

# Add a new column "weightPercent" with the scaled weight values rounded to 2 decimal places
df['weightPercent'] = (df['Weight'] * 100).round(4)

# df_sorted = df.sort_values(by='Weight', ascending=False)
df_sorted = df.sort_values(by='Weight', ascending=False).reset_index(drop=True)


print(df_sorted)
# exit()

feature_list = df_sorted['Feature'].tolist()
weightPercent_list = df_sorted['weightPercent'].tolist()
# label_list = ['Numbers of pulses:', 'Frequency (Hz):', 'Pulse width (ms):', 'Amplitude (V):']
# values_list = ['11', '22', '33', '44']
selected_features, selected_values = gui_check.main(feature_list, weightPercent_list, verbose=False)
if selected_features != []:

    ## IF SOME FEATURES WERE SELECTED FOR AGGREGATION
    print("AGGREGATING FOLLOWING FEATURES:", selected_features)
    
    create_folder.main(class_name, local_folder = 'INTER')
    exit()

    list_of_features_to_aggregate = []

    for feature in selected_features:
        print("feature:", feature)

        # Find the corresponding 'Path' value based on the 'Feature' value
        path_value = df.loc[df['Feature'] == feature, 'Path'].iloc[0]
        print("path_value:", path_value)

        print("Path value corresponding to", feature, ":", path_value)
        filename_from_path = os.path.basename(path_value)
        print("filename_from_path:", filename_from_path)
        recreated_path = selected_folder_path+"/"+filename_from_path
        print("recreated_path:", recreated_path)
        list_of_features_to_aggregate.append(recreated_path)

    print("list_of_features_to_aggregate:", list_of_features_to_aggregate)

    aggregated_df = aggregate.main(list_of_features_to_aggregate)

    aggregated_df.to_csv("aggregated_features.csv", index=False)
    exit()
    ## CHOOSE PROJECT COLOR
    project_color = color_choice.main()

    write_weights.main(df_sorted, 
                    project_id=class_name, 
                    project_color=project_color,
                    csv_file='weights_'+class_name+'.csv')
