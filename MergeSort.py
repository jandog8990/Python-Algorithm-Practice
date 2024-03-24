# Python merge sort algorithm
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        # divid arr elems
        left = arr[:mid]
        right = arr[mid:]

        # recursion: sort the first half
        mergeSort(left)

        # sor tright half
        mergeSort(right)

        # set the indices
        i = j = k = 0

        # copy data to tmp arrays
        print(f"Mid = {mid}") 
        print(f"len(left): {len(left)} = {left}")
        print(f"len(right): {len(right)} = {right}")
        print("\n")

        # copy temp arrays
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                li = left[i]
                rj = right[j]
                arr[k] = left[i]
                print(f"left[{i}] <= right[{j}]")
                print(f"{li} <= {rj}")
                print(f"arr[{k}] = left[i] = {arr[k]}")
                i+=1
                print(f"i += 1 = {i}") 
                print("\n")
            else:
                arr[k] = right[j]
                print(f"left[{i}] > right[{j}]")
                print(f"arr[{k}] = right[j] = {arr[k]}")
                j+=1
                print(f"j += 1 = {j}") 
                print("\n")
            k+=1
       
        # check if any elem is left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

if __name__ == '__main__':
    arr = [12, 11, 14, 5, 6, 7]
    print("Arr:")
    print(arr)
    print("Sorted arr:") 
    mergeSort(arr)
    print(arr)
