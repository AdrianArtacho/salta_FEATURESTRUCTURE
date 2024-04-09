import pandas as pd

## RENDER IN DIFFERENT RESOLUTION
def main(df):
    # Convert 'x_axis' and 'y_axis' columns to numeric type
    df['x_axis'] = pd.to_numeric(df['x_axis'], errors='coerce')
    df['y_axis'] = pd.to_numeric(df['y_axis'], errors='coerce')
    # Round index to 2 decimal points
    df.index = df.index.round(2)
    # Group by rounded index and calculate mean for 'x_axis' and 'y_axis'
    result_df = df.groupby(level=0).agg({'x_axis': 'mean', 'y_axis': 'mean'})
    # For non-numeric columns, take the first occurrence for each group
    non_numeric_cols = [col for col in df.columns if col not in ['x_axis', 'y_axis']]
    for col in non_numeric_cols:
        result_df[col] = df.groupby(level=0)[col].first()
    # return result_df

    print(result_df.head())
    return result_df

# Example usage:
# Assuming `df` is your DataFrame representing the probability density plot
# Replace this with your actual DataFrame

# Example DataFrame:
# df = pd.DataFrame({'Probability': [0.2, 0.3, 0.5]}, index=[0.123, 0.456, 0.789])

# Rendering lower resolution
# new_df = render_lower_resolution(df)
# print(new_df)


if __name__ == "__main__":
    example_file="INPUT/testu51/testu51-MFCC9.csv"
    df = pd.read_csv(example_file)
    main(df)