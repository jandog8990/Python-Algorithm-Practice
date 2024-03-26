def reverse_string(s):
    # this is easy just two pointer tech 
    s = list(s) 
    i = 0
    j = len(s) - 1
    while i < j:
        left = s[i]
        right = s[j]
        s[i] = right
        s[j] = left
        i += 1
        j -= 1

    return s

s = "hello"
res = reverse_string(s)
print(res)
