import torch
import torch.nn as nn

class Tempix(nn.Module):
    def __init__(self, input_size: int, hid1_size: int, hid2_size: int, hid3_size: int, out_size: int) -> None:
        super().__init__()
        self.hid1 = nn.Linear(input_size, hid1_size)
        self.hid2 = nn.Linear(hid1_size, hid2_size)
        self.hid3 = nn.Linear(hid2_size, hid3_size)
        self.out = nn.Linear(hid3_size, out_size)

        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)

    def forward(self, input_data: torch.Tensor) -> torch.Tensor:
        h1 = self.dropout(self.relu(self.hid1(input_data)))
        h2 = self.dropout(self.relu(self.hid2(h1)))
        h3 = self.dropout(self.relu(self.hid3(h2)))
        out = self.out(h3)
        return out