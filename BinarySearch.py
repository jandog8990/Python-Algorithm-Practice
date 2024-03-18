# Binary search algo - splits list to find
# particular value using halving algo

# returns location of specific val given arr
class BinarySearch:
    def __init__(self, arr):
        self.arr = arr 

    # iterative binary search using while loop
    def runIterativeBinarySearch(self, left, right, x):
        #left = 0
        #right = len(self.arr)-1

        # actual binary search splitting the list in half
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == x:
                # step 1: check if x is mid
                return mid
            elif arr[mid] < x:
                # step 2: check if x is > mid
                # ignore the left half of list
                left = mid+1 # increase idx
            else:
                # step 3: if x < mid 
                # ignore right half
                right = mid-1
           
        # if we reach => elem was no present
        return -1

    # recursive binary search using the same func call
    def runRecursiveBinarySearch(self, left, right, x):
        if right >= left:

            # split the batch
            mid = left + (right - left) // 2

            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                # ignore the left side
                left = mid+1
                return self.runRecursiveBinarySearch(left, right, x)
            else:
                # ignore the right
                right = mid-1
                return self.runRecursiveBinarySearch(left, right, x)

        return -1

arr = [2, 4, 8, 23, 45, 67]
x = 4 
left = 0
right = len(arr)-1

# create the arr obj
binaryObj = BinarySearch(arr)
result = binaryObj.runIterativeBinarySearch(left, right, x)
result2 = binaryObj.runRecursiveBinarySearch(left, right, x)
print(f"Iterative Binary result = {result}")
print(f"Recursive Binary result = {result2}")
print("\n")


