import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

h = 1.0545718e-27 # h bar in erg s
mn = 1.67492749804e-24 # mass of neutron in grams
G = 6.67430e-8 # Gravitational constant in cm^3 g^-1 s^-2
c = 3e10 # Speed of light in cm/s
R_0 = G * 2e33/ c**2 # Schwarzschild radius in cm
alpha = R_0 * 3 # Unit is 1/km
K = 1/3 # Value of K
gamma = 1 # gamma 
epsilon0 = 1.6e38 #V alue of epsilon0 in erg cm^-3 
K_bar = K * epsilon0**(gamma - 1) # Dimensionless K
beta = 4 * np.pi * epsilon0 / (2e33 * c**2 * K_bar**(1/gamma)) # Value of beta in cm^-3 
alpha, beta, epsilon0 = alpha/1e5, beta * 1e15, epsilon0 * 1e15 /(2e33 * c**2) # Converting all to units of solar masses and km as in the paper
B = 160**4 * 2.055e26 * 1e15/ (2e33 * c**2 * epsilon0)
print(160**4)
m_s = 90
u = 400
x = u**2 * m_s**2
x = x * 2.055e26 * 1e15/ (2e33 * c**2 * epsilon0)

def equations2(r, y): # Just the equations
    m, P_bar = y
    dm_dr = beta * r**2 * (P_bar + (4/3)*B + 3 * (x / (2 * np.pi**2)))**(1/gamma)
    dP_dr = - alpha * (P_bar + (4/3)*B + 3 * (x / (2 * np.pi**2)))**(1/gamma) * m / r**2
    return [dm_dr, dP_dr]

def event_termination(r, y):
    return y[1]  # We want to stop when pressure P (y[1]) is zero

event_termination.terminal = True
event_termination.direction = -1  # Ensure we catch zero crossing from positive to non-positive

# Initial conditions
r0 = 1e-6 # Starting radius (to avoid division by zero), in meters
r_end = 1e6 # Ending radius, in meters

m0 = 0  # Initial mass at the core, in solar masses here actually
P0 = 2.2e-2   # Initial pressure in solar mass km^-1 s^-2

atol, rtol = 1e-15, 1e-15 #Tolerances

# Solve the ODEs
solution = solve_ivp(equations2, [r0, r_end], [m0, P0], method='RK45', dense_output=True, atol=atol, rtol=rtol, events=event_termination)
print(solution)

# Extract the results
r = solution.t 
m = solution.y[0] 
P = solution.y[1]

r, m, P = r[0:-1], m[0:-1], P[0:-1]
# Plot the results
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(r, m)
plt.xlabel('Radius (km)')
plt.ylabel('Mass (Solar Mass)')
plt.title('Mass vs Radius')

plt.subplot(1, 2, 2)
plt.plot(r, P)
plt.xlabel('Radius (km)')
plt.ylabel('Pressure')
plt.yscale('log')
plt.title('Pressure vs Radius')

plt.tight_layout()
plt.show()

# Print the final mass and radius
print("Mass of the star is", m[-1], "solar masses")
print("Radius of the star is", r[-1], "km")
