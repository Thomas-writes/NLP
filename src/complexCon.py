import matplotlib.pyplot as plt
import pycutest
import numpy as np
from solvers import solver, clearcache

#methods trust-constr, SLSQP, COBYLA
def main():
    clearcache()
    
    complex_constraints = pycutest.find_problems(constraints=['linear', 'quadratic', 'adjacency', 'other'])
    print("Complex Constraints problems: " + str(len(complex_constraints)))
    
    alreadysolvedproblems = []
    with open("./checkpointfiles/type2constraints.csv") as f:
        for line in f:
            parts = line.strip().split(",")
            alreadysolvedproblems.append(parts[0])
    
    Tlist = []
    Slist = []
    Clist = []
    
    #problem names keeps track of the problems solved
    #counter countes to 3 to stop the loop
    problemNames = []
    counter = 0
    for i in complex_constraints:
        if i not in alreadysolvedproblems:
            a = solver(i)
            problemNames.append(i)
            Tlist.append(a.complex_bounds("trust-constr"))
            clearcache()
            Slist.append(a.complex_bounds("SLSQP"))
            clearcache()
            Clist.append(a.complex_bounds("COBYLA"))
            counter += 1
        #only want 3 probs for each run
        if counter == 2:
            break
    
    counter = 0
    with open("./checkpointfiles/type2constraints.csv", "a") as f:
        counter = 0
        for i in Tlist:
            p = pycutest.import_problem(problemNames[counter])
            f.write(f"{problemNames[counter]},trust-constr,{i[0]},{i[1]},{i[2]},{p.n},\n")
            counter += 1
                
        counter = 0
        for i in Slist:
            p = pycutest.import_problem(problemNames[counter])
            f.write(f"{problemNames[counter]},SLSQP,{i[0]},{i[1]},{i[2]},{p.n},\n")
            counter += 1
            
        counter = 0
        for i in Clist:
            p = pycutest.import_problem(problemNames[counter])
            f.write(f"{problemNames[counter]},COBYLA,{i[0]},{i[1]},{i[2]},{p.n},\n")
            counter += 1 
    
main()