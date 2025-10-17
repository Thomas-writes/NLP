import matplotlib.pyplot as plt
import numpy as np

def cleaner(list):
    #line1 = name 
    #line2 = convexity 
    #line3 = time 
    #line4 = success 
    #line5 = number of variables
    temp = []
    temp.append(int(list[2]))
    temp.append(float(list[3]))
    if list[4].lower() == "none":
        temp.append(None)
    else:
        temp.append(int(list[4]))
    temp.append(int(list[5]))
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
            if line[1] == "L-BFGS-B":
                Llist.append(cleaner(line))
            elif line[1] == "TNC":
                Tlist.append(cleaner(line))
            elif line[1] == "Powell":
                Plist.append(cleaner(line))
            elif line[1] == "Nelder-Mead":
                Nlist.append(cleaner(line))
            elif line[1] == "CG":
                Clist.append(cleaner(line))
            elif line[1] == "BFGS":
                Blist.append(cleaner(line))
            elif line[1] == "dogleg":
                Dlist.append(cleaner(line))
            elif line[1] == "trust-ncg":
                TNlist.append(cleaner(line))
                
                
    TClist, SQlist, COlist = [], [], []
    with open("./checkpointfiles/type2constraints.csv") as f:
        for line in f:
            line = line.strip().split(",")
            if line[1] == "trust-constr":
                TClist.append(cleaner(line))
            elif line[1] == "SLSQP":
                SQlist.append(cleaner(line))
            elif line[1] == "COBYLA":
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
        for r in runs:
            success.append(r[2])
            time.append(r[1])
            convexity.append(r[0])

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
    def graph_helper(l1, l2, l3, l4, l5, l6, l7, l8, title, filename):
        avgL = avg_for(l1)
        avgT = avg_for(l2)
        avgP = avg_for(l3)
        avgN = avg_for(l4)
        avgC = avg_for(l5)
        avgB = avg_for(l6)
        avgD = avg_for(l7)
        avgTN = avg_for(l8)

        #this sorts those results into useful information for the bars
        methods = ["L-BFGS-B", "TNC", "Powell", "Nelder-Mead", "CG", "BFGS", "dogleg", "trust-ncg"]
        convex_avgs = [avgL[0], avgT[0], avgP[0], avgN[0], avgC[0], avgB[0], avgD[0], avgTN[0]]
        nonconvex_avgs = [avgL[1], avgT[1], avgP[1], avgN[1], avgC[1], avgB[1], avgD[1], avgTN[1]]
        fail_avgs = [avgL[2], avgT[2], avgP[2], avgN[2], avgC[2], avgB[2], avgD[2], avgTN[2]]
        total_convex = [avgL[3], avgT[3], avgP[3], avgN[3], avgC[3], avgB[3], avgD[3], avgTN[3]]
        total_nonconvex = [avgL[4], avgT[4], avgP[4], avgN[4], avgC[4], avgB[4], avgD[4], avgTN[4]]
        total_fail = [avgL[5], avgT[5], avgP[5], avgN[5], avgC[5], avgB[5], avgD[5], avgTN[5]]

        #x just is 8 evenly spaced __
        x = np.arange(8)
        width = 0.125
        #set the bar groups for each type of result
        bars1 = plt.bar(x - width, convex_avgs, width=width, label="Convex")
        bars2 = plt.bar(x, nonconvex_avgs, width=width, label="Nonconvex")
        bars3 = plt.bar(x + width, fail_avgs, width=width, label="Fails")

        plt.xticks(x, methods)
        plt.yscale("log")
        plt.ylabel("Average Time (s, logrithmic)")
        plt.title(title)
        plt.legend()

        #This adds the total # to the bars
        annotate_bars(bars1, total_convex)
        annotate_bars(bars2, total_nonconvex)
        annotate_bars(bars3, total_fail)

        plt.savefig(f"./outputimages/{filename}.png")
        plt.show()
        
        
        
    
    def graph_helper_2(l1, l2, l3, title, filename):
        avgL = avg_for(l1)
        avgT = avg_for(l2)
        avgP = avg_for(l3)

        #this sorts those results into useful information for the bars
        methods = ["trust-constr", "SLSQP", "COBYLA"]
        convex_avgs = [avgL[0], avgT[0], avgP[0]]
        nonconvex_avgs = [avgL[1], avgT[1], avgP[1]]
        fail_avgs = [avgL[2], avgT[2], avgP[2]]
        total_convex = [avgL[3], avgT[3], avgP[3]]
        total_nonconvex = [avgL[4], avgT[4], avgP[4]]
        total_fail = [avgL[5], avgT[5], avgP[5]]

        #x just is 3 evenly spaced __
        x = np.arange(3)
        width = 0.33
        #set the bar groups for each type of result
        bars1 = plt.bar(x - width, convex_avgs, width=width, label="Convex")
        bars2 = plt.bar(x, nonconvex_avgs, width=width, label="Nonconvex")
        bars3 = plt.bar(x + width, fail_avgs, width=width, label="Fails")

        plt.xticks(x, methods)
        plt.yscale("log")
        plt.ylabel("Average Time (s, logrithmic)")
        plt.title(title)
        plt.legend()

        #This adds the total # to the bars
        annotate_bars(bars1, total_convex)
        annotate_bars(bars2, total_nonconvex)
        annotate_bars(bars3, total_fail)
        
        plt.savefig(f"./outputimages/{filename}.png")
        plt.show()
        
        
    
    graph_helper(Llist, Tlist, Plist, Nlist, Clist, Blist, Dlist, TNlist, "All Type 1 methods all dimensions", "type1AllDims")
    graph_helper_2(TClist, SQlist, COlist, "All Type 2 methods all dimensions", "type2AllDims")
    
    l1, l2, l3 = [], [], []
    l11, l21, l31 = [], [], []
    l111, l211, l311 = [], [], []
    
    for i in TClist:
        if i[3] <= 50:
            l1.append(i)
        elif i[3] <= 500:
            l11.append(i)
        else:
            l111.append(i)
    
    for i in SQlist:
        if i[3] <= 50:
            l2.append(i)
        elif i[3] <= 500:
            l21.append(i)
        else:
            l211.append(i)
    
    for i in COlist:
        if i[3] <= 50:
            l3.append(i)
        elif i[3] <= 500:
            l31.append(i)
        else:
            l311.append(i)
            
    graph_helper_2(l1, l2, l3, "All Type 2 methods (dim <= 50)", "type2DimsSmall")
    graph_helper_2(l11, l21, l31, "All Type 2 methods (50 < dim <= 500)", "type2DimsMedium")
    graph_helper_2(l111, l211, l311, "All Type 2 methods (500 < dim)", "type2DimsLarge")

    
    l1, l2, l3, l4, l5, l6, l7, l8 = [], [], [], [], [], [], [], []
    l11, l21, l31, l41, l51, l61, l71, l81 = [], [], [], [], [], [], [], []
    l111, l211, l311, l411, l511, l611, l711, l811, = [], [], [], [], [], [], [], []
    
    for i in Llist:
        if i[3] <= 50:
            l1.append(i)
        elif i[3] <= 500:
            l11.append(i)
        else:
            l111.append(i)
            
    for i in Tlist:
        if i[3] <= 50:
            l2.append(i)
        elif i[3] <= 500:
            l21.append(i)
        else:
            l211.append(i)
            
    for i in Plist:
        if i[3] <= 50:
            l3.append(i)
        elif i[3] <= 500:
            l31.append(i)
        else:
            l311.append(i)
            
    for i in Nlist:
        if i[3] <= 50:
            l4.append(i)
        elif i[3] <= 500:
            l41.append(i)
        else:
            l411.append(i)
            
    for i in Clist:
        if i[3] <= 50:
            l5.append(i)
        elif i[3] <= 500:
            l51.append(i)
        else:
            l511.append(i)
            
    for i in Blist:
        if i[3] <= 50:
            l6.append(i)
        elif i[3] <= 500:
            l61.append(i)
        else:
            l611.append(i)
            
    for i in Dlist:
        if i[3] <= 50:
            l7.append(i)
        elif i[3] <= 500:
            l71.append(i)
        else:
            l711.append(i)
            
    for i in TNlist:
        if i[3] <= 50:
            l8.append(i)
        elif i[3] <= 500:
            l81.append(i)
        else:
            l811.append(i)
    
    graph_helper(l1, l2, l3, l4, l5, l6, l7, l8, "All Type 1 methods (dim <= 50)", "type1DimsSmall")
    graph_helper(l11, l21, l31, l41, l51, l61, l71, l81, "All Type 1 methods (50 < dim <= 500)", "type1DimsMedium")
    graph_helper(l111, l211, l311, l411, l511, l611, l711, l811, "All Type 1 methods (500 < dim)", "type1DimsLarge")
    

    
def main():
    graph()
    
main()