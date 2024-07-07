import pandas as pd
import numpy as np
import pyt.paths.parse_path as parse_path

def savefile_path(file_path, output_folder, verbose=False):
    name_string, ext_string = parse_path.main(file_path)

    if verbose:
        print(name_string, ext_string)

    # Find the position of the first underscore
    underscore_index = name_string.find('_')

    # Extract substring before the underscore
    substring_before_underscore = name_string[:underscore_index]

    # Print the result
    if verbose:
        print("substring_before_underscore:", substring_before_underscore)

    generated_path = output_folder+name_string+'/'+substring_before_underscore+'.csv'

    if verbose:
        print("generated_path:", generated_path)
    
    # exit()
    return generated_path

def main(input_path, output_folder='OUTPUT/', factor=100, verbose=True): # multiply_and_round_x_axis

    # determine savefile path
    generated_path = savefile_path(input_path, output_folder)
    if verbose:
        print("generated_path:", generated_path)

    # exit()

    # Load the CSV file
    df = pd.read_csv(input_path)

    # Multiply all values in the 'x_axis' column by the given factor and round up to the nearest integer
    df['x_axis'] = np.ceil(df['x_axis'] * factor).astype(int)

    # Save the modified DataFrame to a CSV file
    df.to_csv(generated_path, index=False)

    print(f"Modified file saved to {generated_path}")

    return generated_path

if __name__ == "__main__":
    # Example usage
    input_file_path = 'OUTPUT/exp0b_SALTA/exp0b_SALTA.csv'
    # output_file_path = 'OUTPUT/exp0b_SALTA/exp0b_SALTA_round.csv'
    main(input_file_path)
