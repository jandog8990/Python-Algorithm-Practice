def combine(arr1, arr2):
    # initialize indices and the result
    result = []
    i = j = 0
    
    # main loop for comparing arr1 and arr2
    # while the results last and indices fit 
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # remaining numbers will be inserted accordingly
    # since there is nothing to compare against
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result

arr1 = [1, 4, 7, 20]
arr2 = [3, 5, 12]
res = combine(arr1, arr2)
print(res)
