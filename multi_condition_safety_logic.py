import numpy as np

# Working with multiple conditions

readings = np.array([12.5, 7.8, 15.2, 9.1, 20.3, 5.4, 11.0, 18.7, 6.9, 14.6, 8.2])

low_threshold = 7
high_threshold = 13.5

low_mask = readings < low_threshold
high_mask = readings > high_threshold

abnormal_mask = low_mask | high_mask


print(f"abnormal_mask: {abnormal_mask}")
print(f"low_mask: {low_mask}")
print(f"high_mask: {high_mask}")
