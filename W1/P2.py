import sympy as sp

# Define the symbols
delta, F, a, b, x, E, I, Pi, h = sp.symbols('delta F a b x E I Pi h')

# Moment of inertia
I = b * h**3 / 12

# From elementary beam theory
delta = F * a * b * a**3 / (24 * E * I) * ((x/a)**4 - 4 * (x/a) + 3)

# Potential energy
# Pi = U + W = 1/2 * W
Pi = 1/2 * (2 * sp.integrate(-F*delta*b, (x, 0, a)))
print(Pi)

# Energy release rate G
G = - 1/b * sp.diff(Pi, a)
print(G)