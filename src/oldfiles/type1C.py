import pycutest
from solvers import solver, clearcache

#methods are L-BFGS-B, TNC, Powell, Nelder-Mead
    
def type1C():
    #dont want times to be affected by previous results
    clearcache()
    
    #get problems from pycutest
    simple_constraints = pycutest.find_problems(constraints='bound')
    print(f"Simple Constraints problems: {len(simple_constraints)}\n" )
    
    #this is a list of problem names that have already been solved
    alreadysolvedproblems = []
    with open("./checkpointfiles/type1constraints.csv") as f:
        for line in f:
            parts = line.strip().split(",")
            alreadysolvedproblems.append(parts[0])
    
    
    #methods L-BFG-B, TNC, Powell, Nelder-Mead
    Llist = []
    Tlist = []
    Plist = []
    Nlist = []
    
    #problem names keeps track of the problems solved
    #counter countes to 2 to stop the loop
    problemNames = []
    counter = 0
    for i in simple_constraints:
        if i not in alreadysolvedproblems:
            a = solver(i)
            problemNames.append(i)
            Llist.append(a.simple_bounds("L-BFGS-B"))
            clearcache()
            Tlist.append(a.simple_bounds("TNC"))
            clearcache()
            Plist.append(a.simple_bounds("Powell"))
            clearcache()
            Nlist.append(a.simple_bounds("Nelder-Mead"))
            counter += 1
        #only want 2 probs for each run
        if counter == 2:
            break
        
    #next huge block of code writes information to the csv
    with open("./checkpointfiles/type1constraints.csv", "a") as f:
        counter = 0
        for i in Llist:
            p = pycutest.import_problem(problemNames[counter])
            f.write(f"{problemNames[counter]},L-BFGS-B,{i[0]},{i[1]},{i[2]},{p.n},{i[3]}\n")
            counter += 1
                
        counter = 0
        for i in Tlist:
            p = pycutest.import_problem(problemNames[counter])
            f.write(f"{problemNames[counter]},TNC,{i[0]},{i[1]},{i[2]},{p.n},{i[3]}\n")
            counter += 1
            
        counter = 0
        for i in Plist:
            p = pycutest.import_problem(problemNames[counter])
            f.write(f"{problemNames[counter]},Powell,{i[0]},{i[1]},{i[2]},{p.n},{i[3]}\n")
            counter += 1 
        
        counter = 0
        for i in Nlist:
            p = pycutest.import_problem(problemNames[counter])
            f.write(f"{problemNames[counter]},Nelder-Mead,{i[0]},{i[1]},{i[2]},{p.n},{i[3]}\n")
            counter += 1
    