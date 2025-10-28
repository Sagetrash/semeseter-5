def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array)//2
    left = merge_sort(array[:mid])
    right= merge_sort(array[mid:])
    return sort(left,right)

def sort(left,right):
    new = []
    i,j = 0,0
    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1
    new.extend(left[i:])
    new.extend(right[j:])
    return new

array = [0,3,4,2,1]
print(merge_sort(array))
