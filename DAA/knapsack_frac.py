class knapsackFrac:
    def __init__(self,profit,wt,cap):
        self.profit,self.wt,self.cap = profit,wt,cap
        self.table = [(profit[i],wt[i],profit[i]/wt[i]) for i in range(0,len(profit))]
        self.table = sorted(self.table,key = lambda row: row[2],reverse=True)

    def greedy(self):
        net = 0
        currCap = self.cap
        table = self.table
        for i in range(len(table)):
            if (currCap != 0) and (currCap >= table[i][1]):
                net += table[i][0]
                currCap = currCap - table[i][1]
            else:
                net += table[i][2] * currCap
                break
        self.net = net
        return net
        
    def showTable(self):
        for i in self.table: print(i)

val = [60, 100, 120]
wt = [10, 20, 30]
capacity = 50

k = knapsackFrac(val,wt,capacity)
k.showTable()
k.greedy()
print(k.net)