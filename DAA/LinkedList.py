class Node:
    def __init__(self,name,age,salary,next= None):
        self.name = name
        self.age = age
        self.salary = salary
        self.next = next

class EmployeeList:
    def __init__(self,nameArr,ageArr,SalaryArr):
        self.names = nameArr
        self.ages = ageArr
        self.salaries = SalaryArr
        
    def sortByName(self):
        a = []
        names = self.names
        n = len(names)
        for i in range(n):
            a.append([self.names[i],self.ages[i],self.salaries[i]])
        
        for i in range(n):
            for j in range(i+1,n):
                if a[i][0] > a[j][0]:
                    a[i],a[j] = a[j],a[i]
        self.array2d = a

    def CreateList(self):
        arr = self.array2d
        i = 0
        root = Node(arr[i][0],arr[i][1],arr[i][2])
        a = root; i+= 1
        while i < len(arr):
            a.next = Node(arr[i][0],arr[i][1],arr[i][2])
            a = a.next; i += 1
        self.root = root

    def ShowList(self):
        root = self.root
        a = root
        while a.next != None:
            print(f"{a.name},{a.age},{a.salary}")
            a = a.next
        print(f"{a.name},{a.age},{a.salary}")



name = ['Ayush',"Harshit","Rohit","Yash","lalit","Om","Aryan","Shreya","Kavya","keshav"]
age = [19,18,20,21,33,23,25,43,23,26]
salary = [1000,2000,3000,15000,5000,5000,5000,5000,6000,10000]
e = EmployeeList(name,age,salary)
e.sortByName()
e.CreateList()
e.ShowList()
