
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

def process_confidence(description_text):
    confidence_header='&confidence-text='

    if description_text:  # Check if the string is not empty
        modified_text = description_text.replace(' ', '+')
        confidence_text = confidence_header+modified_text
        # print(confidence_text)
        return confidence_text
    else:
        return ""

def process_peaks_distance(distance_value):
    distance_header = '&peaks='

    if distance_value:  # Check if the string is not empty
        distance_text = distance_header+str(distance_value)
        print(distance_text)
        return distance_text
    else:
        return ""

def main(folder_path, general_url='https://adrianartacho.github.io/SALTA/?file=', 
         distance=20, verbose=False):

    # Process the files in the folder
    salta_filename, weights_string, description_text = process_files(folder_path)

    confidence_text = process_confidence(description_text)
    distance_text = process_peaks_distance(distance)

    concatenated_string = general_url+salta_filename+weights_string+confidence_text+distance_text

    if verbose:
        print("URL string:")
        print(concatenated_string)
    
    return concatenated_string, description_text
    

if __name__ == "__main__":
    old_url = 'https://adrianartacho.github.io/SALTA/?file=testu51.csv&wEnergy=0.8&wEntropyEnergy=0.7&wMFCC10=0.7&wMFCC11=0.7&wMFCC12=1&wMFCC13=0.7&wMFCC2=0.7&wMFCC3=1&wMFCC4=0.7&wMFCC5=0.7&wMFCC6=0.7&wMFCC7=0.7&wMFCC8=0.7&wMFCC9=0.7&wSpectralCentroid=0.7&wSpectralEntropy=0.7&wd=0.7'
    # Define the folder path
    folder_path = 'OUTPUT/exp0b_SALTA'
    main(folder_path)

    # 'https://adrianartacho.github.io/SALTA/?file=exp0b_SALTA.csv&wrightknee=1&wleftheel=0.95&wleftfootindex=0.41&wleftelbow=0.25&wrightshoulder=0.15&wrightankle=0.14&wrightheel=0.12&wrightear=0.1&wrightelbow=0.07&wrightwrist=0.07&wleftindex1=0.06&wmouthleft=0.06&wleftpinky=0.06&wleftthumb=0.06&wleftwrist=0.06&wmouthright=0.06&wrighteye=0.06&wnose=0.05&wlefteyeouter=0.05&wrightfoot=0.05&wlefteye=0.05&wlefteyeinner=0.05&wrightthumb=0.05&wleftknee=0.04&wrightpinky=0.04&wrightindex=0.04&wleftshoulder=0.03&wleftear=0.03&wrighthip=0&wlefthip=0'
    # 'https://adrianartacho.github.io/SALTA/?file=exp0b_SALTA.csv&wrightknee=1&wleftheel=0.95&wleftfootindex=0.41&wleftelbow=0.25&wrightshoulder=0.15&wrightankle=0.14&wrightheel=0.12&wrightear=0.1&wrightelbow=0.07&wrightwrist=0.07&wleftindex1=0.06&wmouthleft=0.06&wleftpinky=0.06&wleftthumb=0.06&wleftwrist=0.06&wmouthright=0.06&wrighteye=0.06&wnose=0.05&wlefteyeouter=0.05&wrightfoot=0.05&wlefteye=0.05&wlefteyeinner=0.05&wrightthumb=0.05&wleftknee=0.04&wrightpinky=0.04&wrightindex=0.04&wleftshoulder=0.03&wleftear=0.03&wrighthip=0&wlefthip=0&peaks=55'