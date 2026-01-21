import numpy as np

# 6 machines, each reporting 3 sensor values Shape(6,3)

arr = np.array([
    [25,32,98],
    [54,36,45],
    [21,31,65],
    [26,51,34],
    [23,56,35],
    [27,57,36]
])

mean_per_sensor = np.mean(arr, axis = 0)

std_per_sensor = np.std(arr, axis = 0)

normalized_arr = (arr - mean_per_sensor)/std_per_sensor

print(f"Mean per sensor is {mean_per_sensor}")
print(f"Std per sensor is {std_per_sensor}")
print(f"Normalized array per sensor is {normalized_arr}")
print("All done")