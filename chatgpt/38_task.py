import pandas as pd


def clean_data(csv_file):
    """ 
    Clean and prepare the data in the csv_file, with various columns, including 'Age', 'Gender', 'Income', and 'Occupation'. 
    The function should perform the following operations:
    1. Drop rows with any missing values.
    2. Convert categorical columns ('Gender' and 'Occupation') to one-hot encoded columns.
    3. Remove outliers in the 'Age' and 'Income' columns based on a specified method (e.g., removing values beyond 1.5 times the interquartile range).
    """
    # Load the CSV file
    df = pd.read_csv(csv_file)

    # 1. Drop rows with any missing values
    df.dropna(inplace=True)

    # 2. Convert categorical columns ('Gender' and 'Occupation') to one-hot encoded columns
    df = pd.get_dummies(df, columns=['Gender', 'Occupation'])

    # 3. Remove outliers in the 'Age' and 'Income' columns
    for column in ['Age', 'Income']:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

    return df