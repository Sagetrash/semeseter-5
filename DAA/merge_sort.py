class node:
    leaf = False

    def __init__(self, array, parent = None):
        self.array = array
        self.parent = parent
        mid = len(self.array)//2
        if len(array) > 1:
            self.left = node(self.array[0:mid],self)
            self.right = node(self.array[mid:],self)
            self.sort()
        else:
            self.leaf = True
        

      
    def sort(self):
        self.array = []
        i,j = 0,0
        left_arr = self.left.array
        right_arr = self.right.array
        while (i < len(left_arr)) and (j < len(right_arr)):
            if left_arr[i] < right_arr[j]:
                self.array.append(left_arr[i])
                i = i+1
            else:
                self.array.append(right_arr[j])
                j = j+1
        self.array.extend(left_arr[i:])
        self.array.extend(right_arr[j:])

