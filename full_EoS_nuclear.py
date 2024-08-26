import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

h = 1.0545718e-27 # h bar in erg s
mn = 1.67492749804e-24 # mass of neutron in grams
G = 6.67430e-8 # Gravitational constant in cm^3 g^-1 s^-2
c = 2.99792458e10 # Speed of light in cm/s
R_0 = G * 2e33/ c**2 # Schwarzschild radius in cm
alpha = R_0 # Unit is 1/km
epsilon0 = mn**4 * c**5 / (3 * np.pi**2 * h**3) #Value of epsilon0 in erg cm^-3 

beta = 4 * np.pi * epsilon0 / (2e33 * c**2) # Value of beta in cm^-3 
alpha, beta, epsilon0, R_0 = alpha/1e5, beta * 1e15, epsilon0 * 1e15 /(2e33 * c**2), R_0 / 1e5 # Converting all to units of solar masses and km as in the paper
c = c / 1e5

def equations2(r, y): # Just the equations
    m, P = y
    P_bar = P / epsilon0
    dm_dr = beta * r**2 * (2.4216 * P_bar**(3/5) + 2.8663 * P_bar)  
    dP_dr = - alpha * (2.4216 * P_bar**(3/5) + 2.8663 * P_bar) * m / r**2 * epsilon0
    
    return [dm_dr, dP_dr]

def event_termination(r, y):
    return y[1]  # We want to stop when pressure P (y[1]) is zero

event_termination.terminal = True
event_termination.direction = -1  # Ensure we catch zero crossing from positive to non-positive

# Initial conditions
r0 = 1e-6 # Starting radius (to avoid division by zero), in meters
r_end = 1e6 # Ending radius, in meters

m0 = 0  # Initial mass at the core, in solar masses here actually
P0 = 1e-4 * epsilon0  # Initial pressure in solar mass km^-1 s^-2

atol, rtol = 1e-15, 1e-15 #Tolerances

# Solve the ODEs
try:
    solution = solve_ivp(equations2, [r0, r_end], [m0, P0], method='RK45', dense_output=True, atol=atol, rtol=rtol, events=event_termination)
except ValueError:
    print("oh")
    
print(solution)

# Extract the results
r = solution.t 
m = solution.y[0] 
P = solution.y[1]
print(len(P))

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
plt.title('Pressure vs Radius')

plt.tight_layout()
plt.show()

# Print the final mass and radius
print("Mass of the star is", m[-1], "solar masses")
print("Radius of the star is", r[-1], "km")
