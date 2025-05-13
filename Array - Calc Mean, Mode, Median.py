# Calculate Mean, Mode and Median Given an Array

import numpy



Numbers = [10,15, 23, 45, 50, 971]; n = len(Numbers); avg = 0; sum = 0

for i in Numbers:
    sum += i

avg = sum / n

print(f"The Average of given array is: {avg:.2f}")

# Using numpy
print(f"Using Numpy to do the work for me: {numpy.mean(Numbers):.2f}.")



#Numbers
