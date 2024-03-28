# algorithm to find max subarray containing a
# product that is < target k
def subarrProduct(nums: list[int], k: int) -> int:
    # first check that if prod is 1 then we return nothing
    if k <= 1:
        return 0

    left = 0
    currProd = 1
    numSubarrays = 0
    for right in range(len(nums)):
        currProd *= nums[right]
        while currProd >= k:
            # remove the left side to decrease prod
            currProd //= nums[left]
            left += 1

        # set the window length
        numSubarrays += right - left + 1

    return numSubarrays 

nums = [10, 5, 2, 6]
k = 100
res = subarrProduct(nums, k)
print(f"Result = {res}")
