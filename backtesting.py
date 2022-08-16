import numpy as np

# 기간수익률
def calculate_hpr(initial_value, final_value):
    hpr = (final_value - initial_value) / initial_value
    hpr = round(hpr*100, 2)
    return hpr

# 연평균 복리 수익률
def calculate_cagr(initial_value, final_value, period):
    cagr = (final_value / initial_value) ** (1 / period) - 1
    cagr = round(cagr*100, 2)
    return cagr

# 최대 낙폭
def calculate_mdd(price_array):
    arr = np.array(price_array)
    idx_lower = np.argmin(arr - np.maximum.accumulate(arr))
    idx_upper = np.argmax(arr[:idx_lower])
    mdd = (arr[idx_lower] - arr[idx_upper]) / arr[idx_upper]
    return mdd