import numpy as np

def fahrenheit_to_celsius(f):
    return (f - 32) * (5/9)

vectorized_conversion = np.vectorize(fahrenheit_to_celsius)

# Given array of temperatures
temperatures_f = np.array([32, 68, 100, 212, 77])
temperatures_c = vectorized_conversion(temperatures_f)

print(temperatures_c)


# Task 2: Custom function to calculate power
def power_function(base, exponent):
    return base ** exponent

vectorized_power = np.vectorize(power_function)

# Given arrays of numbers and their corresponding powers
bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])
results = vectorized_power(bases, exponents)

print(results)



#task3

import numpy as np

# Define the coefficient matrix A and the constant matrix B
A = np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]])
B = np.array([7, 4, 5])

# Solve the system of equations
X = np.linalg.solve(A, B)

# Print the solution
print(X)


#Task4
import numpy as np

# Define the coefficient matrix A and the constant matrix B
A = np.array([[10, -2, 3], [-2, 8, -1], [3, -1, -6]])
B = np.array([12, -5, 15])

# Solve the system of equations
I = np.linalg.solve(A, B)

# Print the solution
print(I)



