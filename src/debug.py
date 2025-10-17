import pycutest
from scipy.optimize import minimize

def main():
    p = None
    allLines = []
    with open("./checkpointfiles/simpleCons.csv") as f:
        for line in f:
            line = line.strip().split(",")
            p = pycutest.import_problem(line[0])
            line.append(p.n)
            for i in p.bu:
                if i > 1.e19:
                    line[2] = 0
            allLines.append(line)
    
    counter = 0
    with open("./checkpointfiles/unconstrained.csv") as f:
        for line in f:
            counter += 1
            line = line.strip().split(",")
            p = pycutest.import_problem(line[0])
            line.append(p.n)
            line[2] = 0
            allLines.append(line)
            print(counter)
    
    allLines2 = []
    with open("./checkpointfiles/complexCons.csv") as f:
        for line in f:
            counter += 1
            line = line.strip().split(",")
            p = pycutest.import_problem(line[0])
            line.append(p.n)
            for i in p.bu:
                if i > 1.e19:
                    line[2] = 0
            allLines2.append(line)
            print(counter)
    
    with open("./checkpointfiles/type2constraints.csv", "a") as f:
        for line in allLines2:
            for i in line:
                f.write(f"{i},")
            f.write("\n")
        
        
    
main()