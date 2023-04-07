import pandas as pd
import numpy as np

from scipy.stats import expon

chat_id = 845786312 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    loc = 1 / 2
    #scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    #return loc - scale * norm.ppf(1 - alpha / 2), \
    #       loc - scale * norm.ppf(alpha / 2)
    a = loc - (2 / (44 * 44)) * (expon.ppf(1 - alpha / 2) / (x.min() * len(x)))
    b = loc - (2 / (44 * 44)) * (expon.ppf(alpha / 2) / (x.min() * len(x)))
    return a, b
