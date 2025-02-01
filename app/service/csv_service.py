import pandas as pd

def read_csv(file_path):
    df = pd.read_csv(file_path)
    print(df.head())
    return df
