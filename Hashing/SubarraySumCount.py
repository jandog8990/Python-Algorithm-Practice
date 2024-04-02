from collections import defaultdict

# calculate the sums of subarrays and return
# number of subarrays with sum == k
def subarraySumCount(nums: list[int], k: int) -> int:
    counts = defaultdict(int)
    counts[0] = 1   # init with zero index
    ans = 0
    curr = 0

    # calculate current sum up to the curr index
    for num in  nums:
        curr += num
        print(f"Curr = {curr}") 
        # if there exists a difference in the map
        # that contains curr - k, add to ans
        print(f"Curr - k = {curr -k}") 
        print(f"counts[curr-k] = {counts[curr-k]}") 
        ans += counts[curr - k]
        print(f"ans = {ans}") 
        counts[curr] += 1 
        print(f"counts:")
        print(counts)
        print("\n")
  
    print("Counts map:")
    print(counts)
    return ans

#nums = [1,2,1,2,1]
#k = 3
nums = [1, -1, 1, -1] 
k = 0 
res = subarraySumCount(nums, k)
print(f"Ans = {res}")
