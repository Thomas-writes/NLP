'''
This file is used to graph the cdf of each method based on time to solve
and number of problems solved
'''
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from collections import defaultdict

def collect_times(bounds, filter):
    #get the correct directory based on the bounds and the filter
    base_dir = Path("./problems")
    dir_path = base_dir / filter / bounds

    #makes it so i can append to the dictionary directly instead of doing checks
    method_problem_times = defaultdict(list)

    #pull all markdown files that are holding the problems and solves
    for md_file in dir_path.glob("*.md"):
        md_path = md_file

        #use a dictionary with empty lists to track runs per method
        runs_per_method = defaultdict(list)

        #open the markdown file
        with open(md_path, "r", encoding="utf-8") as f:
            for line in f:
                #iterate throught the lines of the file but skip the unimportant ones
                line = line.strip()

                if not line.startswith("|"):
                    continue
                if "method" in line or line.startswith("|:"):
                    continue
                #this is to append the different segments to parts
                #| method | success | start | f | time | iters | messages |
                #^Thats the format used for the lines below
                parts = []
                for p in line.split("|"):
                    parts.append(p.strip())
                    
                method = parts[1]
                success = parts[2]
                time_str = parts[5]

                #Currently ignoring failed runs
                if success != "success":
                    continue
                
                #get the time as a float
                time = float(time_str)
                #add the time to the the list corresponding to that method
                runs_per_method[method].append(time)

        #Since we have multiple runs with different times on the same problem
        #Use the median time to show the problem
        for method, times in runs_per_method.items():
            if len(times) == 0:
                continue

            rep_time = np.median(times)
            method_problem_times[method].append(rep_time)
    #return a dictionary with {"method", [median times]}
    return method_problem_times


def plot_cdf_counts(times, label):
    times = np.sort(times)

    # prepend 0 to both axes
    x = np.concatenate(([0], times))
    y = np.arange(0, len(times) + 1)

    plt.step(x, y, where="post", label=label)

    
def graph(bounds, filter):
    base_dir = Path("./problems")
    dir_path = base_dir / filter / bounds
    
    num_problems = len(list(dir_path.glob("*.md")))

    data = collect_times(bounds, filter)

    plt.figure()

    
    for method, times in data.items():
        plot_cdf_counts(times, method)

    plt.axhline(y=num_problems, linestyle='dotted', color='gray', alpha=0.7)
    plt.xlabel("Time (s)")
    plt.ylabel("# Problems Solved")
    plt.title("Cumulative Problems Solved vs Time")
    plt.xscale("log") 
    plt.legend()
    plt.grid(True)
    plt.savefig(f"./problems/{filter}/{bounds}/.pvt.png")
    plt.show()