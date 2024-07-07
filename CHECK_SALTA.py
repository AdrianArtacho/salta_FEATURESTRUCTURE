import pandas as pd

def analyze_file(input_path, output_path='check.csv'):
    # Load the CSV file
    df = pd.read_csv(input_path)

    # Prepare the DataFrame
    features = df['feature'].unique()
    data = []

    for feature in features:
        feature_df = df[df['feature'] == feature]
        instance_count = len(feature_df)
        min_x = feature_df['x_axis'].min()
        min_y = feature_df['y_axis'].min()
        range_x = feature_df['x_axis'].max() - min_x
        range_y = feature_df['y_axis'].max() - min_y
        data.append([feature, instance_count, min_x, min_y, range_x, range_y])

    # Create a new DataFrame with the required information
    summary_df = pd.DataFrame(data, columns=['feature', 'instance_count', 'min_x', 'min_y', 'range_x', 'range_y'])

    # Save the summary DataFrame to a CSV file
    summary_df.to_csv(output_path, index=False)

    print(f"Summary saved to {output_path}")

if __name__ == "__main__":
    # Example usage
    input_file_path = 'OUTPUT/exp0b_SALTA/exp0b_SALTA.csv'
    output_file_path = 'OUTPUT/exp0b_SALTA/exp0b_check.csv'
    analyze_file(input_file_path, output_file_path)
