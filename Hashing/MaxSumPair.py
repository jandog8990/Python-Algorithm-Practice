from collections import defaultdict
# find maximum sum of the pair of nums
"""
Given array of ints 'nums', find max val
of nums[i] + nums[j], where nums[i] and 
nums[j] have the same digit sum (sum of 
their individual digits)
"""
def maximumSum(nums: list[int]) -> int:
    def get_digit_sum(num):
        digit_sum = 0
        # this loop finds the num sum 
        while num:
            digit_sum += num % 10
            sum //= 10

        return digit_sum

    num_sum_map = defaultdict(int)
    res = -1
    for num in nums:
        # get the current digit sum
        digit_sum = get_digit_sum(num)
        if digit_sum in num_sum_map:
            res = max(res, num + num_sum_map[digit_sum])
        num_sum_map[digit_sum] = max(num_sum_map[digit_sum], num)

    return res
