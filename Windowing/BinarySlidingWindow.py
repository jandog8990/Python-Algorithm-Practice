# find the longest substrings of all 1's
def binary_window(nums):
    left = 0
    window = 0  # total window length of 1s 
    curr = 0    # running count of "0"s

    N = len(nums) 
    for right in range(0, N):
        if nums[right] == "0":
            curr += 1

        # loop for moving left ptr
        while curr > 1:
            if nums[left] == "0":
                # rm if we have more than one "0"
                curr -= 1
            left += 1

        window = max(window, right-left+1)

    return window

s = "1101100111"
res = binary_window(s)
print("Result:")
print(res)
