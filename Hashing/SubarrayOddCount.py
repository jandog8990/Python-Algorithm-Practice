from collections import defaultdict

# find the number of odd numbers in the given list
# of numbers using hashmaps and mod%2 = 1
def findOddCount(nums: list[int], k: int) -> int:
    counts = defaultdict(int) 
    curr = 0
    ans = 0
    counts[0] = 1

    # loop through nums and update the curr/ans
    for num in nums:
        curr += num%2
        print(f"curr += {num%2} = {curr}")
        ans += counts[curr-k]
        print(f"counts[{curr-k}] = {counts[curr-k]}")
        print(f"ans = {ans}")
        counts[curr] += 1
        print(f"counts[{curr}] += 1 = {counts[curr]}")
        print("\n")
        print(f"counts:")
        print(counts)
        print("\n")

    return ans

nums = [1,1,2,1,1]
k = 3
res = findOddCount(nums, k)
print(f"Res = {res}")
print("\n")
