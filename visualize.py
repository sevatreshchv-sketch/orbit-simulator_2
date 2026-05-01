import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import LineCollection

x = []
y = []
energy = []

with open("trajectory.txt", "r") as file:
    for line in file:
        values = line.split()
        x.append(float(values[0]))
        y.append(float(values[1]))
        energy.append(float(values[2]))

x = np.array(x)
y = np.array(y)
energy = np.array(energy)

# =========================
# ORBIT TYPE
# =========================
if energy[0] < 0:
    orbit_type = "Bound Orbit (Elliptical)"
else:
    orbit_type = "Escape Orbit"

# =========================
# NORMALIZE ENERGY (for color)
# =========================
norm_energy = (energy - energy.min()) / (energy.max() - energy.min())

# =========================
# CREATE SEGMENTS
# =========================
points = np.array([x, y]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

# =========================
# CREATE COLORED LINE
# =========================
lc = LineCollection(segments, cmap='plasma')
lc.set_array(norm_energy)
lc.set_linewidth(2)

# =========================
# PLOT ORBIT
# =========================
fig, ax = plt.subplots(figsize=(6,6))

ax.add_collection(lc)
ax.scatter(0, 0, color='white', s=20)

ax.set_title(f"Orbit | {orbit_type}")
ax.set_aspect('equal')
ax.grid()

# colorbar
cbar = plt.colorbar(lc)
cbar.set_label("Normalized Energy")

plt.savefig("orbit_colored.png", dpi=300)

# =========================
# ENERGY GRAPH
# =========================
plt.figure(figsize=(6,4))
plt.plot(energy)

plt.title("Energy over time")
plt.xlabel("Step")
plt.ylabel("Energy")

plt.grid()
plt.savefig("energy_plot.png", dpi=300)

print("Visualization complete (Python)")
print("Orbit type:", orbit_type)




