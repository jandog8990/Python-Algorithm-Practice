def square_sort_arr(arr):
    N = len(arr) 
    left = 0
    right = len(arr)-1
    sq_nums = [int(num)**2 for num in nums] 
    print(sq_nums) 
    result = [0]*N

    for i in range(N-1, -1, -1):
        if sq_nums[left] < sq_nums[right]:
            result[i] = sq_nums[right]
            right -= 1
        else:
            result[i] = sq_nums[left]
            left += 1
    return result
     
nums = [-4, -1, 0, 3, 10]
res = square_sort_arr(nums)
print("Result:")
print(res)
print("\n")
