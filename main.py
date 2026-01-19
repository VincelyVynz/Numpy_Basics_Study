import numpy as np

# Numpy random

rng = np.random.default_rng()

print(rng.integers(1,51, (3,2)))

print(np.random.uniform())

# ages = np.array([
#     [21, 17, 19, 20, 16, 30, 18, 65],
#     [39, 22, 15, 99, 18, 19, 20, 21]
# ])
#
# #Filters using where
#
# adults = np.where(ages>= 18, ages, 'Minor')
#print(adults)

# Filters

# teenagers = ages[ages < 18]
# adults = ages[(ages >= 18) & (ages < 65)]
# seniors = ages[ages >= 65]
# evens = ages[ages % 2 == 0]
# odds  = ages[ages % 2 != 0]
#
# print(teenagers)
# print(adults)
# print(seniors)
# print(evens)
# print(odds)

# Aggregate Functions
#
# arr_1 = np.array([[1,2,3,4,5],
#                   [6,7,8,9,10]])
#
# print(np.sum(arr_1))

# Broadcasting

# array1 = np.array([[1, 2, 3, 4]])
# array2 = np.array([[1], [2], [3], [4]])
#
# print(array1.shape)
# print(array2.shape)
# print(array1)
# print(array2)
# print()
# print(array1 * array2)

# Comparison Operators

# scores = np.array([92, 81, 68, 100, 55])
#
# print(scores == 100)
# print(scores >= 60)
# print(scores <= 90)
# scores[scores< 70] = 0
# print(scores)


# Element wise arithmetic

# arr_1 = np.array([1,2,3,4,5])
# arr_2 = np.array([6,7,8,9,10])
# print(arr_1 + arr_2)



# arr_1 = np.array([1,2.4,3.7,4.1,5.9])

# Scalar Arithmetics
# print(arr_1  + 2)
# print(arr_1 - 2)
# print(arr_1 /2)
# print(arr_1 % 2)
# print(arr_1 ** 2)


# Vectorized Arithmetics
# print(np.sqrt(arr_1))
# print(np.round(arr_1))
# print(np.pi)


# Calculating Area of Circle:
# radii = np.array([1,2,3])
# print(np.pi * radii ** 2)






# arr = np.array([[1,2,3,4],
#                 [5,6,7,8],
#                 [9,10,11,12],
#                 [13,14,15,16]])
#
# print(arr[:,1])
#


# arr = np.array([[['A', 'B', 'C'],['D', 'E', 'F'],['X', 'Y', 'Z']],
#                 [['G', 'H', 'I'],['J', 'K', 'L'],['M', 'N', 'O']],
#                 [['P', 'Q', 'R'],['S', 'T', 'U'],['V', 'W', ' ']]])
#
# print(arr.ndim)
# print(arr.shape)
# print(arr[1,2,1])
# print(arr[1,2,1])