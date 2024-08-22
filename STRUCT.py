import gui.gui_enterstring_t as gui_enterstring
# import gui.gui_menu as gui_menu
# import gui.gui_browse as gui_browse
# import gui.gui_check as gui_check
import gui.gui_button_t as gui_button
# import os
# import json
# import pandas as pd
# import write_weights
# import color_choice

# import aggregate
# import pyt.paths.create_folder as create_folder
import STRUCT_class
import pyt.paths.empty_folder as empty_folder
import report
import INTEGRATE_sets
# import deriv_csvnames
# import deriv_jsonnames
import check_merge
import APP_url
import URL_window_t as URL_window
import url_function
import multiply_round

verbose=True

## ENTER PROJECT NAME AND DESCRIPTION
proj_name = gui_enterstring.main('This string will identify the overall project.',
                                 'Merge Name',
                                 'project ID',
                                 default_text='exp?_SALTA')
# exit()
proj_description = gui_enterstring.main('You may enter a short description here...',
                                        'Description:',
                                        'Description',
                                        default_text='Just doing some tests over here...')


empty_folder.main("INTER/") # Clears the "INTER/" folder, except .gitkeep
# exit()

done_with_project = False
rename_features_after_class = False

while done_with_project == False:
    done_with_class, selected_folder_path, selected_folder_name, inter_filepath = STRUCT_class.main()
    print("done_with_class:::", done_with_class)
    print("selected_folder_path:::", selected_folder_path) 
    print("selected_folder_name:::", selected_folder_name)
    print("inter_filepath:::", inter_filepath)
    # exit()
    while done_with_class == False:
        done_with_class, 
        selected_folder_path, 
        selected_folder_name, 
        done_with_class, selected_folder_path, selected_folder_name, inter_filepath = STRUCT_class.main(selected_folder_path=selected_folder_path,
                                        selected_folder_name=selected_folder_name,
                                        inter_filepath=inter_filepath)
        print("inter_filepath::", inter_filepath)
        print("All returns:::", done_with_class, selected_folder_path, selected_folder_name, inter_filepath)
    else:
        print("Now --REALLY done CLASS!")


        options = ["Yes", "No"]
        selected_option = gui_button.main(options, 0, dialog_text="Select an Option",
                                           title="Proceed with more features/classes?")  # button_dialog
        # exit()
        # print(selected_option)
        if selected_option == options[0]:
            print("HERE rename features?")
            rename_features_after_class = True
            
        elif selected_option == options[1]:
            done_with_project = True


else:
    done_with_project = True
    print("Now --REALLY done PROJECT!")

# exit()
print("integrating...")
# exit()

print("project_name:",proj_name)
print("rename_features_after_class:",rename_features_after_class)


integration_dir = INTEGRATE_sets.main(project_name=proj_name, 
                                output_folder='OUTPUT',
                                directory = "INTER/",
                                rename_features_after_class=rename_features_after_class)

# exit()
report.main(proj_description, proj_name, output_folder='OUTPUT', verbose=True)

# exit()
## Check result

# merge_file = '/Users/artacho/Work/Dissertation/CODE/salta/featurestructure/OUTPUT/proj/proj.csv'
merge_file = 'OUTPUT/'+proj_name+'/'+proj_name+'.csv'
unique_features, folder_path = check_merge.main(file_path=merge_file)
merge_unique = len(unique_features)
# exit()
if verbose:
    print("merge_file:", merge_file)
    # exit()

# wei_file = '/Users/artacho/Work/Dissertation/CODE/salta/featurestructure/OUTPUT/proj/proj.csv'
wei_file = 'OUTPUT/'+proj_name+'/weights_'+proj_name+'.csv'
unique_features, folder_path = check_merge.main(file_path=wei_file,params_initbrowser=folder_path)
wei_unique = len(unique_features)
# exit()
if merge_unique == wei_unique:
    print("Feature check successful!")
else: 
    print("There's a mismatch in the amount of features in the merge file and the weights file...")
print(merge_unique, "unique features in merge file;", wei_unique, "in weights file.")

# exit()
concatenated_string, description_text = APP_url.main(integration_dir, verbose=False)
print("concatenated_string:")
print(concatenated_string)

rounded_file_path = multiply_round.main(merge_file)

url_function.main(concatenated_string, integration_dir, description=description_text)

URL_window.main(font_size=32, text4_width=30,
                text2=rounded_file_path,
                hyperlink2=concatenated_string,
                text4=concatenated_string)

