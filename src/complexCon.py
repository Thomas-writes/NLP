import pycutest
from solvers import solver, clearcache

#methods trust-constr, SLSQP, COBYLA, (COBYQA, IPOPT)

def main():
    clearcache()
    
    complex_constraints = pycutest.find_problems(constraints=['linear', 'quadratic', 'adjacency', 'other'])
    print("Complex Constraints problems: " + str(len(complex_constraints)))
    '''
    counterTr = 0
    timeTr = 0
    
    for i in complex_constraints:
        a = solver(i)
        temp = a.complex_bounds("trust-constr")
        counterTr += temp[0]
        timeTr += temp[1]
    '''
main()