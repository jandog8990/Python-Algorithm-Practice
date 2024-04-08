# compare strings with backspace chars
def backspaceRemove(s: str, t: str) -> bool:
    def build(s):
        st = []
        for c in s:
            if st and c == "#":
                st.pop()
            else:
                st.append(c)
        s1 = "".join(st)
        print(f"new s = {s1}") 
        return s1 

    return build(s) == build(t)

s = "ab#c"
t = "ad#c"
res = backspaceRemove(s,t)
print(f"Res = {res}")
