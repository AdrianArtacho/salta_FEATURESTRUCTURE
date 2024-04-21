import gui.gui_enterstring as gui_enterstring
import gui.gui_menu as gui_menu
import gui.gui_browse as gui_browse
import gui.gui_check as gui_check
import gui.debug as debug
import os
import json
import pandas as pd
import write_weights
import color_choice
import resolution
import aggregate
import create_folder
import json_prune
import copy_file


    
def main(selected_folder_path='',
         selected_folder_name='',
         inter_filepath='', ## So thet the INTER JSON file can be found
         verbose=True):
    print("inter_filepath!!!", inter_filepath)

    if selected_folder_path == '':
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
    else:
        selected_folder_path = selected_folder_path
    
    selected_folder_name = os.path.basename(selected_folder_path)
    selected_folder_parent = os.path.dirname(selected_folder_path)
    print("selected_folder_path:", selected_folder_path)
    print("selected_folder_path:", selected_folder_name)
    print("selected_folder_parent:", selected_folder_parent)
    # exit()

    if selected_folder_name == '':
        class_name = gui_enterstring.main('Is this the right name of the class you are about to process?', 
                                        'enter string:', 
                                        'Merge Name',
                                        default_text=selected_folder_name)
    else:
        class_name = selected_folder_name

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
    # else:
    #     json_files = find_json_files(inter_filepath)

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
        print("!!!!!folder_path!!!!",folder_path)
        json_files = [file for file in os.listdir(folder_path) if file.endswith("json.json")]
        all_features = []
        for file in json_files:
            file_path = os.path.join(folder_path, file)
            features = extract_features_from_json(file_path)
            all_features.extend(features)
        df = pd.DataFrame(all_features)
        return df

    # folder_path = "/path/to/your/json/files"
    print("!!!inter_filepath!!!", inter_filepath)
    if inter_filepath == '':
        working_json_filepath = selected_folder_path    # Original INPUT JSON file path
    else:
        working_json_filepath = inter_filepath  # Intermediate JSON file path
    # print(df)

    print("!!!!working_json_filepath!!!!", working_json_filepath)
    df = json_to_dataframe(working_json_filepath) # Either INPUT... or INTER...
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

    done_with_class = False

    ## GUI FOR MERGING FEATURES
    selected_features, selected_values = gui_check.main(feature_list, weightPercent_list, 
                                                        window_title='Merge features?',
                                                       verbose=False)
    inter_folder = 'INTER'  
    if selected_features != []:

        ## IF SOME FEATURES WERE SELECTED FOR AGGREGATION
        print("AGGREGATING FOLLOWING FEATURES:", selected_features)
        
        
        create_folder.main(class_name, local_folder = inter_folder)
        # exit()

        list_of_features_to_aggregate = []
        list_of_feature_names = []
        
        unselected_features = [feature for feature in feature_list if feature not in selected_features]
        print("unselected_features:", unselected_features)

        # exit()

        for feature in selected_features:
            print("feature:", feature)
            list_of_feature_names.append(feature)

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
        print("list_of_feature_names:", list_of_feature_names)

        # exit()
        aggregated_df = aggregate.main(list_of_features_to_aggregate)

        concatenated_feature_names = '_'.join(list_of_feature_names)
        aggregated_filename = "aggregate_"+concatenated_feature_names
        aggregated_path = inter_folder+"/"+class_name+"/"+aggregated_filename+".csv"

        # Modify all values in the 'feature' column
        aggregated_df['feature'] = aggregated_filename

        aggregated_df.to_csv(aggregated_path, index=False)
        print("Result of the aggregation saved as", aggregated_path)
        # exit()
        

        feature_to_include = aggregated_filename, aggregated_path
        inter_json_file_path = json_prune.main(working_json_filepath+"/"+class_name+"_json.json", 
                                               selected_features,   # To prune, remove
                                               feature_to_include,  # To add
                                               inter_folder+"/"+class_name+"/"+class_name+"_json.json")
        print("Intermediate JSON file created at:", inter_json_file_path)

    else:
        print('No features selected for merge.')
        done_with_class = True

        print("working_json_filepath:", working_json_filepath)
        
        source_file_path = working_json_filepath+'/'+class_name+'_json.json'

        copy_file.main(source_file_path, 'INTER', class_name)

        # shutil.copyfile(source_file_path, 
        #                 os.path.join(inter_folder+'/'+class_name, 
        #                 os.path.basename(source_file_path)))
        

        ## CHOOSE PROJECT COLOR
        project_color = color_choice.main()
        

        print("df_sorted:")
        print(df_sorted)
        # exit()

        # print("class_name:", class_name)
        create_folder.main(class_name, local_folder = 'INTER')  # In case there is no folder yet
        # exit()

        write_weights.main(df_sorted, 
                    project_id=class_name, 
                    project_color=project_color,
                    output_path='INTER/',
                    csv_file='weights_'+class_name+'.csv',
                    default_value=1.0)      # when there is not a weight, like in aggregations

        # exit()

    print("STRUCTURE A CLASS DONE!")
    return done_with_class, selected_folder_path, class_name, inter_folder+"/"+class_name

if __name__ == "__main__":
    main(verbose=True)