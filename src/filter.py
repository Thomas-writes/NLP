#the goal of this file is to filter problems into the different difficulties to solve
#initially i will look at convex problems with <= 100 variables
import pycutest
import numpy as np
from datetime import date
from pathlib import Path

#positive semidefinite - aka convexity x^T(H)x >= 0
def psd_check(H):
    #minimal eigenvalue
    lmin = np.linalg.eigvalsh(H).min()
    if lmin >= -1e-8:
        return "convex"
    else:
        return "nonconvex"

def md_writer(filter, problem_name, convexity, degree):
    p = pycutest.import_problem(problem_name)
    counter =0
    if p.is_eq_cons is not None:
        print(p.is_eq_cons)
        for i in p.is_eq_cons:
            if i is True:
                counter += 1  
        
    if p.is_eq_cons is None:
        bounds = "Type 1UC"
    elif all(p.is_eq_cons):
        bounds = "Type 1"
    else:
        bounds = "Type 2"

    path = Path(f"./problems/{filter}/{bounds}/{problem_name}.md")
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(f"./problems/{filter}/{bounds}/{problem_name}.md", "w") as f:
        f.write(f"# {problem_name}\n\n")
        f.write("## Reproducibility\n")
        f.write("- **pycutest version:** 1.8.0\n")
        f.write("- **python:** 3.12.5\n")
        f.write("- **machine:** M3 Macbook Pro, Sequoia V15.6.1\n")
        f.write("- **tolerances:** 20 minute time limit\n\n")
        
        f.write("## General Info\n")
        try:
            f.write(f"- **Notes:** \n")
        except:
            f.write("- **Notes:** None\n")
        f.write(f"- **Last Updated:** {date.today().isoformat()}\n\n")
        
        f.write(f"## Classification\n")
        f.write(f"- **Convexity:** {convexity}\n")
        f.write(f"- **Degree:** {degree}\n")
        f.write(f"- **# of Variables (n):** {p.n}\n")
        f.write(f"- **# of Constraints (m):** {p.m}\n")
        f.write(f"- **Bounds type: {bounds}** \n")

        

#this filter should be working
def easy_filter():
    #this should filter quadratic objective functions
    small_convex = pycutest.find_problems(objective="quadratic", constraints="unconstrained bound linear")
    
    for problem in small_convex:
        try:
            p = pycutest.import_problem(problem)
        except:
            print(problem)
        if p.n <= 50:
            x0 = p.x0
            H = p.ihess(x0)
            #symmetrize for correctness - thinking about 2nd derivatives this is logical
            H = .5*(H + H.T)
            if psd_check(H) == "convex":
                md_writer("easy", problem, "Convex", "Quadratic")

            
def medium_filter():
    #quadratic objective and quadratic bounds
    #this then could have minimas on the border if a bound is parabolic
    smallq_nonconvex = pycutest.find_problems(objective="quadratic", constraints=["nonlinear"], n=[1,100000])
    filtered = []
    print(smallq_nonconvex)
    '''
    for problem in smallq_nonconvex:
        p = pycutest.import_problem(problem)
        x0 = p.x0
        H = p.ihess(x0)
        #symmetrize for correctness - thinking about 2nd derivatives this is logical
        H = .5*(H + H.T)
        if psd_check(H) == "nonconvex":
            filtered.append(problem)
    '''
            
def hard_filter():
    #any objective and any bounds
    #filter for nonconvex using PSD
    small_nonconvex = pycutest.find_problems(constraints=["bounds", "linear", "nonlinear"], n=[1,20])
    filtered = []
    print(small_nonconvex)



def main():
    easy_filter()
    
main()