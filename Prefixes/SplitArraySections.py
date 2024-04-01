# compare the left section of array with right section
# of array (this uses prefix sums to calc intervals sums)
def splitArray(nums: list[int]) -> int:
    N = len(nums)
    prefix = [nums[0]]
    for i in range(1, N): 
        prefix[i].append(prefix[-1] + nums[i])

    ans = 0
    for i in range(N-1):
        left_section = prefix[i]
        right_section = prefix[-1] - prefix[i]
        if left_section >= right_section:
            ans += 1

    return ans
