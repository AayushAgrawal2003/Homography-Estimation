import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the camera position (x, y, z coordinates)
camera_pos = (2, 3, 4)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the camera position as a point
ax.scatter(camera_pos[0], camera_pos[1], camera_pos[2], c='r', marker='o', label='Camera Position')

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set axis limits or adjust as needed
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
ax.set_zlim(0, 5)

# Add a legend
ax.legend()

# Show the plot
plt.show()
