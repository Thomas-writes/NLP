import matplotlib.pyplot as plt
import pycutest
import numpy as np
from solvers import solver, clearcache

#methods are L-BFGS-B, TNC, Powell, Nelder-Mead (SLSQP not implemented yet but considering)

def annotate_bars(bars, values):
    # Loop over indices
    for i in range(len(bars)):
        bar = bars[i]
        val = values[i]
    #just copied these from online but it centers text for each bar above the bar
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() * 1.02,
            str(val),
            ha="center",
            va="bottom",
            fontsize=8
        )


def graph(Llist, Tlist, Plist, Nlist):
    def avg_for(lst):
        # each list has element runs which have success, time, and convexity
        runs = []
        for run in lst:
            runs.append(run)

        #this just sorts the results into more useful lists
        #if i want to compare more results I will need to add more
        #such as num variables or degree
        time = []
        convexity = []
        success = []
        for r in runs:
            success.append(r[0])
            time.append(r[1])
            convexity.append(r[2])

        #use the convexity calculation to sort into different convexities
        #might remap this into a function if graph needs to graph other things
        convexTime = []
        nonconvexTime = []
        failTime = []
        i = 0
        while i < len(time):
            if convexity[i] == 1 and success[i] == 1:
                convexTime.append(time[i])
            elif convexity[i] == 0 and success[i] == 1:
                nonconvexTime.append(time[i])
            else:
                failTime.append(time[i])
            i += 1

        #the block below just gets the average of times simple formulas
        convexTotal = sum(convexTime)
        nonconvexTotal = sum(nonconvexTime)
        failTotal = sum(failTime)
        if len(convexTime) > 0:
            avg_convex = (convexTotal / len(convexTime)) 
        else:
            avg_convex = 0
        if len(nonconvexTime) > 0:
            avg_nonconvex = (nonconvexTotal / len(nonconvexTime))
        else:
            avg_nonconvex = 0
        if len(failTime) > 0:
            avg_fail = (failTotal / len(failTime))
        else:
            avg_fail = 0

        #this is used for the totals that are displayed above the bars
        num_convex = len(convexTime)
        num_nonconvex = len(nonconvexTime)
        num_fail = len(failTime)

        return [avg_convex, avg_nonconvex, avg_fail, num_convex, num_nonconvex, num_fail]

    #returns the list directly above
    avgL = avg_for(Llist)
    avgT = avg_for(Tlist)
    avgP = avg_for(Plist)
    avgN = avg_for(Nlist)

    #this sorts those results into useful information for the bars
    methods = ["L-BFGS-B", "TNC", "Powell", "Nelder-Mead"]
    convex_avgs = [avgL[0], avgT[0], avgP[0], avgN[0]]
    nonconvex_avgs = [avgL[1], avgT[1], avgP[1], avgN[1]]
    fail_avgs = [avgL[2], avgT[2], avgP[2], avgN[2]]
    total_convex = [avgL[3], avgT[3], avgP[3], avgN[3]]
    total_nonconvex = [avgL[4], avgT[4], avgP[4], avgN[4]]
    total_fail = [avgL[5], avgT[5], avgP[5], avgN[5]]

    #x just is 4 evenly spaced __
    x = np.arange(4)
    width = 0.25
    #set the bar groups for each type of result
    bars1 = plt.bar(x - width, convex_avgs, width=width, label="Convex")
    bars2 = plt.bar(x, nonconvex_avgs, width=width, label="Nonconvex")
    bars3 = plt.bar(x + width, fail_avgs, width=width, label="Fails")

    plt.xticks(x, methods)
    plt.ylabel("Average Time (s)")
    plt.title("Average times by method")
    plt.legend()

    #This adds the total # to the bars
    annotate_bars(bars1, total_convex)
    annotate_bars(bars2, total_nonconvex)
    annotate_bars(bars3, total_fail)

    plt.tight_layout()
    plt.savefig("./outputimages/simple_constraints.png", dpi=300, bbox_inches="tight")
    plt.show()

    
    
def main():
    #dont want times to be affected by previous results
    clearcache()
    
    #get problems from pycutest
    simple_constraints = pycutest.find_problems(constraints='bound')
    print(f"Simple Constraints problems: {len(simple_constraints)}\n" )
    
    #full length crashes my mac 
    #temporarily making it 10 elements
    simple_constraints = simple_constraints[:3]
    
    #methods L-BFG-B, TNC, Powell, Nelder-Mead
    Llist = []
    Tlist = []
    Plist = []
    Nlist = []
    
    for i in simple_constraints:
        a = solver(i)
        Llist.append(a.simple_bounds("L-BFGS-B"))
        clearcache()
        Tlist.append(a.simple_bounds("TNC"))
        clearcache()
        Plist.append(a.simple_bounds("Powell"))
        clearcache()
        Nlist.append(a.simple_bounds("Nelder-Mead"))
    
    #call the graph function with the lists of lists from above
    graph(Llist, Tlist, Plist, Nlist)
    
main()