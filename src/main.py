from filter import *
from writer import *
from grapher import *
from solvers import clearcache

def main():
    
    clearcache()
    filter()
    
    #Type 1: L-BFGS-B, TNC, Powell, Nelder-Mead
    '''
    append_solves("L-BFGS-B", "Type 1", "smallconvex")
    append_solves("TNC", "Type 1", "smallconvex")
    append_solves("Powell", "Type 1", "smallconvex")
    append_solves("Nelder-Mead", "Type 1", "smallconvex")
    
    append_solves("L-BFGS-B", "Type 1", "smallnonconvex")
    append_solves("TNC", "Type 1", "smallnonconvex")
    append_solves("Powell", "Type 1", "smallnonconvex")
    append_solves("Nelder-Mead", "Type 1", "smallnonconvex")
    
    append_solves("L-BFGS-B", "Type 1", "largeconvex")
    append_solves("TNC", "Type 1", "largeconvex")
    append_solves("Powell", "Type 1", "largeconvex")
    append_solves("Nelder-Mead", "Type 1", "largeconvex")
    
    append_solves("L-BFGS-B", "Type 1", "largenonconvex")
    append_solves("TNC", "Type 1", "largenonconvex")
    append_solves("Powell", "Type 1", "largenonconvex")
    append_solves("Nelder-Mead", "Type 1", "largenonconvex")
    '''
    #Type 1UC: CG, BFGS, dogleg, trust-ncg
    append_solves("CG", "Type 1UC", "smallconvex")
    append_solves("BFGS", "Type 1UC", "smallconvex")
    append_solves("dogleg", "Type 1UC", "smallconvex")
    append_solves("trust-ncg", "Type 1UC", "smallconvex")
    
    append_solves("CG", "Type 1UC", "smallnonconvex")
    append_solves("BFGS", "Type 1UC", "smallnonconvex")
    append_solves("dogleg", "Type 1UC", "smallnonconvex")
    append_solves("trust-ncg", "Type 1UC", "smallnonconvex")
    '''
    append_solves("CG", "Type 1UC", "largeconvex")
    append_solves("BFGS", "Type 1UC", "largeconvex")
    append_solves("dogleg", "Type 1UC", "largeconvex")
    append_solves("trust-ncg", "Type 1UC", "largeconvex")
    
    append_solves("CG", "Type 1UC", "largenonconvex")
    append_solves("BFGS", "Type 1UC", "largenonconvex")
    append_solves("dogleg", "Type 1UC", "largenonconvex")
    append_solves("trust-ncg", "Type 1UC", "largenonconvex")
    '''
    #Type 2: trust-constr, SLSQP, COBYLA
    '''
    append_solves("trust-constr", "Type 2", "smallconvex")
    append_solves("SLSQP", "Type 2", "smallconvex")
    append_solves("COBYLA", "Type 2", "smallconvex")
    '''
    graph("Type 1UC", "smallnonconvex")

main()