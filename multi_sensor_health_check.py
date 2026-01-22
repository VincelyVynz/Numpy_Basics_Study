import numpy as np

# Sensor data from 6 machines with 3 sensors each

sensor_data = np.array([
    [7.2,  9.1, 12.5],
    [5.5, 10.0, 11.2],
    [8.0, 14.0, 12.0],
    [6.5,  7.8,  9.0],
    [4.0, 15.0, 10.0],
    [6.8, 12.5, 13.0]
])

low_threshold = 6.0
high_threshold = 13.5

low_mask = sensor_data < low_threshold
high_mask = sensor_data > high_threshold


abnormal_mask = (low_mask | high_mask)
print(abnormal_mask)

machine_wise_abnormal_mask = abnormal_mask.any(axis=1)

print("Machine wise abnormal mask: \n", machine_wise_abnormal_mask)