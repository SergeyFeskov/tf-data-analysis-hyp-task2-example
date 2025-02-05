import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp

chat_id = 875744266

def solution(x: np.array, y: np.array) -> bool:
    return anderson_ksamp([x, y]).pvalue < 0.07
