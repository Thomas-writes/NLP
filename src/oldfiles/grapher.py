import matplotlib.pyplot as plt
import numpy as np

def cleaner(list):
    #line1 = name 
    #line2 = success 
    #line3 = time 
    #line4 = convexity 
    #line5 = number of variables
    temp = []
    #r0 is method
    temp.append(int(list[2]))
    #r1 is success
    temp.append(float(list[3]))
    #r2 is time
    if list[4].lower() == "none":
        temp.append(None)
    else:
        temp.append(int(list[4]))
    #r3 is convexity
    temp.append(int(list[5]))
    #r4 is reason for failure
    if int(list[2]) == 0:
        if len(list) > 6 and list[6].strip().lower() != "none":
            temp.append(list[6].strip())
    else:
        temp.append(None)
    return temp


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
            fontsize=6
        )

def graph():
    Llist, Tlist, Plist, Nlist, Clist, Blist, Dlist, TNlist = [], [], [], [], [], [], [], []
    with open("./checkpointfiles/type1constraints.csv") as f:
        for line in f:
            line = line.strip().split(",")
            if line[1] == "L-BFGS-B" and line[2].lower() != "none":
                Llist.append(cleaner(line))
            elif line[1] == "TNC" and line[2].lower() != "none":
                Tlist.append(cleaner(line))
            elif line[1] == "Powell" and line[2].lower() != "none":
                Plist.append(cleaner(line))
            elif line[1] == "Nelder-Mead" and line[2].lower() != "none":
                Nlist.append(cleaner(line))
            elif line[1] == "CG" and line[2].lower() != "none":
                Clist.append(cleaner(line))
            elif line[1] == "BFGS" and line[2].lower() != "none":
                Blist.append(cleaner(line))
            elif line[1] == "dogleg" and line[2].lower() != "none":
                Dlist.append(cleaner(line))
            elif line[1] == "trust-ncg" and line[2].lower() != "none":
                TNlist.append(cleaner(line))
                
                
    TClist, SQlist, COlist = [], [], []
    with open("./checkpointfiles/type2constraints.csv") as f:
        for line in f:
            line = line.strip().split(",")
            if line[1] == "trust-constr" and line[4].lower() != "none":
                TClist.append(cleaner(line))
            elif line[1] == "SLSQP" and line[4].lower() != "none":
                SQlist.append(cleaner(line))
            elif line[1] == "COBYLA" and line[4].lower() != "none":
                COlist.append(cleaner(line))
        
    
    
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
        reason = []
        for r in runs:
            success.append(r[0])
            time.append(r[1])
            convexity.append(r[2])
            if len(r) == 5:
                reason.append(r[4])
            else:
                reason.append(None)

        #use the convexity calculation to sort into different convexities
        #might remap this into a function if graph needs to graph other things
        convexTime = []
        nonconvexTime = []
        convexFailTime = []
        nonconvexFailTime = []
        
        c_fail_counts  = {"Timeout": 0, "Nan/Inf": 0, "Float Error": 0, "Solver Error": 0}
        nc_fail_counts = {"Timeout": 0, "Nan/Inf": 0, "Float Error": 0, "Solver Error": 0}
        
        i = 0
        while i < len(time):
            if convexity[i] == 1 and success[i] == 1:
                convexTime.append(time[i])
            elif convexity[i] == 0 and success[i] == 1:
                nonconvexTime.append(time[i])
            elif convexity[i] == 1 and success[i] == 0:
                convexFailTime.append(time[i])
                if reason[i]:
                    c_fail_counts[reason[i]] += 1
            elif convexity[i] == 0 and success[i] == 0:
                nonconvexFailTime.append(time[i])
                if reason[i]:
                    nc_fail_counts[reason[i]] += 1
            i += 1

        #the block below just gets the average of times simple formulas
        convexTotal = sum(convexTime)
        nonconvexTotal = sum(nonconvexTime)
        convexFailTimeTotal = sum(convexFailTime)
        nonconvexFailTimeTotal = sum(nonconvexFailTime)
        
        if len(convexTime) > 0:
            avg_convex = (convexTotal / len(convexTime)) 
        else:
            avg_convex = 0
            
        if len(nonconvexTime) > 0:
            avg_nonconvex = (nonconvexTotal / len(nonconvexTime))
        else:
            avg_nonconvex = 0
            
        if len(convexFailTime) > 0:
            avg_c_fail = (convexFailTimeTotal / len(convexFailTime))
        else:
            avg_c_fail = 0
            
        if len(nonconvexFailTime) > 0:
            avg_nc_fail = (nonconvexFailTimeTotal / len(nonconvexFailTime))
        else:
            avg_nc_fail = 0

        #this is used for the totals that are displayed above the bars
        num_convex = len(convexTime)
        num_nonconvex = len(nonconvexTime)
        num_c_fail = len(convexFailTime)
        num_nc_fail = len(nonconvexFailTime)
    
        return [avg_convex, avg_nonconvex, avg_c_fail, avg_nc_fail, num_convex, num_nonconvex, num_c_fail, num_nc_fail, c_fail_counts, nc_fail_counts]

    #given 4 lists a title, filename and a bounded flag make a graph
    def graph_helper(l1, l2, l3, l4, title, filename, b_flag):
        avg1 = avg_for(l1)
        avg2 = avg_for(l2)
        avg3 = avg_for(l3)
        avg4 = avg_for(l4)

        #this sorts those results into useful information for the bars
        if b_flag:
            methods = ["L-BFGS-B", "TNC", "Powell", "Nelder-Mead"]
        else:
            methods = ["CG", "BFGS", "dogleg", "trust-ncg"]
            
        convex_avgs = [avg1[0], avg2[0], avg3[0], avg4[0]]
        nonconvex_avgs = [avg1[1], avg2[1], avg3[1], avg4[1]]
        c_fail_avg = [avg1[2], avg2[2], avg3[2], avg4[2]]
        nc_fail_avg = [avg1[3], avg2[3], avg3[3], avg4[3]]
        total_convex = [avg1[4], avg2[4], avg3[4], avg4[4]]
        total_nonconvex = [avg1[5], avg2[5], avg3[5], avg4[5]]
        total_c_fail = [avg1[6], avg2[6], avg3[6], avg4[6]]
        total_nc_fail = [avg1[7], avg2[7], avg3[7], avg4[7]]

        #x just is 4 evenly spaced __
        x = np.arange(4)
        width = 0.25
        
        #set the bar groups for each type of result
        bars1 = plt.bar(x - width, convex_avgs, width=width, label="Convex")
        bars2 = plt.bar(x, nonconvex_avgs, width=width, label="Nonconvex")
        bars3 = plt.bar(x + width/2 + width/4, c_fail_avg, width=(width/2), label="Convex Fails")
        bars4 = plt.bar(x + width + width/4, nc_fail_avg, width=(width/2), label="Nonconvex Fails")
        
        
        plt.xticks(x, methods)
        plt.yscale("log")
        plt.ylabel("Average Time (s, logrithmic)")
        plt.title(title)
        plt.legend()

        #This adds the total # to the bars
        annotate_bars(bars1, total_convex)
        annotate_bars(bars2, total_nonconvex)
        annotate_bars(bars3, total_c_fail)
        annotate_bars(bars4, total_nc_fail)

        plt.savefig(f"./outputimages/{filename}.png")
        plt.show()
        
        
        
    
    def graph_helper_2(l1, l2, l3, title, filename):
        avg1 = avg_for(l1)
        avg2 = avg_for(l2)
        avg3 = avg_for(l3)

        #this sorts those results into useful information for the bars
        methods = ["trust-constr", "SLSQP", "COBYLA"]
        convex_avgs = [avg1[0], avg2[0], avg3[0]]
        nonconvex_avgs = [avg1[1], avg2[1], avg3[1]]
        c_fail_avg = [avg1[2], avg2[2], avg3[2]]
        nc_fail_avg = [avg1[3], avg2[3], avg3[3]]
        total_convex = [avg1[4], avg2[4], avg3[4]]
        total_nonconvex = [avg1[5], avg2[5], avg3[5]]
        total_c_fail = [avg1[6], avg2[6], avg3[6]]
        total_nc_fail = [avg1[7], avg2[7], avg3[7]]

        #x just is 3 evenly spaced __
        x = np.arange(3)
        width = 0.33
        #set the bar groups for each type of result
        bars1 = plt.bar(x - width, convex_avgs, width=width, label="Convex")
        bars2 = plt.bar(x, nonconvex_avgs, width=width, label="Nonconvex")
        bars3 = plt.bar(x + width/2 + width/4, c_fail_avg, width=width/2, label="Convex Fails")
        bars4 = plt.bar(x + width + width/4, nc_fail_avg, width=width/2, label="Nonconvex Fails")

        plt.xticks(x, methods)
        plt.yscale("log")
        plt.ylabel("Average Time (s, logrithmic)")
        plt.title(title)
        plt.legend()

        #This adds the total # to the bars
        annotate_bars(bars1, total_convex)
        annotate_bars(bars2, total_nonconvex)
        annotate_bars(bars3, total_c_fail)
        annotate_bars(bars4, total_nc_fail)
        
        plt.savefig(f"./outputimages/{filename}.png")
        plt.show()
        
        
    
    graph_helper(Llist, Tlist, Plist, Nlist, "All (bounded) Type 1 methods all dimensions", "bounded/type1AllDims", 1)
    graph_helper(Clist, Blist, Dlist, TNlist, "All (unbounded) Type 1 methods all dimensions", "unbounded/type1AllDims", 0)
    graph_helper_2(TClist, SQlist, COlist, "All Type 2 methods all dimensions", "type2AllDims")
    
    l1, l2, l3 = [], [], []
    l11, l21, l31 = [], [], []
    l111, l211, l311 = [], [], []
    
    for i in TClist:
        if i[3] <= 20:
            l1.append(i)
        elif i[3] <= 500:
            l11.append(i)
        else:
            l111.append(i)
    
    for i in SQlist:
        if i[3] <= 20:
            l2.append(i)
        elif i[3] <= 500:
            l21.append(i)
        else:
            l211.append(i)
    
    for i in COlist:
        if i[3] <= 20:
            l3.append(i)
        elif i[3] <= 500:
            l31.append(i)
        else:
            l311.append(i)

    
    l1, l2, l3, l4, l5, l6, l7, l8 = [], [], [], [], [], [], [], []
    l11, l21, l31, l41, l51, l61, l71, l81 = [], [], [], [], [], [], [], []
    l111, l211, l311, l411, l511, l611, l711, l811, = [], [], [], [], [], [], [], []
    
    for i in Llist:
        if i[3] <= 20:
            l1.append(i)
        elif i[3] <= 500:
            l11.append(i)
        else:
            l111.append(i)
            
    for i in Tlist:
        if i[3] <= 20:
            l2.append(i)
        elif i[3] <= 500:
            l21.append(i)
        else:
            l211.append(i)
            
    for i in Plist:
        if i[3] <= 20:
            l3.append(i)
        elif i[3] <= 500:
            l31.append(i)
        else:
            l311.append(i)
            
    for i in Nlist:
        if i[3] <= 20:
            l4.append(i)
        elif i[3] <= 500:
            l41.append(i)
        else:
            l411.append(i)
            
    for i in Clist:
        if i[3] <= 20:
            l5.append(i)
        elif i[3] <= 500:
            l51.append(i)
        else:
            l511.append(i)
            
    for i in Blist:
        if i[3] <= 20:
            l6.append(i)
        elif i[3] <= 500:
            l61.append(i)
        else:
            l611.append(i)
            
    for i in Dlist:
        if i[3] <= 20:
            l7.append(i)
        elif i[3] <= 500:
            l71.append(i)
        else:
            l711.append(i)
            
    for i in TNlist:
        if i[3] <= 20:
            l8.append(i)
        elif i[3] <= 500:
            l81.append(i)
        else:
            l811.append(i)
    
    graph_helper(l1, l2, l3, l4, "All (bounded) Type 1 methods (dim <= 20)", "bounded/type1DimsSmall", 1)
    graph_helper(l5, l6, l7, l8, "All (unbounded) Type 1 methods (dim <= 20)", "unbounded/type1DimsSmall", 0)
    graph_helper_2(l1, l2, l3, "All Type 2 methods (dim <= 20)", "type2DimsSmall")
    
    graph_helper(l11, l21, l31, l41, "All (bounded) Type 1 methods (20 < dim <= 500)", "bounded/type1DimsMedium", 1)
    graph_helper(l51, l61, l71, l81, "All (unbounded) Type 1 methods (20 < dim <= 500)", "unbounded/type1DimsMedium", 0)
    graph_helper_2(l11, l21, l31, "All Type 2 methods (20 < dim <= 500)", "type2DimsMedium")
    
    graph_helper(l111, l211, l311, l411, "All (bounded) Type 1 methods (500 < dim)", "bounded/type1DimsLarge", 1)
    graph_helper(l511, l611, l711, l811, "All (unbounded) Type 1 methods (500 < dim)", "unbounded/type1DimsLarge", 0)
    graph_helper_2(l111, l211, l311, "All Type 2 methods (500 < dim)", "type2DimsLarge")

