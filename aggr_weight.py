from pathlib import Path

def get_filename_from_path(path):
    return Path(path).name

def get_weight_by_filename(df, filename):
    # Search for the filename in the 'Filename' column
    result = df[df['Filename'] == filename]['Weight']
    
    # Check if any result is found
    if not result.empty:
        return result.iloc[0]  # Return the first (and likely only) matching weight
    else:
        return None  # Return None or a default value if the filename is not found


def main(list_of_features_to_aggregate, df_sorted):
    # print("Here we go!")
    # print(list_of_features_to_aggregate)
    list_of_aggregated_weights = []

    for filepath in list_of_features_to_aggregate:
        print(filepath)
        filename = get_filename_from_path(filepath)
        print(filename)
        weight = float(get_weight_by_filename(df_sorted, filename))
        print(weight)
        list_of_aggregated_weights.append(weight)
    
    print("\nList of aggregated weights:")
    print(list_of_aggregated_weights)
    max_weight_in_list = max(list_of_aggregated_weights)
    print("max_weight_in_list:", max_weight_in_list)
    print(df_sorted)
    # exit()
    return max_weight_in_list

if __name__ == "__main__":
    main()