def check_for_target(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        nsum = nums[left] + nums[right]
        if nsum == target:
            print(f"Sum = {nsum}") 
            return True
        
        if nsum > target:
            # reduce the right index
            right -= 1
        if nsum < target:
            # increase the left index
            left += 1

    return False

nums = [1, 2, 4, 6, 8, 9, 14, 15]
res = check_for_target(nums, 13)
print(f"Resp = {res}")
