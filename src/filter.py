'''
This file is used to filter the problems based on bounds/constraints and convexity
'''
import pycutest
from writer import md_writer
import numpy as np



#positive semidefinite - aka convexity x^T(H)x >= 0
def psd_check(H):
    #minimal eigenvalue
    lmin = np.linalg.eigvalsh(H).min()
    if lmin >= -1e-8:
        return "convex"
    else:
        return "nonconvex"


#this filter should be working
def filter():
    problems = pycutest.find_problems(constraints="unconstrained bound linear")
    
    for problem in problems:
        try:
            p = pycutest.import_problem(problem)
            props = pycutest.problem_properties(problem)
        except Exception as e:
            print(f"Skipping {problem} (import failed): {e}")
            continue
            
        try:
            x0 = p.x0
            H = p.ihess(x0)
            #symmetrize for correctness - thinking about 2nd derivatives this is logical
            H = .5*(H + H.T)
        except Exception as e: 
            print(f"Skipping {problem} (Hessian failed): {e}")
            continue
        
        objective_type = props["objective"] 

        #this is for small problems
        if p.n <= 20:
            #check the convexity using the hessian eigenvalues
            if psd_check(H) == "convex":
                md_writer("smallconvex", problem, "Convex", objective_type)
            else:
                md_writer("smallnonconvex", problem, "Nonconvex", objective_type)
        #this is for relatively large problems
        elif p.n <= 500:
            if psd_check(H) == "convex":
                md_writer("largeconvex", problem, "Convex", objective_type)
            else:
                md_writer("largenonconvex", problem, "Nonconvex", objective_type)