import numpy as np
import matplotlib.pyplot as plt

# Clean sinus curve
n = 100
x_data = np.arange(0, 4*np.pi, 0.1)
y_data = np.sin(x_data) 

plt.plot(x_data, y_data)
plt.show()

# Very noisy sinus curve 
n = 100
x_data = np.linspace(-5, 5, num=n)
y_data = 10 + 5 * np.sin(3 * x_data + 2) + 1.5 * np.random.normal(size=n)
plt.plot(x_data, y_data)
plt.show()
