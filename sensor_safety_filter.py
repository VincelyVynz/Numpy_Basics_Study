import numpy as np

# Boolean Filtering

readings = np.array([12.5, 7.8, 15.2, 9.1, 20.3, 5.4, 11.0, 18.7, 6.9, 14.6, 8.2])

safety_threshold = 13.5

mask_arr = readings > safety_threshold
unsafe_readings = readings[mask_arr]

print(f"Boolean mask: {mask_arr}")
print(f"Unsafe readings: {unsafe_readings}")