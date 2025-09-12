import os
import time
import shutil
import pycutest
import numpy as np
from scipy.optimize import minimize, NonlinearConstraint, Bounds

class solver:
    def __init__(self, name):
        #store the problem inforation in p
        self.p = pycutest.import_problem(name)
        self.name = name
        #initial guess from the cutest
        self.x0 = self.p.x0
        self.pbounds = list(zip(self.p.bl, self.p.bu))
    
    #store the function and gradient/jacobian required for solve methods
    def fun(self, x):
        return self.p.obj(x)
    
    def jac(self, x):
        return self.p.obj(x, gradient=True)[1]
    
    def simple_bounds(self, method):
        #start timer so it has full function scope
        start = time.perf_counter()
        
        #this is called every callback by the solver so every set amount of iterations to check time
        def timeout(xk):
            if time.perf_counter() - start > 80:
                raise TimeoutError
        
        try:
            #start the timer again so it is more accurate
            start = time.perf_counter()
            #this is the set amount of iterations for all methods
            #ask about this
            default_opts = dict(maxiter=40_000)
            if method == "Powell" or method == "Nelder-Mead":
                res = minimize(self.fun, self.x0, method=method, bounds=self.pbounds, callback=timeout, options=default_opts)
            elif method == "TNC":
                #TNC takes Conjugate-Gradient iterations instead of just iterations
                default_opts = dict(maxCGit=40_000)
                res = minimize(self.fun, self.x0, jac=self.jac, method=method, bounds=self.pbounds, callback=timeout, options=default_opts)
            else:
                res = minimize(self.fun, self.x0, jac=self.jac, method=method, bounds=self.pbounds, callback=timeout, options=default_opts)

            #timer doesnt start at 0 so subtract it out
            total = time.perf_counter() - start
            print("Method: " + method)
            print("Problem: " + str(self.name))
            print(f"Time: {total:.2f}")
            print(f"Success: {res.success}")
            
            #get the hessian of the objective function at the resulting point
            H = self.p.hess(res.x) 

            #bounds for each variable in a list
            lower_bounds_list = []
            upper_bounds_list = []
            for bound in self.pbounds:
                lb = bound[0]
                ub = bound[1]
                lower_bounds_list.append(float(lb))
                upper_bounds_list.append(float(ub))

            #numpy arrays needed for linear algebra functions
            lower_bounds = np.array(lower_bounds_list, dtype=float)
            upper_bounds = np.array(upper_bounds_list, dtype=float)


            #at_upper and at_lower store booleans and is true if a variable is at the bound with a tolerance 1e-8
            at_lower = np.isclose(res.x, lower_bounds, atol=1e-8)
            at_upper = np.isclose(res.x, upper_bounds, atol=1e-8)
            
            #gets all the variables at the bounds in a boolean mask (similar to a list)
            variable_at_bound = at_lower | at_upper
            #this gives indices of free variables which is used for the reduced hessian eigenvalues
            #[0] because where returns a tuple and we only care about the first one
            free_indices = np.where(np.logical_not(variable_at_bound))[0]

            #H_red is the reduced hessian after free indices have been 
            H_red = H[np.ix_(free_indices, free_indices)]
            #Hessian is supposed to be symetric by definition
            #take the average of the estimate with the transpose to get closer to symetries
            H_red = 0.5 * (H_red + H_red.T)
            #get the smallest eigenvalue - returns in ascending order so [0] is the smallest
            eigenvalue = np.linalg.eigvalsh(H_red)[0]

            #use the minimum eigen value to determine the convexity of the solution
            if eigenvalue >= -1e-6:
                convex_flag = 1
            else:
                convex_flag = 0
                
            print(f"Convexity: {convex_flag}  (Smallest eigenvalue:{eigenvalue:.3e})\n")
            
            if res.success:
                return [1, total, convex_flag] 
            else:
                return [0, total, convex_flag]
        
        except TimeoutError:
            #catch all the methods that go over the 80s limit
            total = time.perf_counter() - start
            print("Method: " + method)
            print("Problem: " + str(self.name))
            print(f"Time: {total:.2f}")
            print(f"Success: Timeout\n")
            return [0, total, None]
        
        except Exception as e:
            #catch any errors 
            total = time.perf_counter() - start
            print("Method: " + method)
            print("Problem: " + str(self.name))
            print(f"Time: {total:.2f}")
            print(f"Error: {e}\n")
            return [0, total, None]
        
    ''' 
    def complex_bounds(self, method):
        start = time.perf_counter()
        
        def timeout(xk):
            if time.perf_counter() - start > 80:
                raise TimeoutError
            
        try:
            #needed for trust-constr
            bounds = Bounds(np.asarray(self.p.bl), np.asarray(self.p.bu))
            #this whole next block is for constraint functions
            def cons_func(x):
                return self.p.cons(x)
            
            def cons_jac(x):
                return self.p.cons(x, gradient=True)[1]
            
            #scipy classes anything other than closed bounds as nonlinear
            nonlinear_cons = NonlinearConstraint(fun=cons_func, lb=self.p.cl, ub=self.p.cu, jac=cons_jac)
            cons = [nonlinear_cons]
            
            #start timer
            start = time.perf_counter()
            res = minimize(self.fun, self.x0, jac=self.jac, method=method, bounds=bounds, constraints=cons)
            #timer doesnt start at 0 so subtract it out
            total = time.perf_counter() - start
            print("Method: " + method)
            print("Problem: " + str(self.name))
            print(f"Time: {total:.2f}")
            print(f"Success: {res.success}\n")
            
            H = self.p.hess(res.x) 

            #bounds for each variable in a list
            lower_bounds_list = []
            upper_bounds_list = []
            for bound in self.pbounds:
                lb = bound[0]
                ub = bound[1]
                lower_bounds_list.append(float(lb))
                upper_bounds_list.append(float(ub))

            #numpy arrays needed for linear algebra functions
            lower_bounds = np.array(lower_bounds_list, dtype=float)
            upper_bounds = np.array(upper_bounds_list, dtype=float)


            #at_upper and at_lower store booleans and is true if a variable is at the bound with a tolerance 1e-8
            at_lower = np.isclose(res.x, lower_bounds, atol=1e-8)
            at_upper = np.isclose(res.x, upper_bounds, atol=1e-8)
            
            #gets all the variables at the bounds in a boolean mask (similar to a list)
            variable_at_bound = at_lower | at_upper
            #this gives indices of free variables which is used for the reduced hessian eigenvalues
            #[0] because where returns a tuple and we only care about the first one
            free_indices = np.where(np.logical_not(variable_at_bound))[0]

            #H_red is the reduced hessian after free indices have been 
            H_red = H[np.ix_(free_indices, free_indices)]
            #Hessian is supposed to be symetric by definition
            #take the average of the estimate with the transpose to get closer to symetries
            H_red = 0.5 * (H_red + H_red.T)
            #get the smallest eigenvalue - returns in ascending order so [0] is the smallest
            eigenvalue = np.linalg.eigvalsh(H_red)[0]

            #use the minimum eigen value to determine the convexity of the solution
            if eigenvalue >= -1e-6:
                convex_flag = 1
            else:
                convex_flag = 0
            
            if res.success:
                return [1, total, convex_flag] 
            else:
                return [0, total, convex_flag] 
    
        except TimeoutError:
            #catch all the methods that go over the 80s limit
            total = time.perf_counter() - start
            print("Method: " + method)
            print("Problem: " + str(self.name))
            print(f"Time: {total:.2f}")
            print(f"Success: Timeout\n")
            return [0, total, None]
        
        except Exception as e:
            #catch any errors 
            total = time.perf_counter() - start
            print("Method: " + method)
            print("Problem: " + str(self.name))
            print(f"Time: {total:.2f}")
            print(f"Error: {e}\n")
            return [0, total, None]
    '''
        
    def unbounded(self, method):
        #start timer so it has full function scope
        start = time.perf_counter()
        
        #this is called every callback by the solver so every set amount of iterations to check time
        def timeout(xk):
            if time.perf_counter() - start > 80:
                raise TimeoutError
            
        def hess(x):
            return self.p.hess(x)
        
        def hessp(x, p):
            return self.p.hprod(x, p)
        
        try:
            #start the timer again so it is more accurate
            start = time.perf_counter()
            #this is the set amount of iterations for all methods
            #ask about this
            default_opts = dict(maxiter=40_000)
            if method == "trust-ncg":
                res = minimize(self.fun, self.x0, jac=self.jac, hessp=hessp, method=method, callback=timeout, options=default_opts)
            elif method == "dogleg":
                res = minimize(self.fun, self.x0, jac=self.jac, hess=hess, method=method, callback=timeout, options=default_opts)
            else:
                res = minimize(self.fun, self.x0, jac=self.jac, method=method, callback=timeout, options=default_opts)

            
            #timer doesnt start at 0 so subtract it out
            total = time.perf_counter() - start
            print("Method: " + method)
            print("Problem: " + str(self.name))
            print(f"Time: {total:.2f}")
            print(f"Success: {res.success}")
            
            
            n = res.x.size
            print(f"n = {n}, f(x) = {res.fun:.3e}")

            H = self.p.hess(res.x)
            if not np.isfinite(H).all():
                print("Hessian contains inf/NaN skipping convexity check.\n")
                if res.success:
                    return [1, total, None]
                else:
                    return [0, total, None]


            #Hessian is an estimate so symmetrize it like its supposed to be
            H = 0.5 * (H + H.T)

            #Smallest eigenvalue (eigvalsh assumes symmetric input; returns sorted)
            eigenvalue = np.linalg.eigvalsh(H)[0]

            #use the minimum eigen value to determine the convexity of the solution
            if eigenvalue >= -1e-6:
                convex_flag = 1
            else:
                convex_flag = 0
                
            print(f"Convexity: {convex_flag}  (Smallest eigenvalue:{eigenvalue:.3e})\n")
            
            if res.success:
                return [1, total, convex_flag] 
            else:
                return [0, total, convex_flag]
        
        except TimeoutError:
            #catch all the methods that go over the 80s limit
            total = time.perf_counter() - start
            print("Method: " + method)
            print("Problem: " + str(self.name))
            print(f"Time: {total:.2f}")
            print(f"Success: Timeout\n")
            return [0, total, None]
        
        except Exception as e:
            #catch any errors 
            total = time.perf_counter() - start
            print("Method: " + method)
            print("Problem: " + str(self.name))
            print(f"Time: {total:.2f}")
            print(f"Error: {e}\n")
            return [0, total, None]    
    
def clearcache():
    cache = os.path.expanduser("~/.pycutest_cache")
    shutil.rmtree(cache, ignore_errors=True)
    os.makedirs(cache, exist_ok=True)