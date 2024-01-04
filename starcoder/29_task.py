import pandas as pd


def average_price(csv_file):
    """ 
    Returns the average price of all the products in the csv_file.
    The price is in the column 'Price'.
    """
    df = pd.read_csv(csv_file)
    return df['Price'].mean()
