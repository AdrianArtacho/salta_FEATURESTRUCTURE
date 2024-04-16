import pandas as pd

def main(csv_path, prefix, separator='_', verbose=False):
    # Load the CSV file
    df = pd.read_csv(csv_path)

    # Modify the 'feature' column by prefixing 'prt_' to each string
    df['feature'] = prefix + separator + df['feature']

    # Save the modified DataFrame back to a new CSV file
    df.to_csv(csv_path, index=False)
    if verbose:
        print("The feature names in", csv_path, 'have been renamed')

if __name__ == "__main__":
    csv_path = 'INTER/testu51/weights_testu51.csv'
    prefix = 'prt'
    main(csv_path, prefix, verbose=True)