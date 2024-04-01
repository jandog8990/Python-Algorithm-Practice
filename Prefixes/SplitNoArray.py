def splitArray(nums: list[int]) -> int:
    ans = left_section = 0
    total = sum(nums)

    for i in range(len(nums)-1):
        left_section += nums[i]
        right_section = total - left_section
        if left_section >= right_section:
            ans += 1

    return ans

nums = [10, 4, -8, 7]
res = splitArray(nums)
print(f"Res = {res}")
