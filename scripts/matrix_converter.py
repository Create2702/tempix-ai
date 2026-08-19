import pandas as pd
import torch

def convert(csv_file_name: str) -> list:
    data = pd.read_csv(csv_file_name)
    clear_data = data.iloc[:, 2:]
    matrix = torch.tensor(clear_data.values)
    return matrix