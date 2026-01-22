import numpy as np

arr = np.array([
    [945, 657, 365],
    [948, 660, 368],
    [952, 655, 370],
    [950, 658, 372],
    [955, 662, 375],
    [960, 665, 378],
    [958, 663, 380],
    [962, 668, 382],
    [965, 670, 385],
    [970, 675, 388]
])

current_prices = arr[1:, :]
previous_prices = arr[:9, :]
print(current_prices)
print(previous_prices)
# Calculation:
# Daily percentage returns = (current price - previous day price)/ previous day price

daily_percentage_returns = (current_prices - previous_prices)/ previous_prices

print(f"Daily percentage returns is: \n{daily_percentage_returns}")