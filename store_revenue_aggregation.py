import numpy as np

# Daily revenue for 4 stores over 7 days. [Shape of (7,4)]

arr = np.array([
                [254,541,257,384],
                [498,614,587,354],
                [421,358,752,901],
                [825,395,497,234],
                [351,465,794,649],
                [846,647,449,358],
                [921,694,264,816]
            ])

total_revenue_per_store = np.sum(arr, axis=0)
print(f"Total revenue per store is, {total_revenue_per_store}")

total_revenue_per_day = np.sum(arr, axis=1)
print(f"Total revenue per day is, {total_revenue_per_day}")

average_daily_revenue_per_store = np.average(arr, axis=0)
print(f"Average daily revenue per store is, {average_daily_revenue_per_store}")

average_daily_revenue_per_day = np.average(arr, axis= 1)
print(f"Average daily revenue per day is, {average_daily_revenue_per_day}")