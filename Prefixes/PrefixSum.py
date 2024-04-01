# find the sum of prefixes of array
# [3, 6, 2, 8, 1, 4, 1, 5]
# each elem of the new prefix arr will be
# the sum up to the current index
def prefix_sum(arr: list[int]) -> list[int]:
    prefix = [arr[0]]
    for i in range(1, len(arr)):
        # we take the prefix len since we are appending to it 
        prefix.append(arr[i] + prefix[len(prefix)-1])
    return prefix

arr = [3, 6, 2, 8, 1, 4, 1, 5]
res = prefix_sum(arr)
print("Res:")
print(res)
print("\n")
