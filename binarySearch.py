def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        middleElement = (left + right) // 2

        if arr[middleElement] == target:
            return middleElement
        
        elif arr[middleElement] < target:
            left = middleElement + 1
        
        else:
            right = middleElement - 1
    
    return -1 

arr = [2, 3, 5, 7, 11, 13, 17, 19]
target = 7

result = binary_search(arr, target)
if result != -1:
    print(f"Elemento encontrado no índice: {result}")
else:
    print("Elemento não encontrado")