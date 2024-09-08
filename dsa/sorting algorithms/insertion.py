#Time complexity = O(N2)
#Space complexity = O(N)
l = [8,5,2,4,6,7,1,3]
def insertion_ASC(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i -1
        while(j >= 0 and temp < arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr
def insertion_DESC(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i -1
        while(j >= 0 and temp > arr[j]):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr
print(insertion_ASC(l))
print(insertion_DESC(l))