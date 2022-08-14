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