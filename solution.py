import pandas as pd
import numpy as np

from scipy.stats import expon


chat_id = 845786312

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    loc = x.min() * len(x)
    #scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    #return loc - scale * norm.ppf(1 - alpha / 2), \
    #       loc - scale * norm.ppf(alpha / 2)
    return (2 / (44 * 44)) * (- expon.ppf(1 - alpha / 2) + 1/2) / loc, (2 / (44 * 44)) * (- expon.ppf(alpha / 2) + 1/2) / loc

