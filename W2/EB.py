import sympy as sp

# A - Stress concentration for a equibiaxial stress
# Symbols
Phi, sigma, a, r, theta = sp.symbols('Phi sigma a r theta')

# Airy stress function
Phi = sigma * (r**2 / 2 - a**2 * sp.ln(r))

sigma_rr = sp.diff(Phi, r) / r + sp.diff(Phi, theta, theta) / r**2
sigma_tt = sp.diff(Phi, r, r)
sigma_rt = -sp.diff( sp.diff(Phi, theta) / r, r)

sigma_l = [sigma_rr, sigma_tt, sigma_rt]

# Max stress at the hole periphery
name = ["radial", "tangential", "shear"]
for i, name in enumerate(name):
    print(f"Max {name} stress at the hole periphery: {sigma_l[i].subs(r, a)}")
