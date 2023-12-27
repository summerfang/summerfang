import openai, os
from ast import literal_eval

import pandas as pd
import numpy as np


df = pd.read_csv('./articledb/embeddings.csv', index_col=0)
df['embeddings'] = df['embeddings'].apply(literal_eval).apply(np.array)
