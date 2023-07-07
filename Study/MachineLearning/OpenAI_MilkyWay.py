import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a mesh grid of x, y values
x = np.arange(-10, 10, 0.1)
y = np.arange(-10, 10, 0.1)
X, Y = np.meshgrid(x, y)

# Set the z-values to the square of the distance from the center of the galaxy
Z = (X**2 + Y**2) / 100

# Plot the surface
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Add a color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

# Set the axis labels
ax.set_xlabel("Distance (light years)")
ax.set_ylabel("Distance (light years)")
ax.set_zlabel("Distance (light years)")

# Show the plot
plt.show()
