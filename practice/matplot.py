import numpy as np
import matplotlib.pyplot as plt

# compute x and y coordinates for points on a sine curve
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

# Plot the points using matplotlib
plt.plot( x,y_sin)
plt.plot( x, y_cos)
plt.xlabel('x axis')
plt.ylabel('amplitude')

plt.title('Sine and Cosine')
plt.legend(['Sine','Cosine'])
plt.show()

