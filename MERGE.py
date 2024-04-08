""" This script takes several timeseries in .csv format,
    and combines them... (adding the values?)
"""
import pandas as pd
import matplotlib.pyplot as plt
import gui_abstractions.gui_enterstring as gui_enterstring
import gui_abstractions.gui_multiple as gui_multiple
import gui_abstractions.gui_browsemul as gui_browsemul
import gui_abstractions.gui_menu as gui_menu
import ts_weights
import json



def main(indexes_correction_factor = 0.1,
         verbose = True):
    
    proj_name = gui_enterstring.main('This string will ideantify all files generated from here...', 
                                    'enter string:', 
                                    'Merge Name',
                                    default_text='test')
    proj_description = gui_enterstring.main('You may enter a short description here...', 
                                            'Description:', 
                                            'Description',
                                            default_text='Just doing some tests over here...')


    def merge_two_dataframes(left_df, right_df):
        """ This function takes two time series and 
            merges (adds) the y_axis based on the reference x_axis
        """
        right_df.insert(1, 'Time_right', right_df['x_axis'])
        # merge_asof
        merged_df = pd.merge_asof(left_df, right_df, on='x_axis', suffixes=('_left','_right'))
        # print(merged_df)

        merged_df['y_axis'] = merged_df.loc[:,['y_axis_left','y_axis_right']].sum(axis=1)
        # print(merged_df)

        columns_list = merged_df.columns.values.tolist()
        # print("Columns list:", columns_list)

        #--- remove all columns except x_axis and y_axis
        for column in columns_list:
            if column != 'x_axis' and column != 'y_axis':
                merged_df = merged_df.drop(columns=[column])

        return merged_df


    # Select iput path
    input_path_options = ['INPUT/', '../plotly/OUTPUT', '../../plotly/OUTPUT']
    input_path = gui_menu.main(input_path_options, 
                            "Where should we look for input files?", 
                            "Input Path", 
                            default_option=0, 
                            font=('Arial Bold', 14))


    if verbose:
        print("input_path:")
        print(input_path)
        # exit()

    # Select multiple files
    params_title = "Select (multiple) feature files \
        [TAB → SPACEBAR | RETURN → Ok]"
    # params_initbrowser = 'INPUT'
    file_list = gui_multiple.main(params_title, 
                                    input_path, 
                                    font = ("Arial", 18))

    # file_list = gui_browsemul.main(params_title=params_title, 
    #          params_initbrowser=input_path,  # Set the default folder here
    #          params_extensions=('.csv',),  # Set the allowed extensions as a tuple
    #          size=(40, 20))

    print("Selected a total of", len(file_list), "feature files to merge.")

    # if verbose:
    #     exit()

    if len(file_list) < 2:
        print("You need to select at least two files to perform a merge!!")
        exit()

    # set weights for the features

    entered_weights, weights_list = ts_weights.main(file_list, default="1")
    print("weights_list:", weights_list, type(weights_list))
    # exit()

    weights_list_as_floats = [float(x) for x in weights_list]

    # merge all files
    file_zero = file_list[0]    # feature file to which all aother will be concatenated
    file_list_adding = file_list[1:]    # the rest of the feature files

    # run function
    result_df = pd.read_csv(file_zero)
    weighting_factor = weights_list_as_floats[0]
    print("Every value in the column ['y_axis'] of",file_zero, 
        "will be multiplied by weighting factor",weighting_factor, "before merge.")
    # print(result_df.head())
    result_df['y_axis'] = result_df['y_axis'].mul(weighting_factor)
    # result_df['x_axis'] = result_df['x_axis'].mul(indexes_correction_factor)    ###########!!!!!!!!!!
    # print(result_df.head())
    # exit()

    weight_list_index = 1   # starting here (second item), since the index zero was already applied
    for addition in file_list_adding:
        feat_added = pd.read_csv(addition)

        weighting_factor = weights_list_as_floats[weight_list_index]
        feat_added['y_axis'] = feat_added['y_axis'].mul(weighting_factor)
        # feat_added['x_axis'] = feat_added['x_axis'].mul(indexes_correction_factor)  ###########!!!!!!!!!!
        print("Every value in the column ['y_axis'] of",addition, 
        "will be multiplied by weighting factor",weighting_factor, "before merge.")

        result_df = merge_two_dataframes(result_df, feat_added)
        weight_list_index = weight_list_index + 1

    print(result_df)
    # exit()

    plt.plot(result_df['x_axis'], result_df['y_axis'])
    plt.savefig('MERGED/'+proj_name+'.png', bbox_inches='tight')
    plt.show()

    # result_df = result_df.set_index('x_axis')
    # print(result_df.head())

    result_df.to_csv('MERGED/'+proj_name+'.csv', index=False)



    
    stored_data = {
        "merge_name": proj_name,
        "description": proj_description,
        "features": file_list,
        "entered_weights": entered_weights,
        "weights_list": weights_list_as_floats,
        "prediction": "not generated yet"
    }
    
    with open("OUTPUT/"+proj_name+".json", "w") as outfile:
        json.dump(stored_data, outfile, indent=4)

    return proj_name

if __name__ == "__main__":
    main(indexes_correction_factor = 0.1,
         verbose = True)