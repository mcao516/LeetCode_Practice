def partition(arr, low, high):
    i = low - 1  # i is the index of the small element on the most right
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1  # arr[i++] is either a big element or the element itself
            arr[i], arr[j] = arr[j], arr[i] 

    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return i + 1


def quickSort(arr, low, high):
    """The main function that implements QuickSort.

    Args:
        arr: Array to be sorted
        low: Starting index
        high: Ending index (inclusive)
    
    """
    # if len(arr) == 1:
    #     return arr
    if low < high:
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition 
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


arr = [10, 4, 2, 40, 3]
print(arr)
quickSort(arr, 0, len(arr)-1)
print(arr)