# calculate the largest sum of subarray and return the length
def sub_sum(nums, k):
    # set the pointers and sum
    left = 0 
    curr_sum = 0

    # set the window len
    N = len(nums) 
    window_len = 0

    # outter loop for the main arr
    for right in range(0, (N-1)):
        curr_sum += nums[right] # running some from the left
       
        # check the curr sum against the target k
        while (curr_sum > k):
            # subtract the left index from the sum 
            curr_sum -= nums[left]
            left += 1

        # find the max window len, where (R-L+1)
        window_len = max(window_len, right-left+1)

    return window_len

nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8
res = sub_sum(nums, k)
print(f"Final result = {res}")
