import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 5459656416 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    x_cr = x_success / x_cnt
    y_cr = y_success / y_cnt
    uplift = (y_cr - x_cr) / x_cr
    z_score = uplift / (1.0 / y_cnt + 1.0 / x_cnt)**0.5
    p_value = norm.sf(abs(z_score))
    return p_value < 0.05
