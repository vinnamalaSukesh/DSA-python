#Time complexity = O(N2)
#Space complexity = O(N)
l = [8,5,2,4,6,7,1,3]

def selection_ASC(arr,i):
    if(i == len(arr) -1):
        return
    low = i
    for j in range(i + 1,len(arr)):
        if(arr[low] > arr[j]):
            low = j
    if(low != i):
        arr[low],arr[i] = arr[i],arr[low]

def selection_DESC(arr,i):
    if(i == len(arr) -1):
        return
    high = i
    for j in range(i + 1,len(arr)):
        if(arr[high] < arr[j]):
            high = j
    if(high != i):
        arr[high],arr[i] = arr[i],arr[high]

for i in range(len(l)):
    selection_ASC(l,i)
print(l)
for i in range(len(l)):
    selection_DESC(l,i)
print(l)