# Merges two subarrays of arr[]
# First -  arr[l..m]
# Second - arr[m+1..r]
def merge(arr, l, m, r):
    print("Merge call:")
    print(f"{l} - {m} - {r}") 
    # L and R represent the number of indices
    # present for the left/right subarrays
    L = m - l + 1
    R = r - m
    print(f"L = {m} - {l} + 1 = {L}")
    print(f"R = {r} - {m} = {R}")

    # copy data to temp arrays
    Larr = [0] * (L)
    Rarr = [0] * (R)
   
    # copy data from arr to sub arrays
    for i in range(0, L):
        Larr[i] = arr[l + i]
    for j in range(0, R):
        # index is 0 based so need to increase 
        Rarr[j] = arr[m + 1 + j]
    print(f"Larr = {Larr}")
    print(f"Rarr = {Rarr}")
   
    # Merge temp arrays back into arr[l..r]
    # this updates the arr based on left/right conditions
    i = 0   # init index of first subarray
    j = 0   # init index of second subarray
    k = l   # init left index of merged subarray

    # run while loop comparing left and right sides
    print("Begin Left and Right checks:")
    while i < L and j < R:
        print(f"index i = {i}") 
        print(f"index j = {j}") 
        print(f"index k = {k}") 
        if Larr[i] < Rarr[j]:
            print(f"{Larr[i]} < {Rarr[j]}")
            arr[k] = Larr[i]
            print(f"arr[{k}] = {arr[k]}") 
            i += 1
        else:
            print(f"{Larr[i]} >= {Rarr[j]}")
            arr[k] = Rarr[j]
            print(f"arr[{k}] = {arr[k]}") 
            j += 1
        k += 1
        print("\n")
   
    # copy remaining elems of L[]
    while i < L:
        arr[k] = Larr[i]
        i+=1
        k+=1
    
    # copy remaining elems of R[]
    while j < R:
        arr[k] = Rarr[j]
        j+=1
        k+=1

    
    print("Merged array:")
    print(arr)
    print("\n")
    
# merge sort using L/R indices of
# sub-arry of main arr
def mergeSort(arr, l, r):
    print("Merge sort call:")
    print(f"Left idx = {l}")
    print(f"Right idx = {r}")

    if l < r:
        # same as (l+r)//2 but avoids overflow
        m = l + (r-l)//2
        print(f"L < R => Middle = {m}")
        print("\n")

        # sort left half 
        print(f"Merge sort left side: L={l}, R={m}") 
        mergeSort(arr, l, m)
        
        # sort right half 
        print(f"Merge sort right side: L={m+1}, R={r}") 
        mergeSort(arr, m+1, r)

        # merge the entire arr
        print(f"--- Merge arr ---") 
        print(f"l = {l}")
        print(f"m = {m}")
        print(f"r = {r}")
        print("--------------\n") 
        merge(arr, l, m, r)

# test code
arr = [12, 11, 13, 5, 6, 7]
N = len(arr)
print(f"Unsorted arr:")
print(arr)
print("\n")

mergeSort(arr, 0, N-1)
