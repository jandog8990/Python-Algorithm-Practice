from collections import defaultdict

# find array of numbers that intersects all the 
# unique rows in the matrix
def findIntersections(nums: list[list[int]]) -> list[int]:
    counts = defaultdict(int)
    N = len(nums)
    print(f"N = {N}")
    
    # create the hashmap with counts of elems
    for arr in nums:
        for x in arr:
            counts[x] += 1

    # loop through keys and compare
    # with the length of rows for uniqueness
    uniques = []
    for key in counts:
        if counts[key] == N:
            uniques.append(key)

    return sorted(uniques)

nums = [[3,1,2,4,5],
        [1,2,3,4],
        [3,4,5,6]]
print("Nums:")
print(nums)
print("\n")

resp = findIntersections(nums)
print("Resp:")
print(resp)
print("\n")

