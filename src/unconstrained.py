import pycutest
from solvers import solver, clearcache

#methods are CG, BFGS, dogleg, trust-ncg


def main():
    clearcache()
    
    unconstrained = pycutest.find_problems(constraints='unconstrained')
    print("Unconstrained problems: " + str(len(unconstrained)))
    
    #this is a list of problem names that have already been solved
    alreadysolvedproblems = []
    with open("./checkpointfiles/type1constraints.csv") as f:
        for line in f:
            parts = line.strip().split(",")
            alreadysolvedproblems.append(parts[0])
    
    
    
    #CG, BFGS, dogleg, trust-ncg
    Clist = []
    Blist = []
    Dlist = []
    Tlist = []
    
    #problem names keeps track of the problems solved
    #counter countes to 3 to stop the loop
    problemNames = []
    counter = 0
    for i in unconstrained:
        if i not in alreadysolvedproblems:
            a = solver(i)
            problemNames.append(i)
            Clist.append(a.unbounded("CG"))
            clearcache()
            Blist.append(a.unbounded("BFGS"))
            clearcache()
            Dlist.append(a.unbounded("dogleg"))
            clearcache()
            Tlist.append(a.unbounded("trust-ncg"))
            counter += 1
        if counter == 2:
            break
    
    #next huge block of code writes information to the csv
    counter = 0
    with open("./checkpointfiles/type1constraints.csv", "a") as f:
        counter = 0
        for i in Clist:
            p = pycutest.import_problem(problemNames[counter])
            f.write(f"{problemNames[counter]},CG,{i[0]},{i[1]},{i[2]},{p.n},\n")
            counter += 1
                
        counter = 0
        for i in Blist:
            p = pycutest.import_problem(problemNames[counter])
            f.write(f"{problemNames[counter]},BFGS,{i[0]},{i[1]},{i[2]},{p.n},\n")
            counter += 1
            
        counter = 0
        for i in Dlist:
            p = pycutest.import_problem(problemNames[counter])
            f.write(f"{problemNames[counter]},dogleg,{i[0]},{i[1]},{i[2]},{p.n},\n")
            counter += 1 
        
        counter = 0
        for i in Tlist:
            p = pycutest.import_problem(problemNames[counter])
            f.write(f"{problemNames[counter]},trust-ncg,{i[0]},{i[1]},{i[2]},{p.n},\n")
            counter += 1
    
    
main()