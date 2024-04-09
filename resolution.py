import pandas as pd

## RENDER IN DIFFERENT RESOLUTION
def main(df, decimal_points=2):
    df_copy = df.copy()
    # Convert 'x_axis' column to numeric type
    df_copy['x_axis'] = pd.to_numeric(df_copy['x_axis'], errors='coerce')
    # Round 'x_axis' to the specified resolution
    df_copy['x_axis'] = df_copy['x_axis'].round(decimal_points)
    # Group by rounded 'x_axis' and calculate mean for 'y_axis'
    result_df = df_copy.groupby('x_axis')['y_axis'].mean().reset_index()
    # Since 'feature' and 'tuples' are non-numeric columns, we'll simply take the first occurrence for each group
    non_numeric_cols = ['feature', 'tuples']
    for col in non_numeric_cols:
        result_df[col] = df_copy.groupby('x_axis')[col].first().reset_index(drop=True)
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
    main(df, decimal_points=2)