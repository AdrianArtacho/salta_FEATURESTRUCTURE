
import os
import pandas as pd
import pyt.math.round_float as round_float

def find_files(folder):
    weights_file = None
    salta_file = None
    description_file = None
    
    # Iterate over files in the folder
    for filename in os.listdir(folder):
        if filename.startswith('weights_') and filename.endswith('.csv'):
            weights_file = filename
        elif filename.endswith('.csv') and not filename.startswith('weights_'):
            salta_file = filename
        elif filename.endswith('.txt'):
            description_file = filename
    
    return weights_file, salta_file, description_file

def process_files(folder):
    weights_file, salta_file, description_file = find_files(folder)
    
    if weights_file:
        weights_df = pd.read_csv(os.path.join(folder, weights_file))
        # weights_string = ''.join([f"&w{row['feature']}={row['weight']}" for _, row in weights_df.iterrows()])
        weights_string = ''.join([f"&w{row['feature']}={round_float.main(row['weight'])}" for _, row in weights_df.iterrows()])
    else:
        weights_string = None
    
    salta_filename = salta_file if salta_file else None
    
    if description_file:
        with open(os.path.join(folder, description_file), 'r') as file:
            description_text = file.read()
    else:
        description_text = None
    
    return salta_filename, weights_string, description_text

def main(folder_path, general_url='https://adrianartacho.github.io/SALTA/?file=', verbose=False):

    # Process the files in the folder
    salta_filename, weights_string, description_text = process_files(folder_path)

    # Display the results
    # print("Salta Filename:", salta_filename)
    # print("Description Text:", description_text)
    # print("Weights String:", weights_string)

    concatenated_string = general_url+salta_filename+weights_string

    if verbose:
        print("URL string:")
        print(concatenated_string)
    
    return concatenated_string
    

if __name__ == "__main__":
    old_url = 'https://adrianartacho.github.io/SALTA/?file=testu51.csv&wEnergy=0.8&wEntropyEnergy=0.7&wMFCC10=0.7&wMFCC11=0.7&wMFCC12=1&wMFCC13=0.7&wMFCC2=0.7&wMFCC3=1&wMFCC4=0.7&wMFCC5=0.7&wMFCC6=0.7&wMFCC7=0.7&wMFCC8=0.7&wMFCC9=0.7&wSpectralCentroid=0.7&wSpectralEntropy=0.7&wd=0.7'
    # Define the folder path
    folder_path = 'OUTPUT/exp1_SALTA'
    main(folder_path)