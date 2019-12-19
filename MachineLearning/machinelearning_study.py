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