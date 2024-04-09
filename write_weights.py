import pandas as pd
import create_folder

def main(df, 
         project_id='',
         project_color='red',
         output_path='OUTPUT/',
         csv_file='output.csv'):


    # CREATE A PROJECT FOLDER IN CASE IT FOESN'T EXIST
    create_folder.main(project_id, local_folder = 'OUTPUT')

    #Resulting csv filepath
    filepath = output_path+project_id+'/'+csv_file

    # Drop columns except 'Feature', 'Weight'
    # df = df.drop(columns=['Path'])
    desired_columns = ['Feature', 'Weight']
    df = df.loc[:, desired_columns]

    # Insert the 'class' column with values 'project_id' after 'Feature' column
    df.insert(df.columns.get_loc('Feature') + 1, 'class', project_id)

    # Insert the 'color' column with values 'red' after 'Weight' column
    df.insert(df.columns.get_loc('Weight') + 1, 'color', project_color)

    print(df.head())
    # exit()

    # Write DataFrame to CSV with lowercase column names
    df.to_csv(filepath, index=False, header=['feature', 'class', 'weight', 'color'])

    print(f"CSV file '{filepath}' has been created.")


if __name__ == "__main__":
    # Example DataFrame creation (replace this with your actual DataFrame)
    data = {
        'Feature': ['Feature1', 'Feature2', 'Feature3'],
        'Class': ['Class1', 'Class2', 'Class3'],
        'Weight': [1, 2, 3],
        'Color': ['Red', 'Green', 'Blue']
    }
    df = pd.DataFrame(data)
    main(df, project_id='testu61', csv_file='output_test.csv')