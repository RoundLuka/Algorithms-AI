def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  


print(linear_search([4, 2, 9, 7, 5, 6], 7))