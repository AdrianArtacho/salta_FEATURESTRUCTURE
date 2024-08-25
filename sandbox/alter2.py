import os
# alter_folder="INPUT"
alter_folder="../plotly/OUTPUT"
orig_folder="OUTPUT"

# original_path = "OUTPUT/testu51/testu51-MFCC2.csv"
original_path = "OUTPUT/exp13b_pdps_mpipe-irt/exp13b_pdps_mpipe-irt-leftear.csv"


filename = os.path.basename(original_path)  # Extract the filename
exp_dir = filename.split('_')[0]    # Extract the exp_dir by splitting the filename at the first underscore
sub_dir = original_path.replace(f"{orig_folder}/", "")  # Construct the new path by inserting exp_dir after "OUTPUT/"
new_path = os.path.join(alter_folder, exp_dir, sub_dir)  # Create the new path

print(new_path)

# alternative2_path = os.path.join(alter_folder, os.path.relpath(original_path, orig_folder))
# print(alternative2_path)

# OUTPUT/exp13b_pdps_mpipe-irt/exp13b_pdps_mpipe-irt-leftear.csv
#  INPUT/exp13b_pdps_mpipe-irt/exp13b_pdps_mpipe-irt-leftear.csv