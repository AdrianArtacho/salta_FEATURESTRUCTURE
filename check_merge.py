import pandas as pd
import gui.gui_browse as gui_browse
import os

def main(file_path='', params_initbrowser='OUTPUT/', column_name='feature',verbose=False):

    if file_path == '':
        chosen_file = gui_browse.main(params_title='Choose .cv file to check', 
            params_initbrowser=params_initbrowser,
            params_extensions='.csv',               # E.g. '.csv'
            size=(40,20),
            verbose=False)
    else:
        chosen_file = file_path
    
    if verbose:
        print("chosen_file:", chosen_file)
    # exit()
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(chosen_file)

    # Extract unique values from the 'feature' column
    unique_features = df[column_name].unique().tolist()

    if verbose:
        print("List of unique features:")
    
    for feature in unique_features:
        if verbose:
            print(feature)

    if verbose:
        print("Total unique features: ", len(unique_features))

    # Extract the directory path
    folder_path = os.path.dirname(chosen_file)

    if verbose:
        print("folder_path:", folder_path)

    return unique_features, folder_path


if __name__ == '__main__':
    main()