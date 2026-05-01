#include <iostream>
#include <fstream>
#include <cmath>

int main() {
    const double G = 6.67430e-11;
    const double M = 5.972e24;

    double x = 7000000.0;
    double y = 0.0;

    double vx = 0.0;
    double vy = 7500.0;

    double dt = 1.0;

    std::ofstream file("trajectory.txt");

    for (int i = 0; i < 8000; i++) {
        double r = sqrt(x*x + y*y);

        double ax = -G * M * x / (r*r*r);
        double ay = -G * M * y / (r*r*r);

        vx += ax * dt;
        vy += ay * dt;

        x += vx * dt;
        y += vy * dt;

        double v = sqrt(vx*vx + vy*vy);

        // energy per unit mass
        double E = (v*v)/2.0 - (G*M)/r;

        file << x << " " << y << " " << E << std::endl;
    }

    file.close();

    std::cout << "Simulation complete (C++)" << std::endl;
    return 0;
}



