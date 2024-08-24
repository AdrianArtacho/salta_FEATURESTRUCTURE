import list_folders
import pyt.paths.create_folder as create_folder
import extension_search
import read_features
import pandas as pd
import alter_path
import os
import extract_from_json
import deriv_df
import APP_url
import fill_source
import pyt.df.drop_col as dropcol
import CHECK_SALTA
import gui.gui_button_t as gui_button
import resize
import pprint

def main(project_name='proj', 
         output_folder='OUTPUT',
         directory = "INTER/",
         rename_features_after_class=True,
         verbose=True):
    
    ## CREATE A PROJECT FOLDER IN "OUTPUT/"
    create_folder.main(project_name, local_folder=output_folder)
    # Define the output directory
    output_dir = output_folder+'/'+project_name
    os.makedirs(output_dir, exist_ok=True)

    ## LIST FOLDERS IN "INTER/"
    # directory = "INTER/"    # "INTER/"

    folders = list_folders.main(directory)
    json_files = []
    aggr_files = []
    weig_files = []

    for folder in folders:
        json_path = extension_search.main(directory+folder, '.json')
        json_files.extend(json_path)

        agg_paths = extension_search.main(directory+folder, '.csv', except_string="weight")
        if len(agg_paths) != 0:
            aggr_files.extend(agg_paths)

        csv_paths = extension_search.main(directory+folder, '.csv', except_string=" ")
        # Filter out elements from csv_paths that are not in agg_paths
        weight_paths = [path for path in csv_paths if path not in agg_paths]
        weig_files.extend(weight_paths)

    print("json_files:", json_files)
    print("aggr_files:", aggr_files)
    print("weig_files:", weig_files)


    ## MAKE A LIST OF ALL FEATURES (AND AGGREGATES) WITH THE PATH

    print("json_files:", json_files)
    # exit()

    df_extracted = extract_from_json.main(json_files)
    if verbose:
        print("______________________________")
        print(df_extracted)
        print("______________________________")

    # exit()
    ## SUBSTITUTE PATHS for those pointing at the wrong folder (where needed)
    # Define a function to apply alter_path.main() to each element in the "path" column
    def update_path(original_path):
        # return alter_path.main(original_path, orig_folder="OUTPUT", alter_folder="INPUT")
        return alter_path.main(original_path, orig_folder="OUTPUT", alter_folder="../plotly/OUTPUT")

    # Apply the function to each element in the "path" column and update the DataFrame
    df_extracted['path'] = df_extracted['path'].apply(update_path)

    # Sort the DataFrame based on the 'weight' column
    df_extracted = df_extracted.sort_values(by='weight')

    if verbose:
        print("__________")
        print(df_extracted)
        print("__________")
    # exit()
    
    ## INTEGRATE ALL FEATURES
    paths_list = df_extracted['path'].tolist()
    print('paths_list:', paths_list)
    # exit()

    # Initialize an empty list to store DataFrames
    dfs = []

    print("rename_features_after_class:", rename_features_after_class)

    print("paths_list:")
    print(paths_list)
    print(len(paths_list))
    counter=0
    # exit()

    # Iterate through each file path
    for path in paths_list:
        counter = counter + 1
        print("---->",counter)
        print("Now processing...", path)
        # Read the CSV file into a DataFrame
        df = pd.read_csv(path)

        # # Extract the filename without extension
        # feat_string = os.path.splitext(os.path.basename(path))[0]
        # print("feat_string:",feat_string)

        # # Modify all values in the 'feature' column
        # df['feature'] = feat_string

        if rename_features_after_class:
            df = deriv_df.main(df, path, column_name='feature', separator='_') #!!!!
        
        # Append the DataFrame to the list
        dfs.append(df)

    # exit()
    # Concatenate all DataFrames in the list into a single DataFrame
    combined_df = pd.concat(dfs, ignore_index=True)

    #################
    # THERE SEEMS TO BE MINIMUM X VALUES IN THE SALTA APP, SO BY MULTIPLYING BY 100 Y TURN THE X-VALUES INTO MILLISECONDS
    combined_df['x_axis'] = combined_df['x_axis'] * 100
    # Cast all values in the 'x_axis' column to integers (milliseconds)
    combined_df['x_axis'] = combined_df['x_axis'].astype(int)
    # Drop the 'tuples' and 'source' columns
    data_reduced = dropcol.main(combined_df,colname='source')   #?
    ################

    # Define the output file path
    output_file_salta = os.path.join(output_dir, project_name+".csv")
    checkout_file_salta = os.path.join('INTER', "salta.csv")

    # Save the concatenated DataFrame to a CSV file
    data_reduced.to_csv(output_file_salta, index=False)   #?
    data_reduced.to_csv(checkout_file_salta, index=False) #?



    # exit()
    ## GENERATE A WEIGHTS FILE FOR ALL FEATURES
    print(weig_files)
    # exit()
    # Initialize an empty list to store DataFrames
    df_agg = []

    # Iterate through each file path
    for file in weig_files:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file)
        if rename_features_after_class:
            df = deriv_df.main(df, file, column_name='feature', separator='_') #!!!!

        # Append the DataFrame to the list
        df_agg.append(df)

    # Concatenate all DataFrames in the list into a single DataFrame
    concatenated_df = pd.concat(df_agg, ignore_index=True)

    # # Define the output directory
    # output_dir = "OUTPUT"+'/'+project_name
    # os.makedirs(output_dir, exist_ok=True)

    # Define the output file path
    output_file_wei = os.path.join(output_dir, "weights_"+project_name+".csv")
    checkout_wei = os.path.join('INTER', "weights.csv")

    # Save the concatenated DataFrame to a CSV file
    concatenated_df.to_csv(output_file_wei, index=False)
    concatenated_df.to_csv(checkout_wei, index=False)

    ####### CHECKING SIZE
    salta_filesize_bytes, salta_filesize_mb  = CHECK_SALTA.get_filesize(file_path=checkout_file_salta) # "INTER/salta.csv"
    size_result = f"The size of the SALTA .csv file is {salta_filesize_bytes} ({salta_filesize_mb} mb)"
    resize_choices = ("Try to reduce size", "Leave as it is")
    button_choice = gui_button.main(resize_choices, default_option=0, dialog_text=size_result, 
                                    title="Choice", verbose=False)
    print("button_choice:", button_choice)

    if button_choice == resize_choices[0]:
        print("lets resize")
        # resize.filter_tuples(checkout_file_salta, output_file) # Causes some issue...
        new_names_dict = resize.modify_features_and_return_dict(checkout_file_salta, output_file_salta)
        resize.apply_replacements(output_file_wei, new_names_dict)
        resize.round_y_axis(output_file_salta, decimal_points=7)
        pprint.pprint(new_names_dict)
    else:
        print("leave as it is")
    # exit()
    ####################

    # Now concatenated_df contains the contents of all CSV files concatenated together
    print(f"Concatenated data saved to: {output_file_salta}")
    if verbose:
        print("INTEGRATing done!")
        # print("Gnerating URL...")


    # This saves the working directory path as a txt in INTER
    with open("INTER/folderpath.txt", "w") as file:
        file.write(output_dir)

    return output_dir
    

if __name__ == "__main__":
    main()