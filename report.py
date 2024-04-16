
def main(proj_description, proj_name, output_folder='OUTPUT', verbose=False):
    if verbose:
        print("writing report...")
    
    # Open a file in write mode
    txt_path = output_folder+'/'+proj_name+'/'+proj_name+'_description.txt'
    with open(txt_path, 'w') as file:
        # Write the string to the file
        file.write(proj_description)

    if verbose:
        print("Project report was saved in", txt_path)



if __name__ == "__main__":
    # Define the string to be written to the file
    proj_name = 'proj'
    proj_description = "This is a detailed description of the project."
    main(proj_description,proj_name, verbose=True)