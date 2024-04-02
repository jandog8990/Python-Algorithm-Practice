from collections import defaultdict
# find the longest substring in string that 
# contains at most K unique chars
def findLongestSubstring(s: str, k: int) -> int:
    counts = defaultdict(int)
    left = 0
    ans = 0

    # first traverse to the right and insert
    # char counts from string into map
    for right in range(len(s)):
        counts[s[right]] += 1
        # check that we have at most k unique keys 
        while len(counts) > k:
            # remove left indices until 0
            counts[s[left]] -= 1
            if counts[s[left]] == 0:
                del counts[s[left]]
            left += 1

        # find the max window size using 
        # current right and left indices
        ans = max(ans, right-left+1)

    return ans

s = "eceba"
k = 2
res = findLongestSubstring(s, k)
print(f"Res = {res}")
