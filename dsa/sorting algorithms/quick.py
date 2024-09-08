# Time complexity = O(N log N)
# Space complexity = O(N)
l = [8, 5, 2, 4, 6, 7, 1, 3]

def partition_ASC(arr,left,right):
    pivot = arr[right]
    j = right - 1
    i = left
    while(i <= j):
        while(i <= j and arr[i] < pivot):
            i += 1
        while(i <= j and arr[j] > pivot):
            j -= 1
        if(i < j):
            arr[i],arr[j] = arr[j],arr[i]
            i += 1
            j -= 1
        arr[i],arr[right] = arr[right],arr[i]
    return i

def Quick_ASC(arr, left, right):
    if left < right:
        part_pos = partition_ASC(arr, left, right)
        Quick_ASC(arr, left, part_pos - 1)
        Quick_ASC(arr, part_pos + 1, right)

def partition_DESC(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]
    while i <= j:
        while i <= j and arr[i] > pivot:
            i += 1
        while i <= j and arr[j] < pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

def Quick_DESC(arr, left, right):
    if left < right:
        part_pos = partition_DESC(arr, left, right)
        Quick_DESC(arr, left, part_pos - 1)
        Quick_DESC(arr, part_pos + 1, right)

Quick_ASC(l, 0, len(l) - 1)
print(l)
Quick_DESC(l, 0, len(l) - 1)
print(l)