import numpy
import matplotlib.pyplot as plt

# Normal plot
data_set = numpy.random.uniform(5.0, 1.0, 10000)
plt.hist(data_set, 100)
plt.show()

# Scatter plot
x = numpy.random.uniform(1, 10, 100)
y = numpy.random.uniform(1, 10, 100)
plt.scatter(x, y)
plt.show()
