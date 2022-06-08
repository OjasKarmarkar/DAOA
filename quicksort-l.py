def partition(array, low, high):
    # Taking Pivot as Right-most element
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1

# function to perform quicksort
def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

arr = [10,9,8,7,6,5,4,3,2,1]
quickSort(arr, 0, len(arr)-1)
print(arr)