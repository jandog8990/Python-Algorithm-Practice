# pseudocode for sliding window
function f(nums, k):
    left = 0
    curr = 0
    ans = 0
    for (int right = 0; right < nums.length; right++):
        # current sum of the window 
        curr += nums[right]

        # while loop that subtracts when sum
        # does not equal the target
        while (curr > k):
            curr -= nums[left]
            left += 1

        # get the max window size??
        answer = max(answer, right - left + 1)

    return answer
