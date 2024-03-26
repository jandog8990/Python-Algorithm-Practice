def find_substring(s, t):
    # where s is the string
    # and t is the target (substring)
    j = 0
    isSub = False
    for i in range(len(s)):
        if t[j] == s[i]:
            # we found a letter in substring
            # increase the second pointer j
            j += 1

    if j != len(t):
        return False
    else:
        return True

t = "aed"
s = "abcde"
res = find_substring(s, t)
print(f"Result = {res}")
