import pycutest
import time

def main():
    problems = pycutest.find_problems()
    print("Total problems: " + str(len(problems)))
    
    bounded = pycutest.find_problems(constraints='bound')
    print("Bounded problems: " + str(len(bounded)))
    
    constrained = pycutest.find_problems(constraints='linear''quadratic''adjacency''other')
    print("Constrained problems: " + str(len(constrained)))
    
    unconstrained = pycutest.find_problems(constraints='unconstrained')
    print("Unconstrained problems: " + str(len(unconstrained)))
    
    #for bounded problems the methods L-BFG-B, TNC, Powell, Nelder-Mead
    def solveWithLBFGB(name):
        #store the problem inforation in p
        p = pycutest.import_problem(name)
        
        #store the function and gradient/jacobian
        def fun(x):
            return p.obj(x)
        
        def grad(x):
            return p.obj(x, gradient=True)[1]
    
    #for constrained problems the methods trust-constr, SLSQP, COBYLA, COBYQA
    
    #for unconstrained problems the methods CG, BFGS, Newton-CG, dogleg, trust-ncg, trust-krylov, trust-exact


main()
