import pandas as pd
import resolution
from pathlib import Path
import gui.gui_button_t as gui_button
import pyt.graph.graph_df as graph_df
import sum_df

def get_filename_from_path(path):
    return Path(path).name

def get_weight_by_filename(df, filename):
    # Search for the filename in the 'Filename' column
    result = df[df['Filename'] == filename]['Weight']
    
    # Check if any result is found
    if not result.empty:
        return float(result.iloc[0])  # Return the first (and likely only) matching weight
    else:
        return None  # Return None or a default value if the filename is not found

def apply_weight(df, file_path, df_sorted, verbose=True):
    filename_to_search = get_filename_from_path(file_path)
    weight = get_weight_by_filename(df_sorted, filename_to_search)
    # print("weight:", weight, type(weight))

    if verbose:
        rounded_weight = format(weight, '.15f')  # 15 decimal places
        print("Weight is:", weight, rounded_weight, type(weight))

    if verbose:
        print(df)
        graph_df.main(df, title=filename_to_search+" (before)", savepath="INTER/"+filename_to_search+"before.png")

    df['y_axis'] = df['y_axis'] * weight

    if verbose:
        print(df)
        graph_df.main(df, title=filename_to_search+" (after)", savepath="INTER/"+filename_to_search+"after.png")


    if verbose:
        print(f"\nWeight {weight} ({rounded_weight}) was applied to feature {filename_to_search}")
    # print("AAPPLLYY")
    return df

def main(file_paths,
         df_sorted,     # in process...
         verbose=True):  
    """It aggregates .csv files...
        ...based on their weights?
    """

    if verbose:
        print("\ndf_sorted:")
        print(df_sorted)

    # Apply the function to the 'Path' column to get Filenames
    df_sorted['Filename'] = df_sorted['Path'].apply(get_filename_from_path)
    if verbose:
        print("\nStripped down paths:")
        print(df_sorted)

    # print("\nfile_paths:")
    for path in file_paths:
        filename_to_search = get_filename_from_path(path)
        weight = get_weight_by_filename(df_sorted, filename_to_search)
        if verbose:
            print("path:", path)
            print("filename_to_search:", filename_to_search)
            print("weight:", weight)
    # exit()



    #######
    applying_options = (True, False)
    applying_weights = gui_button.main(applying_options, 0, dialog_text="(True = apply weights)",
                                           title="Should the default weights be applied at the moment of merge?")  # button_dialog
    #######
    # Initialize an empty list to store DataFrames
    dfs = []

    print("The number of file paths in the list 'file_paths'is", len(file_paths))
    # exit()

    # Iterate over each file path in the list
    for file_path in file_paths:
        print(f"\n------------->The 'file_path'is {file_path}")
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)
        if applying_weights == True:
            print(df)
            df = apply_weight(df, file_path, df_sorted, verbose=verbose)
            # exit()
        else:
            print("Not applying any weighting during merge (!)")
        print("**********before resolution")
        df = resolution.main(df, decimal_points=2) # Resolution in th X-axis
        # Add a new column to identify the source file
        file_name = file_path.split('/')[-1]  # Extract file name from file path
        df['source'] = file_name
        # Append the DataFrame to the list of DataFrames
        dfs.append(df)

    print("What is 'dfs'?", type(dfs), dfs)

    sum_dataframe = sum_df.main(dfs)
    sum_dataframe.to_csv("INTER/sum_probabilities.csv", index=False)
        
    if verbose:
        graph_df.main(sum_dataframe, title="(sum)", savepath="INTER/"+"sum.png")
    
    # Concatenate all DataFrames in the list along rows
    combined_df = pd.concat(dfs, ignore_index=True)
    
    if verbose:
        graph_df.main(combined_df, title="(concatenated)", savepath="INTER/"+"conc.png")

        print("combined_df:")
        print(combined_df.head())
    
    # Save the resulting DataFrame to a new CSV file
    combined_df.to_csv("INTER/combined_probabilities.csv", index=False)
    
    return combined_df


if __name__ == "__main__":
    file_paths = [
    "../plotly/OUTPUT/exp16a_pdps_audio-mic/exp16a_pdps_audio-mic-EntropyEnergy.csv",
    "../plotly/OUTPUT/exp16a_pdps_audio-mic/exp16a_pdps_audio-mic-Energy.csv",
    "../plotly/OUTPUT/exp16a_pdps_audio-mic/exp16a_pdps_audio-mic-SpectralEntropy.csv"
    ]
    main(file_paths)
