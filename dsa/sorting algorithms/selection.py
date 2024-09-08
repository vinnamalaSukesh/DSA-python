#Time complexity = O(N2)
#Space complexity = O(N)
l = [8,5,2,4,6,7,1,3]
def selection_ASC(arr):
    for i in range(len(arr) - 1):
        low = i
        for j in range(i + 1,len(arr)):
            if(arr[low] > arr[j]):
                low = j
        if(i != low):
            arr[i],arr[low] = arr[low],arr[i]
    return arr
def selection_DESC(arr):
    for i in range(len(arr) - 1):
        high = i
        for j in range(i + 1,len(arr)):
            if(arr[high] < arr[j]):
                high = j
        if(i != high):
            arr[i],arr[high] = arr[high],arr[i]
    return arr
print(selection_ASC(l))
print(selection_DESC(l))