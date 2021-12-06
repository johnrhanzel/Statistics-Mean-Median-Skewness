import numpy as np
from scipy.stats import skew

#Inputs for user using list to store the values
inputs_array = [float(i) for i in input("Enter number (Ex. 12 2 3): ").split()]
print("Your inputted data = ", inputs_array)

#Calculation for Mean
input_mean = float(np.mean(inputs_array))
print("Your Mean is: ", round(input_mean, 2))

#Calculation for Median
input_median = float(np.median(inputs_array))
print("Your Median is: ", round(input_median,2))

#Calculation for Standard Deviation
input_deviation = float(np.std(inputs_array))
print("Your Standard Deviation is: ", round(input_deviation,3))

#Calculation for Skewness
print(skew("Skewness is: ", inputs_array))
