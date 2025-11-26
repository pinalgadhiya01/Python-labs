import sympy as sp

def z_transform_unit_step():
    n, z = sp.symbols('n z')

    # unit step: u[n] = 1
    u = 1

    # Z-transform formula
    U = sp.summation(u * z**(-n), (n, 0, sp.oo))
    
    print("Z-transform of unit step u[n]:")
    print("U(z) =", U)

    # ROC: |z| > 1
    print("\nRegion of Convergence (ROC): |z| > 1")

    # Check stability
    if 1 > 1:  
        print("System is Stable")
    else:
        print("System is Unstable")

z_transform_unit_step()
