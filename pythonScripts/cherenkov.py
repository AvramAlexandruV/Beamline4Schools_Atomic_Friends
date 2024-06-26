import numpy as np
import matplotlib.pyplot as plt
import math
# >>>> Constants

# > speed of light
c = 299792458   # [m/s]
# > refractive index N2
n_N2 = 1.00029
# > refractive index Ar
n_Ar = 1.000281
# > refractive index He
n_He = 1.00036

me = 511E3 # [eV]
mp = 938E6 # [eV]

# >>>> Calculations
# E -> particle energy [J]
# p -> momentum [kg*m/s]
# mo -> rest mass [kg]
# c -> speed of light [m/s]
# v -> particle velocity [m/s]
# B -> velocity relative to speed of light in vacuum

def energyToMomentum(E, m):
    p = np.sqrt(E**2 - m**2)
    return p/1E9

def gamma(E, m):
    gamma = E / m
    return gamma

def beta(E, m):
    gamma = E / m
    beta = np.sqrt((gamma**2-1) / (gamma ** 2))
    return beta


# cos(theta) = 1 / (B*n)
def cherenkovAngle(m0, E, n, c):
    B = beta(m0, E, c)
    print(B)
    try:
        theta = math.acos(1 / (B * n))
        return theta
    except ValueError:
        print("Cherenkov radiation would not be observed in the given conditions")
        return -10

# >>>> Plotting

def draw_cherenkov_ring(E, m0, n, radius=10, ax=None):
    if ax is None:
        fig = plt.figure(figsize=(10, 5))
        ax = fig.add_subplot(121, projection='3d')
        ax_side = fig.add_subplot(122)

    theta = cherenkovAngle(m0, E, n, 3e8)
    
    if theta == -10 :
        return
    
    phi = np.linspace(0, 2*np.pi, 100)
    
    for r in range(0, radius + 1):
        x = r * np.sin(theta) * np.cos(phi)
        y = r * np.sin(theta) * np.sin(phi)
        z = r * np.cos(theta)

        ax.plot(x, y, z)
        ax_side.plot(x, y)

    ax.set_xlabel('X [m]')
    ax.set_ylabel('Y [m]')
    ax.set_zlabel('Z [m]')
    ax.set_title('Cherenkov Ring')

    ax_side.set_xlabel('X [m]')
    ax_side.set_ylabel('Y [m]')
    ax_side.set_aspect('equal', adjustable='box')
    ax_side.set_title('Side View')

    plt.tight_layout()
    plt.show()


def draw_cherenkov_ring_2d(E, m0, n, radius=10):
    fig, ax = plt.subplots(figsize=(8, 6))

    theta = cherenkovAngle(m0, E, n)
    phi = np.linspace(0, 2*np.pi, 100)
    
    for r in range(0, radius + 1):
        x = r * np.sin(theta) * np.cos(phi)
        y = r * np.sin(theta) * np.sin(phi)
        ax.plot(x + r, y + r)

    ax.plot([0, 2*radius], [0, 2*radius], color='black', linestyle='--')

    ax.set_aspect('equal', 'box')
    ax.set_xlabel('X [m]')
    ax.set_ylabel('Y [m]')
    ax.set_title('Cherenkov Rings')
    ax.legend()

    plt.show()

for i in range(1, 16):
    print(f"ENERGY:{i}")
    print()
    print(f"Momentum for electron: {energyToMomentum(i * 1e9,me)} GeV/c")
    print(f"Momentum for proton: {energyToMomentum(i * 1e9,mp)} GeV/c")

    print(f"gamma for electron: {gamma(i * 1e9,me)} ")
    print(f"gamma for proton: {gamma(i * 1e9,mp)}")

    print(f"beta for electron: {beta(i * 1e9,me)} GeV/c")
    print(f"beta for proton: {beta(i * 1e9,mp)} GeV/c")