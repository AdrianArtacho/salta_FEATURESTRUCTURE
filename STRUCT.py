import gui.gui_enterstring as gui_enterstring
import gui.gui_menu as gui_menu
import gui.gui_browse as gui_browse
import gui.gui_check as gui_check
import gui.gui_buttons as gui_buttons
import os
import json
import pandas as pd
import write_weights
import color_choice
import resolution
import aggregate
import create_folder
import STRUCT_class
import empty_folder

# selected_option = gui_buttons.main(["Yes", "No"], "Yes",
#          dialog_text="Select an Option",
#          title="Proceed with more features/classes?")  # button_dialog
# # (["Yes", "No", "Maybe"], "Yes")
# print(selected_option)
# exit()

## ENTER PROJECT NAME AND DESCRIPTION
proj_name = gui_enterstring.main('This string will identify the overall project.',
                                 'Merge Name',
                                 'project ID',
                                 default_text='test')
proj_description = gui_enterstring.main('You may enter a short description here...',
                                        'Description:',
                                        'Description',
                                        default_text='Just doing some tests over here...')

empty_folder.main("INTER/") # Clears the "INTER/" folder, except .gitkeep

done_with_project = False

while done_with_project == False:
    done_with_class, selected_folder_path, selected_folder_name, inter_filepath = STRUCT_class.main()
    # print("done_with_class:::", done_with_class)
    # print("selected_folder_path:::", selected_folder_path) 
    # print("selected_folder_name:::", selected_folder_name)
    # print("inter_filepath:::", inter_filepath)
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
        selected_option = gui_buttons.main(options, "Yes",dialog_text="Select an Option",
                                           title="Proceed with more features/classes?")  # button_dialog
        # print(selected_option)
        if selected_option == options[1]:
            done_with_project = True

else:
    done_with_project = True
    print("Now --REALLY done PROJECT!")
# project_color = color_choice.main()

# write_weights.main(df_sorted, 
#                     project_id=class_name, 
#                     project_color=project_color,
#                     csv_file='weights_'+class_name+'.csv')