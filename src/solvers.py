import os
import time
import shutil
import pycutest
import traceback
import numpy as np
import numdifftools as nd
from scipy.optimize import minimize, NonlinearConstraint, Bounds
from scipy.linalg import eigvals


class solver:
    def __init__(self, name):
        #store the problem inforation in p
        self.p = pycutest.import_problem(name)
        self.name = name
        #initial guess from the cutest
        self.x0 = self.p.x0
        self.pbounds = list(zip(self.p.bl, self.p.bu))
        
    def _random_starts(self, k=3):
        rng = np.random.default_rng(None)
        bl = np.asarray(self.p.bl, dtype=float)
        bu = np.asarray(self.p.bu, dtype=float)

        starts = []
        for _ in range(k):
            #need finite values
            lo = np.where(np.isfinite(bl), bl, -10000000.0)
            hi = np.where(np.isfinite(bu), bu, 10000000.0)

            #generates a random array for each lo and hi
            x = rng.uniform(lo, hi)
            starts.append(x)
        return starts
    
    #store the function and gradient/jacobian required for solve methods
    def fun(self, x):
        return self.p.obj(x)
    
    def jac(self, x):
        return self.p.obj(x, gradient=True)[1]
    
    def simple_bounds(self, method):
        #This is a check to make my mac not crash :(
        n = self.p.n
        if n > 3000:
            print(f"Skipping {self.name}: too large for {method} (n={n})\n")
            return [None, 0.0, None]

        #start timer so it has full function scope
        start = time.perf_counter()
        
        #this is called every callback by the solver so every set amount of iterations to check time
        def timeout(xk):
            if time.perf_counter() - start > 60*20:
                raise TimeoutError

        try:
            starts = self._random_starts(k=3)
            all_success = []
            success_times = []
            convex_flags = []

            print(f"Method: {method}")
            print(f"Problem: {self.name}")

            run_id = 1
            for x0_try in starts:
                #start the timer again so it is more accurate
                start = time.perf_counter()
                print(f"\nRun {run_id}")
                run_id += 1

                if method == "Powell" or method == "Nelder-Mead":
                    res = minimize(self.fun, x0_try, method=method, bounds=self.pbounds, callback=timeout)
                elif method == "TNC":
                    #TNC takes Conjugate-Gradient 
                    res = minimize(self.fun, x0_try, jac=self.jac, method=method, bounds=self.pbounds, callback=timeout)
                else:
                    res = minimize(self.fun, x0_try, jac=self.jac, method=method, bounds=self.pbounds, callback=timeout)

                #timer doesnt start at 0 so subtract it out
                total = time.perf_counter() - start
                print(f"Starting point: {x0_try}")
                print(f"Time: {total:.2f}")
                print(f"Success: {res.success}")
                print(f"Message: {res.message}")
                
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
                if free_indices.size == 0:
                    convex_flag = None
                else:
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
                        
                    print(f"Convexity: {convex_flag}  (Smallest eigenvalue:{eigenvalue:.3e})")

                if res.success:
                    success_times.append(total)
                    all_success.append(1)
                else:
                    all_success.append(0)
                convex_flags.append(convex_flag)
                

            #average success and time (only count successful runs)
            num_successes = sum(all_success)
            if starts:
                avg_success = num_successes / len(starts)
            else:
                avg_success = 0.0
            
            if success_times:
                avg_time = float(np.mean(success_times))
            else:
                0.0
                
            #if one is nonconvex all are
            if (any(c == 0 for c in convex_flags) or any(i>=1e19 for i in self.p.bu)):
                overall_convex = 0
            elif any(c == 1 for c in convex_flags):
                overall_convex = 1
            else:
                overall_convex = None

            print(f"Avg Success Rate: {avg_success:.2f}")
            print(f"Avg Time (successful runs only): {avg_time:.2f}")
            print(f"Overall Convexity: {overall_convex}\n")

            return [1, avg_time, overall_convex]

        except TimeoutError:
            #catch all the methods that go over the 20m limit
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
        
        
    
    def complex_bounds(self, method):
        n = self.p.n
        if n > 3000:
            print(f"Skipping {self.name}: too large for {method} (n={n})\n")
            return [None, 0.0, None]

        start = time.perf_counter()
        
        def timeout(xk, state=None):
            if time.perf_counter() - start > 60*20:
                raise TimeoutError
            
        try:
            starts = self._random_starts(3)
            all_success = []
            success_times = []
            convex_flags = []
            run_id = 1
            print(f"Method: {method}")
            print(f"Problem: {self.name}")
            #needed for trust-constr
            bounds = Bounds(np.asarray(self.p.bl), np.asarray(self.p.bu), keep_feasible=True)
            #this whole next block is for constraint functions
            def cons_func(x):
                return self.p.cons(x)
            
            #the jacobians have non-finite values which causes trust-constr to error so the block of code below is prevention
            useful_jac = self.jac
            try:
                if not np.all(np.isfinite(self.jac(self.x0))):
                    useful_jac = None
            except Exception:
                useful_jac = None
                
            #scipy classes anything other than closed bounds as nonlinear
            nonlinear_cons = NonlinearConstraint(fun=cons_func, lb=self.p.cl, ub=self.p.cu)
            cons = [nonlinear_cons]
            
            #start timer
            for x0 in starts:
                start = time.perf_counter()
                if method == "trust-constr":
                    res = minimize(self.fun, x0, jac=useful_jac, method=method, bounds=bounds, constraints=cons, callback=timeout)
                elif method == "COBYLA":
                    res = minimize(self.fun, x0, method=method, constraints=cons)
                else:
                    res = minimize(self.fun, x0, jac=useful_jac, method=method, bounds=bounds, constraints=cons, callback=timeout)
                #timer doesnt start at 0 so subtract it out
                total = time.perf_counter() - start
                print(f"Run {run_id}")
                run_id += 1
                print(f"Time: {total:.2f}")
                print(f"Success: {res.success}")
                print(f"Message: {res.message}")

                if res.success:
                    success_times.append(total)
                    all_success.append(1)
                else:
                    all_success.append(0)
 
            #using numdifftools for this 
                convex_flag = None
                if res.success:
                    x = res.x
                    H = nd.Hessian(self.fun)(x)
                    #np arrays needed for calculation
                    bl = np.asarray(self.p.bl, dtype=float)
                    bu = np.asarray(self.p.bu, dtype=float)
                    tol = 1e-8
                    at_lo = np.isfinite(bl) & (x <= bl + tol)
                    at_hi = np.isfinite(bu) & (x >= bu - tol)
                    active = at_lo | at_hi
                    free = ~active

                    if np.any(free):
                        Hff = H[np.ix_(free, free)]
                        eigenvalue = np.linalg.eigvalsh(Hff).min()
                    else:
                        eigenvalue = 0.0

                    if eigenvalue >= -1e-6:
                        convex_flag = 1 
                    else:
                        convex_flag = 0
                    print(f"Convexity: {convex_flag}  (Smallest eigenvalue:{eigenvalue:.3e})\n")
                
                convex_flags.append(convex_flag)

            #use the minimum eigen value to determine the convexity of the solution
            
            num_successes = sum(all_success)
            avg_success = num_successes / len(starts) if starts else 0.0
            avg_time = float(np.mean(success_times)) if success_times else 0.0

            if any(c == 0 for c in convex_flags):
                overall_convex = 0
            elif any(c == 1 for c in convex_flags):
                overall_convex = 1
            else:
                overall_convex = None
                
            print(f"Avg Success Rate: {avg_success:.2f}")
            print(f"Avg Time (successful runs only): {avg_time:.2f}")
            print(f"Overall Convexity: {overall_convex}\n")

            return [1, avg_time, overall_convex] 
    
        except TimeoutError:
            #catch all the methods that go over the 20m limit
            total = time.perf_counter() - start
            print("Method: " + method)
            print("Problem: " + str(self.name))
            print(f"Time: {total:.2f}")
            print(f"Success: Timeout\n")
            traceback.print_exc()
            return [0, total, None]
        
        except Exception as e:
            #catch any errors 
            total = time.perf_counter() - start
            print("Method: " + method)
            print("Problem: " + str(self.name))
            print(f"Time: {total:.2f}")
            print(f"Error: {e}\n")
            traceback.print_exc()
            return [0, total, None]
    
    
        
    def unbounded(self, method):
         #This is a check to make my mac not crash :(
        n = self.p.n
        if n > 3000:
            print(f"Skipping {self.name}: too large for {method} (n={n})\n")
            return [None, 0.0, None]
        #start timer so it has full function scope
        start = time.perf_counter()
        
        #this is called every callback by the solver so every set amount of iterations to check time
        def timeout(xk):
            if time.perf_counter() - start > 20*60:
                raise TimeoutError
            
        def hess(x):
            return self.p.hess(x)
        
        def hessp(x, p):
            return self.p.hprod(x, p)
        
        try:
            #start the timer again so it is more accurate
            starts = self._random_starts(3)
            all_success = []
            success_times = []
            run_id = 1

            print("Method: " + method)
            print("Problem: " + str(self.name))
            print(f"Dimension: {self.p.n}")
            
            for x0 in starts:
                start = time.perf_counter()
                print(f"\nRun {run_id}")
                run_id += 1

                if method == "trust-ncg":
                    res = minimize(self.fun, x0, jac=self.jac, hessp=hessp, method=method, callback=timeout)
                elif method == "dogleg":
                    res = minimize(self.fun, x0, jac=self.jac, hess=hess, method=method, callback=timeout)
                else:
                    res = minimize(self.fun, x0, jac=self.jac, method=method, callback=timeout)

                
                #timer doesnt start at 0 so subtract it out
                total = time.perf_counter() - start
                print(f"Time: {total:.2f}")
                print(f"Success: {res.success}")
                print(f"Message: {res.message}")
                
                if res.success:
                    all_success.append(1)
                    success_times.append(total)
                else:
                    all_success.append(0)
            
            num_successes = sum(all_success)
            avg_success = num_successes / len(starts) if starts else 0.0
            avg_time = float(np.mean(success_times)) if success_times else 0.0

            print(f"Avg Success Rate: {avg_success:.2f}")
            print(f"Avg Time (successful runs only): {avg_time:.2f}\n")

            if num_successes > 0:
                return [1, avg_time, 0]
            else:
                return [0, avg_time, None]
        
        except TimeoutError:
            #catch all the methods that go over the 20m limit
            total = time.perf_counter() - start
            print("Method: " + method)
            print("Problem: " + str(self.name))
            print(f"Time: {total:.2f}")
            print(f"Dimension: {self.p.n}")
            print(f"Success: Timeout\n")
            return [0, total, None]
        
        except Exception as e:
            #catch any errors 
            total = time.perf_counter() - start
            print("Method: " + method)
            print("Problem: " + str(self.name))
            print(f"Time: {total:.2f}")
            print(f"Dimension: {self.p.n}")
            print(f"Error: {e}\n")
            
            return [0, total, None]    
    
    
def clearcache():
    cache = os.path.expanduser("~/.pycutest_cache")
    shutil.rmtree(cache, ignore_errors=True)
    os.makedirs(cache, exist_ok=True)