#Time complexity = O(N2)
#Space complexity = O(N)
l = [8,5,2,4,6,7,1,3]
def bubble_sort(arr):
    for i in range(0,len(arr) - 1):
        for j in range(i + 1,len(arr)):
            if(arr[i] > arr[j]):
                arr[i],arr[j] = arr[j],arr[i]
    return arr
print(bubble_sort(l))