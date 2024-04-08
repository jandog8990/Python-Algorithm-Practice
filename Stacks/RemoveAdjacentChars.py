# remove adjacent characters in a given string
def removeAdj(s: str) -> str:
    st = []
    for c in s:
        if st and st[-1] == c:
            st.pop()
        else:
            st.append(c)

    return st

s = "abbaca"
res = removeAdj(s)
print(f"Result = {res}")
