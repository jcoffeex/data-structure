def quicksort(arr):
    size = len(arr)

    if(size <= 1):
        return arr
    
    pivot = arr[-1]

    left = []
    right = []

    for x in arr[:-1]:
        if x <= pivot:
            left.append(x)

    for x in arr[:-1]:
        if x > pivot:
            right.append(x)

    return quicksort(left) + [pivot] + quicksort(right) 

arr = [3, 7, 2, 5, 1, 6, 4]
sorted_arr = quicksort(arr)
print(sorted_arr)