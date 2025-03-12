import numpy as np
from scipy import stats

# Heights of 20 students in centimeters
heights = [160, 165, 170, 172, 175, 176, 178, 180, 181, 182, 
           183, 185, 187, 188, 189, 190, 192, 194, 195, 200]

# Mean
mean_height = np.mean(heights)

# Median
median_height = np.median(heights)

# Mode
mode_height = stats.mode(heights)[0][0]

# Mean Deviation
mean_deviation = np.mean(np.abs(np.array(heights) - mean_height))

# Standard Deviation
std_deviation = np.std(heights)

# Variance
variance = np.var(heights)

# Karl Pearson’s coefficient of skewness
skewness = stats.skew(heights)

# Output
print("Mean Height:", mean_height)
print("Median Height:", median_height)
print("Mode Height:", mode_height)
print("Mean Deviation:", mean_deviation)
print("Standard Deviation:", std_deviation)
print("Variance:", variance)
print("Skewness:", skewness)
