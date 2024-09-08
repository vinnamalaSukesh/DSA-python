# Time complexity = O(N log N)
# Space complexity = O(1)
l = [8, 5, 2, 4, 6, 7, 1, 3]
def heapify_ASC(arr, N, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < N and arr[i] < arr[left]:
        largest = left
    if right < N and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_ASC(arr, N, largest)

def heapify_DESC(arr, N, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < N and arr[i] > arr[left]:
        smallest = left
    if right < N and arr[smallest] > arr[right]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify_ASC(arr, N, smallest)

def heapSort_ASC(arr):
    N = len(arr)
    for i in range(N // 2 - 1, -1, -1):
        heapify_ASC(arr, N, i)
    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify_ASC(arr, i, 0)

def heapSort_DESC(arr):
    N = len(arr)
    for i in range(N // 2 - 1, -1, -1):
        heapify_DESC(arr, N, i)
    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify_DESC(arr, i, 0)

heapSort_ASC(l)
print(l)
heapSort_DESC(l)
print(l)
