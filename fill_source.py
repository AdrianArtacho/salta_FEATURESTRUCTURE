import pandas as pd
import sys

def main(df):
    # Load the CSV file
    # df = pd.read_csv(file_path)

    # Fill missing 'source' values with 'unknown'
    df['source'].fillna('unknown', inplace=True)

    # Save the updated dataframe back to a CSV file
    output_file_path = file_path.replace('.csv', '_filled.csv')
    df.to_csv(output_file_path, index=False)

    print(f"Updated file saved as: {output_file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fill_missing_source.py <path_to_csv_file>")
    else:
        file_path = sys.argv[1]
        main(file_path)
