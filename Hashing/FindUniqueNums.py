# make sure (num+1) and (num-1) not in the
# unique set, then add to the arr list
def findUniqueNums(nums: list[int]) -> set:
    # convert nums to set for uniqueness
    ans = []    # arr with uniques
    nums = set(nums)

    for num in nums:
        if (num+1 not in nums) and (num-1 not in nums):
            ans.append(num)

    return ans
