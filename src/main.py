import os
import time
import shutil
import pycutest
import numpy as np
from scipy.optimize import minimize, NonlinearConstraint, BFGS, Bounds


def clearcache():
    cache = os.path.expanduser("~/.pycutest_cache")
    shutil.rmtree(cache, ignore_errors=True)
    os.makedirs(cache, exist_ok=True)
    

class solver:
    def __init__(self, name):
        #store the problem inforation in p
        self.p = pycutest.import_problem(name)
        self.name = name
        #initial guess from the cutest
        self.x0 = self.p.x0
        self.pbounds = list(zip(self.p.bl, self.p.bu))
    
    #store the function and gradient/jacobian
    def fun(self, x):
        return self.p.obj(x)
    
    def jac(self, x):
        return self.p.obj(x, gradient=True)[1]
    
    def simple_bounds(self, method):
        #start timer
        start = time.perf_counter()
        if method == "Powell" or method == "Nelder-Mead":
            res = minimize(self.fun, self.x0, method=method, bounds=self.pbounds)
        else:
            res = minimize(self.fun, self.x0, jac=self.jac, method=method, bounds=self.pbounds)
        #timer doesnt start at 0 so subtract it out
        total = time.perf_counter() - start
        print("Problem: " + str(self.name))
        print("Time: " + f"{total:.6f}")
        if res.success:
            return [1, total] 
        else:
            return [0, total]
        
        
    def complex_bounds(self, method):
        try:
            #needed for trust-constr
            bounds = Bounds(np.asarray(self.p.bl), np.asarray(self.p.bu))
            #this whole next block is for constraint functions
            def cons_func(x):
                return self.p.cons(x)
            
            def cons_jac(x):
                return self.p.cons(x, gradient=True)[1]
            
            #scipy classes anything other than bounds as nonlinear
            nonlinear_cons = NonlinearConstraint(fun=cons_func, lb=self.p.cl, ub=self.p.cu, jac=cons_jac)
            cons = [nonlinear_cons]
            
            #start timer
            start = time.perf_counter()
            res = minimize(self.fun, self.x0, jac=self.jac, method=method, bounds=bounds, constraints=cons)
            #timer doesnt start at 0 so subtract it out
            total = time.perf_counter() - start
            print("Problem: " + str(self.name))
            print("Time: " + f"{total:.6f}")
            
            if res.success:
                return [1, total] 
            else:
                return [0, total]
        except:
            print("Something went wrong")
            return [0, 0]
    
    
def print_statement(method, counter, time, problemN):
    print("Number of successes (" + method + f"): {counter}")
    print(f"Success rate: {counter/problemN}")
    print(f"Average time: {time/problemN}")
    

def main():
    clearcache()
    problems = pycutest.find_problems()
    print("Total problems: " + str(len(problems)))
    
    simple_constraints = pycutest.find_problems(constraints='bound')
    print("Simple Constraints problems: " + str(len(simple_constraints)))
    
    complex_constraints = pycutest.find_problems(constraints=['linear', 'quadratic', 'adjacency', 'other'])
    print("Complex Constraints problems: " + str(len(complex_constraints)))
    
    unconstrained = pycutest.find_problems(constraints='unconstrained')
    print("Unconstrained problems: " + str(len(unconstrained)))
    
    #full length crashes my mac 
    #temporarily making it 10 elements
    simple_constraints = simple_constraints[:10]
    complex_constraints = complex_constraints[:10]
    
    #for simple constraints problems the methods L-BFG-B, TNC, Powell, Nelder-Mead
    counterL = 0
    timeL = 0
    counterT = 0
    timeT = 0
    counterP = 0
    timeP = 0
    counterN = 0
    timeN = 0
    
    for i in simple_constraints:
        a = solver(i)
        temp = a.simple_bounds("L-BFGS-B")
        counterL += temp[0]
        timeL += temp[1]
        clearcache()
        temp = a.simple_bounds("TNC")
        counterT += temp[0]
        timeT += temp[1]
        clearcache()
        temp = a.simple_bounds("Powell")
        counterP += temp[0]
        timeP += temp[1]
        clearcache()
        temp = a.simple_bounds("Nelder-Mead")
        counterN += temp[0]
        timeN += temp[1]
    
    #success rate is incorrect because I dont have global mins or maxs to check yet
    #looking at using shgo for global mins and maxs 
    print_statement("L-BFGS-B", counterL, timeL, len(simple_constraints))
    print_statement("TNC", counterT, timeT, len(simple_constraints))
    print_statement("Powell", counterP, timeP, len(simple_constraints))
    print_statement("Nelder-Mead", counterN, timeN, len(simple_constraints))
    
    #for constrained problems the methods trust-constr, SLSQP, COBYLA, COBYQA
    counterTr = 0
    timeTr = 0
    
    for i in complex_constraints:
        a = solver(i)
        temp = a.complex_bounds("trust-constr")
        counterTr += temp[0]
        timeTr += temp[1]
        
    print_statement("trust-constr", counterTr, timeTr, len(complex_constraints))
    
    #for unconstrained problems the methods CG, BFGS, Newton-CG, dogleg, trust-ncg, trust-krylov, trust-exact


main()
