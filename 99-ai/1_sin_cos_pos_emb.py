import torch
import math


def pos_emb(seq_len, d_model):
    # Create a matrix of shape (seq_len, d_model)
    pe = torch.zeros(seq_len, d_model)
    # Create a vector of shape (seq_len)
    position = torch.arange(0, seq_len, dtype=torch.float).unsqueeze(1)  # (seq_len, 1)
    # Create a vector of shape (d_model)
    div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))  # (d_model / 2)
    print("-"*100)
    print(div_term)
    print("-"*100)
    # Apply sine to even indices
    pe[:, 0::2] = torch.sin(position * div_term)  # sin(position * (10000 ** (2i / d_model))
    # Apply cosine to odd indices
    pe[:, 1::2] = torch.cos(position * div_term)  # cos(position * (10000 ** (2i / d_model))

    return pe

if __name__=='__main__':
    pe = pos_emb(10, 100)
    print(pe)