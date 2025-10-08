class lcs():
    def __init__(self,s1,s2):
        self.s1 = s1
        self.s2 = s2
        self.m = len(s1)
        self.n = len(s2)
        self.table = [[0]*(self.n + 1) for x in range(self.m + 1)]
        self.Value = self.calcLcs(); self.reconstruct()
    
    def calcLcs(self):
        table = self.table; 
        m = self.m 
        n = self.n
        for row in range(1,m+1):
            for column in range(1,n+1):
                
                if self.s1[row -1] == self.s2[column - 1]:
                    table[row][column] = table[row - 1][column -1] + 1

                else:
                    table[row][column] = max(table[row-1][column],table[row][column -1])
        self.table = table
        self.reconstruct()
        return table[m][n]

    def reconstruct(self):
        s = ''
        i,j = self.m,self.n
        while i > 0 and j > 0:
            if self.s1[i-1] == self.s2[j-1]:
                s = self.s1[i-1] + s
                i -= 1
                j -= 1
            elif self.table[i-1][j] > self.table[i][j-1]:
                i -= 1
            else: 
                j -= 1
        self.lcString = s


    def showTable(self):
        for i in self.table:
            print(i)

    def showString(self):
        print(self.lcString)

s1 = input("enter string 1:")
s2 = input("enter string 2:")
lc = lcs(s1,s2)
print(lc.Value)
lc.showTable()
print(lc.lcString)