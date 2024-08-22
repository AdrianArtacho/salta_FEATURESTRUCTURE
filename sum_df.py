import pandas as pd
import numpy as np

def main(dataframes):   # Sum curves
    """
    Sums the y_axis values from multiple DataFrames, interpolating them over a common x_axis range.

    Parameters:
    dataframes (list of pandas.DataFrame): A list of DataFrames, each with 'x_axis' and 'y_axis' columns.

    Returns:
    pandas.DataFrame: A DataFrame with the common x_axis and the summed y_axis values.
    """
    if not dataframes:
        raise ValueError("The list of dataframes is empty.")
    
    # Step 1: Create a common x_axis range by finding the union of all x_axis values
    common_x_axis = np.array([])  # Initialize as an empty array
    for df in dataframes:
        common_x_axis = np.union1d(common_x_axis, df['x_axis'])
    
    # Step 2: Initialize the summed y_axis array with zeros
    summed_y_axis = np.zeros_like(common_x_axis, dtype=float)
    
    # Step 3: Interpolate and sum the y_axis values from each DataFrame
    for df in dataframes:
        # Interpolate y_axis values over the common x_axis range
        y_interp = pd.Series(df['y_axis'].values, index=df['x_axis']).reindex(common_x_axis).interpolate(method='linear').fillna(0)
        # Add the interpolated y_axis values to the sum
        summed_y_axis += y_interp.values
    
    # Step 4: Create a new DataFrame for the summed curve
    summed_df = pd.DataFrame({
        'x_axis': common_x_axis,
        'y_axis': summed_y_axis
    })
    
    return summed_df

# Example Usage
if __name__ == "__main__":
    # Example DataFrames with different x_axis ranges
    df1 = pd.DataFrame({
        'x_axis': [1, 2, 3, 4, 5],
        'y_axis': [10, 20, 30, 40, 50]
    })
    
    df2 = pd.DataFrame({
        'x_axis': [4, 5, 6, 7, 8],
        'y_axis': [15, 25, 35, 45, 55]
    })
    
    df3 = pd.DataFrame({
        'x_axis': [2, 4, 6, 8, 10],
        'y_axis': [5, 10, 15, 20, 25]
    })
    
    # Sum the curves from the DataFrames
    summed_df = main([df1, df2, df3])
    
    print(summed_df)
