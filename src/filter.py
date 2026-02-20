#the goal of this file is to filter problems into the different difficulties to solve
#initially i will look at convex problems with <= 100 variables
import pycutest
import numpy as np
from datetime import date
from pathlib import Path
from solvers import solver

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
    counter = 0
    if p.is_eq_cons is not None:
        print(p.is_eq_cons)
        for i in p.is_eq_cons:
            if i is True:
                counter += 1  
    

        
    #check if there are no constraint equations
    if p.m == 0 and np.all(p.bl <= -1e19) and np.all(p.bu >= 1e19):
        bounds = "Type 1UC"
    elif p.m == 0:
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
        f.write(f"- **Bounds type: {bounds}** \n\n")

        f.write("## Runs\n")
        f.write("| method | success | start | f | time | iters | messages |\n")
        #: is for align left right or center
        f.write("|:------|:--------:|:------|------:|------:|------:|:------|\n")
        
def append_solves(method, bounds, filter):
    base_dir = Path("./problems")
    filter_dir = base_dir / filter
    problem_names = []
    
    dir = filter_dir / bounds
        
    for md_file in dir.glob("*.md"):
        problem_name = md_file.stem
        problem_names.append(problem_name)

    if bounds == "Type 1":
        for i in problem_names:
            a = solver(i)
            successes, start_vals, objvals, times, iters, messages = a.simple_bounds(method)
            counter = 0
            with open(f"./problems/{filter}/{bounds}/{i}.md", "a") as f:
                while counter < len(successes):
                    start_vals[counter] = np.array2string(start_vals[counter], max_line_width=10**9)
                    f.write(f"| {method} | {successes[counter]} | {start_vals[counter]} | {objvals[counter]} | {times[counter]} | {iters[counter]} | {messages[counter]} |\n")
                    counter += 1
    
    elif bounds == "Type 1UC":
        for i in problem_names:
            a = solver(i)
            successes, start_vals, objvals, times, iters, messages = a.unbounded(method)
            counter = 0
            with open(f"./problems/{filter}/{bounds}/{i}.md", "a") as f:
                while counter < len(successes):
                    start_vals[counter] = np.array2string(start_vals[counter], formatter={'float_kind': lambda x: f"{x:.3g}"}, max_line_width=10**9)
                    f.write(f"| {method} | {successes[counter]} | {start_vals[counter]} | {float(objvals[counter]):.3g} | {float(times[counter]):.3g} | {iters[counter]} | {messages[counter]} |\n")
                    counter += 1
    
    else:
        for i in problem_names:
            a = solver(i)
            successes, start_vals, objvals, times, iters, messages = a.complex_bounds(method)
            counter = 0
            with open(f"./problems/{filter}/{bounds}/{i}.md", "a") as f:
                while counter < len(successes):
                    start_vals[counter] = np.array2string(start_vals[counter], formatter={'float_kind': lambda x: f"{x:.3g}"}, max_line_width=10**9)
                    f.write(f"| {method} | {successes[counter]} | {start_vals[counter]} | {float(objvals[counter]):.3g} | {float(times[counter]):.3g} | {iters[counter]} | {messages[counter]} |\n")
                    counter += 1
    

def append_best(bounds, filter):
    base_dir = Path("./problems")
    filter_dir = base_dir / filter
    dir_path = filter_dir / bounds

    problem_names = []
    for md_file in dir_path.glob("*.md"):
        problem_names.append(md_file.stem)

    for name in problem_names:
        md_path = Path(f"./problems/{filter}/{bounds}/{name}.md")

        best_time = None
        best_iters = None
        best_obj = None

        #read and parse
        with open(md_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                #Skip down to the table in the file
                if not line.startswith("|"):
                    continue

                #Skip the first two header rows
                if "method" in line or line.startswith("|:"):
                    continue

                parts = []
                for p in line.split("|"):
                    parts.append(p.strip())

                #parts layout:
                #['', method, success, start, f, time, iters, messages]

                method = parts[1]
                success = parts[2]
                obj_str = parts[4]
                time_str = parts[5]
                iters_str = parts[6]

                obj = float(obj_str)
                time = float(time_str)
                iter = int(iters_str)

                if best_time is None or time < best_time["time"]:
                    best_time = {"method": method, "time": time, "iters": iter, "obj": obj}

                if best_iters is None or iter < best_iters["iters"]:
                    best_iters = {"method": method, "time": time, "iters": iter, "obj": obj}

                if best_obj is None or obj < best_obj["obj"]:
                    best_obj = {"method": method, "time": time, "iters": iter, "obj": obj}

        with open(md_path, "a", encoding="utf-8") as f:
            f.write("\n## Best-known results (by metric)\n")

            if best_time is None:
                f.write("\nNo successful runs found in this file.\n")
                continue

            f.write("\n### Fastest successful (time)\n")
            f.write(f"- Method: {best_time['method']}\n")
            f.write(f"- Time: {best_time['time']:.3g} s\n")
            f.write(f"- Iterations: {best_time['iters']}\n")
            f.write(f"- Objective: {best_time['obj']:.3g}\n")
            if bounds == "Type 1" or bounds == "Type 1UC":
                f.write("\n### Least Iterations (iter)\n")
                f.write(f"- Method: {best_iters['method']}\n")
                f.write(f"- Time: {best_iters['time']:.3g} s\n")
                f.write(f"- Iterations: {best_iters['iters']}\n")
                f.write(f"- Objective: {best_iters['obj']:.3g}\n")

            f.write("\n### Best Objective (f)\n")
            f.write(f"- Method: {best_obj['method']}\n")
            f.write(f"- Time: {best_obj['time']:.3g} s\n")
            f.write(f"- Iterations: {best_obj['iters']}\n")
            f.write(f"- Objective: {best_obj['obj']:.3g}\n")

        

#this filter should be working
def easy_med_filter():
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
            else:
                md_writer("medium", problem, "Nonconvex", "Quadratic")



def main():
    '''
    easy_med_filter()
    
    append_solves("L-BFGS-B", "Type 1", "easy")
    append_solves("TNC", "Type 1", "easy")
    append_solves("Powell", "Type 1", "easy")
    append_solves("Nelder-Mead", "Type 1", "easy")

    append_solves("CG", "Type 1UC", "easy")
    append_solves("BFGS", "Type 1UC", "easy")
    append_solves("dogleg", "Type 1UC", "easy")
    append_solves("trust-ncg", "Type 1UC", "easy")
    
    append_solves("trust-constr", "Type 2", "easy")
    append_solves("SLSQP", "Type 2", "easy")
    append_solves("COBYLA", "Type 2", "easy")
    '''
    append_best("Type 2", "easy")


    
    
    
main()