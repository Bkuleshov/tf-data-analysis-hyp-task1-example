import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 818742406 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    sales = np.array([x_success, y_success])
    counts = np.array([x_cnt, y_cnt])
    zstat, pvalue = proportions_ztest(sales, counts, alternative='smaller')
    return pvalue < 0.04
