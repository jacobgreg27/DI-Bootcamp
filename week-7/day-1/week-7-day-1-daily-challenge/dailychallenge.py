# Daily Challenge
# The Power Of NumPy
# We said that NumPy is pretty much a list on steroids. Let’s see that in action.

# For the tasks below, do them using a regular Python list implementation, and then use NumPy.

# Create a table (i.e. a 2d array) of size M x N filled with random integers between 1 and 100,
# where 1 < N < 40 and 1 < M < 50.

# Print out the third row

# Print out the third column

# Set every element in the last row equal to 7

# Set every element in the last column equal the sum of the first two columns. (note: the result of
# the sum is a list which will the same length as the last column)

import random


M = 5
N = 10
matrix = [[random.randint(1, 100) for j in range(N)] for i in range(M)]


print(matrix[2])


print([row[2] for row in matrix])


matrix[-1] = [7] * N


sums = [sum(row[:2]) for row in matrix]
for i in range(M):
    matrix[i][-1] = sums[i]

print(matrix)






