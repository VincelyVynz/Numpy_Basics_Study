import numpy as np

# Sensor fail safe clamp

readings = np.array([12.5, 7.8, 15.2, 9.1, 20.3, 5.4, 11.0, 18.7, 6.9, 14.6, 8.2])

safety_threshold = 13.5

mask_arr = readings > safety_threshold

readings[mask_arr] = safety_threshold

print(readings)