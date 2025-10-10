import pycutest
from scipy.optimize import minimize

def main():
    p = None
    nonConvex = []
    with open("./checkpointfiles/simpleCons.csv") as f:
        for line in f:
            line = line.strip().split(",")
            if line[0] not in nonConvex and int(line[2]) == 0:
                nonConvex.append(line[0])
    
    def fun(x):
        return p.obj(x)
    
    def jac(x):
        return p.obj(x, gradient=True)[1]
    
    counter = 0
    with open("./debug.txt", "a") as f:
        for i in nonConvex:
            p = pycutest.import_problem(i)
            f.write(f"Problem name: {i}\n")
            f.write(f"Number of variables: {p.n}\n")
            f.write(f"Number of constraints: {p.m}\n")
            f.write(f"Upper Objective Bound: {p.bu}\n")
            f.write(f"Lower Objective Bound: {p.bl}\n")
            f.write(f"Initial guess: {p.x0}\n")
            f.write(f"Objective Value (initial guess): {p.obj(p.x0)}\n")
            f.write(f"Gradient (initial guess): {p.grad(p.x0)}\n")
            f.write(f"Hessian (initial guess): {p.hess(p.x0)}\n")
            bounds = list(zip(p.bl, p.bu))
            res = minimize(fun, p.x0, method="L-BFGS-B", bounds=bounds, jac=jac)
            f.write(f"Solution: {res.x}\n")
            f.write(f"Solver Message: {res.message}\n")
            f.write("\n\n\n\n\n\n\n")

            counter += 1
            if counter > 5:
                break
            
        
        
    
main()