def arr_input():
    size = int(input("enter the size of array: "))
    arr =[]
    for i in range(0,size):
        arr.append( int(input(f"Enter array element no. {i+1} : ")))
    
    return arr

def BubbleSort(arr):
    size = len(arr)
    for i in range(0,size):
        for j in range(0,size-i-1):
            if arr[j] >= arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

def insertionSort(arr):
    size = len(arr)

    for i in range(1,size):
        pivot = i
        while (arr[pivot] < arr[pivot-1])&(pivot > 0 ):
            arr[pivot],arr[pivot-1] = arr[pivot-1],arr[pivot]
            pivot = pivot - 1


def selectionSort(arr):

    for pivot in range (0,len(arr)):
        lowest = pivot #sets the pivot location as the location with the lowest number

        for j in range(pivot,len(arr)): #traverses the array ahead of the pivot element

            if arr[j] < arr[lowest]: #comapres the current elements with the lowest yet, and reaplaces if true
                lowest = j

        arr[pivot],arr[lowest]=arr[lowest],arr[pivot] #swaps the lowest element with the pivot location     

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)

def binarySearch(arr,target = None):
    if target == None:
        target = int(input("Enter the number to search for:"))

    low = 0; high = len(arr) - 1

    while low <= high:
        mid = (high + low)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid+1
        else:
            high = mid - 1
    return -1

def selectSort(arr):
    sorts = ["Bubble Sort","Insertion Sort","Selection Sort","QuickSort"]
    for i in range(0,len(sorts)):
        print(f"{i+1}. {sorts[i]}")
    select = int(input("Select a Sorting algorithm: "))
    if select not in range(1,len(sorts)+1):
        print("invalid selection")
        return selectSort(arr)
    else:
        print(f"you selected {sorts[select - 1]}")
        match select:
            case 1:
                BubbleSort(arr)
            case 2:
                insertionSort(arr)
            case 3:
                selectionSort(arr)
            case 4:
                quicksort(arr)


array = arr_input()
print(array)
selectSort(array)
print(array)
index = binarySearch(array)
print(f'the required number is at index {index}')