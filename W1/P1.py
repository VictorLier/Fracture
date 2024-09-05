import sympy as sp

# Define the symbols
I, b, h, M, a, E, Pi, sigma_B, delta_B, G, Gc = sp.symbols('I b h M a E Pi sigma_B delta_B G Gc')

# Moment of inertia
I = b * h**3 / 12

# From elementary beam theory
phi = M * a / (E * I)

Pi = - 1/2 * M * phi

# Energy release rate G
G = - 1/b * sp.diff(Pi, a)
print(G)

# Critical energy release rate Gc
# Gc = 1/2 * sigma_B * delta_B

M_crit = sp.solve(Gc - G, M)
print(M_crit)