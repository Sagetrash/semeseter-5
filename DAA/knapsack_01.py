class knapsack:
    def __init__(self,vl,wt,cap):
        self.vl = vl; self.wt = wt; self.cap = cap
    
    def knap01(self):
        vl = self.vl;wt = self.wt; cap = self.cap
        self.n = n = len(vl)
        table = []
        
        for _ in range(n+1):
            table.append([0]*(cap+1)) #creating an empty table for the knapsack
        
        for i in range(1,n+1): #fetermining rows (item number)
            for j in range(1,cap + 1): #determining capacity number
                if wt[i-1] <= j: 
                    item_included = table[i-1][j-wt[i-1]] + vl[i-1]
                    item_excluded = table[i-1][j]
                    table [i][j] = max(item_included,item_excluded)
                else:
                    table[i][j] = table[i-1][j]
                    
        self.table = table
        self.maxValue = table[n][cap]

    def showTable(self):
        for i in self.table:
            print(i)

    def getItems(self):
        items = []
        j = self.cap

        for i in range(self.n,0,-1):
            if self.table[i][j] != self.table[i-1][j]:
                items.append(i-1)
                j = j - self.wt[i-1]
        return items       
items = [[300,2,"microscope"],[200,1,"Globe"],[400,5,"trophy"],[500,3,"crown"]] #([values,weight,item no.])
cap = 10
vl = [items[i][0] for i in range(len(items))]
wt = [items[i][1] for i in range(len(items))]

k = knapsack(vl,wt,cap)
k.knap01()
k.showTable()
print(k.maxValue)
for i in k.getItems():
    print([items[i][2]])