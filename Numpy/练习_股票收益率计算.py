import numpy as np

prices = np.array([100, 102, 101, 105, 107])

returns = (prices[1:] - prices[:-1])/prices[:-1]
returns = np.round(returns,4)

print("每日收益率:", returns)

