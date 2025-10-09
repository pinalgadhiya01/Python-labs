import sympy as sp

n,z,w=sp.symbols('n z w', real=True)

x_n=sp.cos(w*n)

X_z=sp.summation(x_n*z**(-n),(n,0,sp.oo))

print("Z-transformation of x[n]=cos(wn) u[n]:")
sp.pprint(sp.simplify(X_z), use_unicode=True)