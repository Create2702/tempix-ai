import pandas as pd

def convert(csv_file_name: str) -> list:
    data = pd.read_csv(csv_file_name)
    clear_data = data.iloc[:, 2:]
    matrix = [clear_data.values.flatten().tolist()]
    return matrix