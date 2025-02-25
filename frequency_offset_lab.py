import numpy as np
import matplotlib.pyplot as plt

# Define inner and outer radii
r1 = 1.4142  # Inner radius
r2 = 3.8637  # Outer radius

# Define phase for outer and inner points
theta_outer = np.linspace(np.pi / 12, 2 * np.pi - np.pi / 12, 12)  # Uniform phase distribution for outer points
theta_inner = np.linspace(np.pi / 4, 2 * np.pi - np.pi / 4, 4)  # Uniform phase distribution for inner points

# Calculate the x and y coordinates for inner and outer points
inner_x = r1 * np.cos(theta_inner)
inner_y = r1 * np.sin(theta_inner)

outer_x = r2 * np.cos(theta_outer)
outer_y = r2 * np.sin(theta_outer)

# Combine the inner and outer coordinates
x = np.concatenate([inner_x, outer_x])
y = np.concatenate([inner_y, outer_y])

# Simulate frequency and phase offset by adding 50 random points around each constellation point
num_noise_points = 50  # Number of points around each constellation point
noise_std = 0.1  # Standard deviation for the noise (simulating the offsets)

# Generate noise around each constellation point
noisy_x = []
noisy_y = []

for i in range(len(x)):
    # Generate random noise for frequency and phase offset (uniformly distributed in a small range)
    noise_x = np.random.normal(loc=x[i], scale=noise_std, size=num_noise_points)
    noise_y = np.random.normal(loc=y[i], scale=noise_std, size=num_noise_points)

    noisy_x.extend(noise_x)
    noisy_y.extend(noise_y)

# Plot the constellation diagram with the noisy points
plt.figure(figsize=(6, 6))
plt.scatter(noisy_x, noisy_y, color='blue', s=5, label='Noisy Points')
plt.scatter(x, y, color='black', zorder=5, label='Constellation Points')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('In-phase (I)')
plt.ylabel('Quadrature-phase (Q)')
plt.title('16-APSK Constellation Diagram with Frequency Offsets')
plt.legend()

# 保存图表到文件
plt.savefig('img/Frequency_Offset_Lab.png')

plt.show()
