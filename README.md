# 🚀 Hybrid Orbit Simulator (C++ + Python)

A hybrid physics-based simulation of satellite motion using **C++ for computation** and **Python for visualization**.

---

## 🧠 Overview

This project simulates the motion of a satellite in Earth's gravitational field using numerical integration.

It demonstrates a simple but powerful architectural idea:

- **C++** handles physics calculations (performance-critical part)
- **Python** handles visualization and analysis

---

## ⚙️ Physics Model

The simulation is based on Newtonian gravity:

F = G * (M * m) / r²

Acceleration:

a = -G * M / r³ * r_vector

Total specific orbital energy:

E = v²/2 - GM/r

---

## 📊 Features

- 2D orbital motion simulation
- Hybrid architecture (C++ + Python)
- Energy calculation at each timestep
- Orbit classification:
  - Bound (elliptical)
  - Escape trajectory
- Color-coded trajectory based on energy
- Energy vs time visualization

---

## 🎨 Visualization

- Orbit colored by energy (scientific visualization)
- Energy stability graph
- Earth-centered coordinate system

---

## 📷 Output

![Orbit](output/orbit_colored.png)
![Energy](output/energy_plot.png)

---

## 📁 Project Structure



