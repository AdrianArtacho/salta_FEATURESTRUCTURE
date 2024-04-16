import list_folders
import create_folder
import extension_search
import read_features
import pandas as pd
import alter_path
import os
import extract_from_json
import deriv_df

def main(project_name='proj', 
         output_folder='OUTPUT',
         directory = "INTER/",
         rename_features_after_class=True):
    
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
    # print(df_extracted)
    # exit()
    ## SUBSTITUTE PATHS for those pointing at the wrong folder (where needed)
    # Define a function to apply alter_path.main() to each element in the "path" column
    def update_path(original_path):
        return alter_path.main(original_path, orig_folder="OUTPUT", alter_folder="INPUT")

    # Apply the function to each element in the "path" column and update the DataFrame
    df_extracted['path'] = df_extracted['path'].apply(update_path)

    print(df_extracted)

    
    
    ## INTEGRATE ALL FEATURES
    paths_list = df_extracted['path'].tolist()
    # print('paths_list:', paths_list)

    # Initialize an empty list to store DataFrames
    dfs = []

    # Iterate through each file path
    for path in paths_list:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(path)
        if rename_features_after_class:
            df = deriv_df.main(df, path, column_name='feature', separator='_') #!!!!
        # Append the DataFrame to the list
        dfs.append(df)

    # Concatenate all DataFrames in the list into a single DataFrame
    combined_df = pd.concat(dfs, ignore_index=True)

    # Now combined_df contains the contents of all CSV files combined together
    print(combined_df)

    # Define the output file path
    output_file = os.path.join(output_dir, project_name+".csv")

    # Save the concatenated DataFrame to a CSV file
    combined_df.to_csv(output_file, index=False)

    # exit()
    ## GENERATE A WEIGHTS FILE FOR ALL FEATURES
    print(weig_files)
    # Initialize an empty list to store DataFrames
    df_agg = []

    # Iterate through each file path
    for file in weig_files:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file)
        if rename_features_after_class:
            df = deriv_df.main(df, path, column_name='feature', separator='_') #!!!!

        # Append the DataFrame to the list
        df_agg.append(df)

    # Concatenate all DataFrames in the list into a single DataFrame
    concatenated_df = pd.concat(df_agg, ignore_index=True)

    # # Define the output directory
    # output_dir = "OUTPUT"+'/'+project_name
    # os.makedirs(output_dir, exist_ok=True)

    # Define the output file path
    output_file = os.path.join(output_dir, "weights_"+project_name+".csv")

    # Save the concatenated DataFrame to a CSV file
    concatenated_df.to_csv(output_file, index=False)

    # Now concatenated_df contains the contents of all CSV files concatenated together
    print(f"Concatenated data saved to: {output_file}")

if __name__ == "__main__":
    main()