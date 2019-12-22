# Machine Learning is making the computer learn from studying data and statistics.
# Machine Learning is a step into the direction of artificial intelligence (AI).
# Machine Learning is a program that analyses data and learns to predict the outcome.

# Data Set
# Collection of Data

# Data Types
# Numerical
# Categorical
# Ordinal

# Numerical
# Discrete Data - numbers that are limited to integers. Example: The number of cars passing by.
# Continuous Data - numbers that are of infinite value. Example: The price of an item, or the size of an item

# Categorical
# Data are values that cannot be measured up against each other. Example: a color value, or any yes/no values.

# Ordinal
# Data are like categorical data, but can be measured up against each other. Example: school grades where A is better than B and so on.

# Mean Medium Mode
# Mean
import numpy
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.mean(speed)
print(x)

# Medium
import numpy
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = numpy.median(speed)
print(x)

# Mode
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = stats.mode(speed)
print(x)

# Standard Deviation
# Number that describes how spread out the values are.
# A low standard deviation means that most of the numbers are close to the mean (average) value.
# A high standard deviation means that the values are spread out over a wider range.
import numpy
speed = [86,87,88,86,87,85,86]
x = numpy.std(speed)
print(x)

# Variance
# Another number that indicates how spread out the values are.
# In fact, if you take the square root of the variance, you get the standard variation!
# Or the other way around, if you multiply the standard deviation by itself, you get the variance!
