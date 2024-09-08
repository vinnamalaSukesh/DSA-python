# Time complexity = O(N log N)
# Space complexity = O(N)
l = [8, 5, 2, 4, 6, 7, 1, 3]
def merge_ASC(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if arr[left] < arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    for i in range(len(temp)):
        arr[low + i] = temp[i]
def merge_DESC(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    while left <= mid and right <= high:
        if arr[left] > arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1
    for i in range(len(temp)):
        arr[low + i] = temp[i]
def merge_sort_ASC(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort_ASC(arr, low, mid)
    merge_sort_ASC(arr, mid + 1, high)
    merge_ASC(arr, low, mid, high)

def merge_sort_DESC(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    merge_sort_DESC(arr, low, mid)
    merge_sort_DESC(arr, mid + 1, high)
    merge_DESC(arr, low, mid, high)

merge_sort_ASC(l, 0, len(l) - 1)
print(l)
merge_sort_DESC(l, 0, len(l) - 1)
print(l)
