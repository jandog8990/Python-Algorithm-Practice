# find sum of subarray with largest sum
# whose length is k. 
# NOTE: As we add elements to the right 
# at index i, then remove i-k
def max_subarr_window(nums: list[int], k: int) -> int:
    curr = 0
    # start with the first window [0, k-1] 
    for i in range(k):
        curr += nums[i]
    print(f"Current = {curr}")
    print("\n")
    
    # finish with remaining windows [k, N-1]
    ans = curr 
    for i in range(k, len(nums)):
        print(f"i = {i}, k = {k}") 
        print(f"prev curr = {curr}")
        curr += nums[i] - nums[i-k]
        print(f"curr = {nums[i]} - {nums[i-k]} = {nums[i] - nums[i-k]}")
        ans = max(ans, curr)
        print(f"max({ans}, {curr}) = {ans}") 
        print("\n")

    return ans

k = 4
nums = [3, -1, 4, 12, -8, 5, 6]
print(f"Nums = {nums}")
print(f"k = {k}")
res = max_subarr_window(nums, k)
print(f"Res = {res}")
