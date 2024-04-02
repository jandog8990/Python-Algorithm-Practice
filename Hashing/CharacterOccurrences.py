from collections import defaultdict

# find number of occurrences of unique
# characters and make sure they occur the same
def findOccurrences(s: str) -> bool:
    counts = defaultdict(int)
    for c in s:
        counts[c] += 1

    # count the unique values
    cset = len(set(counts.values()))

    print("Unique values:")
    print(counts.values())
    print("\n")

    return cset == 1

from collections import Counter
def findOccurrenceCounter(s: str) -> bool:
    return len(set(Counter(s).values())) == 1

s = "abacbc"
res = findOccurrences(s)
print(f"Res = {res}")

res2 = findOccurrenceCounter(s)
print(f"Res = {res2}")

