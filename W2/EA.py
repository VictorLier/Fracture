import sympy as sp

# Material properties
name = ["Steel 1940", "Steel 1970", "Steel 2000", "Silicon carbide", "Aluminium"]
K_IC_l = [100, 120, 150, 3, 40]         # M * N / M^(3/2)
sigma_l = [300, 600, 2000, 10e4, 300]   # M * Pa

# Saftey factor
S = 1.25

# Stress intensity factor
K, a, sigma, K_IC = sp.symbols('K a sigma K_IC')
K = sigma * S * sp.sqrt(sp.pi * a)

# Solve for crack length
eq = K - K_IC
a = sp.solve(eq, a)[0]

crack_length = []
for i, mat in enumerate(name):
    crack_length.append(2 * a.subs({K_IC: K_IC_l[i], sigma: sigma_l[i]}))
    print(f"Crack length for {mat}: {crack_length[i]:.3g} m")