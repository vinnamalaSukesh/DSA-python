#Time complexity = O(N2)
#Space complexity = O(N)
l = [8,5,2,4,6,7,1,3]
def bubble_ASC(arr,n):
    if(n == 1):
        return
    for j in range(n - 1):
        if(arr[j] > arr[j + 1]):
            arr[j],arr[j + 1] = arr[j + 1],arr[j]

def bubble_DESC(arr,n):
    if(n == 1):
        return
    for j in range(n - 1):
        if(arr[j] < arr[j + 1]):
            arr[j],arr[j + 1] = arr[j + 1],arr[j]

for i in range(len(l)):
    bubble_ASC(l,len(l) - i)
print(l)

for i in range(len(l)):
    bubble_DESC(l,len(l) - i)
print(l)