#Time complexity = O(N2)
#Space complexity = O(N)
l = [8,5,2,4,6,7,1,3]
def selection(arr):
    for i in range(len(arr) - 1):
        low = i
        for j in range(i + 1,len(arr)):
            if(arr[low] > arr[j]):
                low = j
        if(i != low):
            arr[i],arr[low] = arr[low],arr[i]
    return arr
print(selection(l))