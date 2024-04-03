# check if array of strings contains anagrams
# re-ordered strings that spell diff things
from collections import defaultdict
def findAnagrams(strs: list[str]) -> list[str]:
    anagrams = defaultdict(list) 
    for s in strs:
        key = "".join(sorted(s)) 
        anagrams[key].append(s)

    return anagrams.values()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = findAnagrams(strs)
print("Result:")
print(res)
print("\n")
