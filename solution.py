import pandas as pd
import numpy as np


chat_id = 818742406 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return (x_success / x_cnt) > (1.04 * y_success / y_cnt) # Ваш ответ, True или False
