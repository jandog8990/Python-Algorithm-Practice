from collections import defaultdict
# find length of shortest subarray that contains
# at least one duplicate -> if no dups ret -1
def minConsecutiveCards(cards: list[int]) -> int:
    card_map = defaultdict(list)
    for i,card in enumerate(cards):
        card_map[card].append(i)
    print("Card map:")
    print(card_map)
    print("\n")

    dist = float("inf")
    for key in card_map:
        idxs = card_map[key]
        for i in range(len(idxs)-1):
            curr_dist = idxs[i+1] - idxs[i] + 1  
            print(f"idxs[{i+1}] = {idxs[i+1]}")
            print(f"idxs[{i}] = {idxs[i]}")
            print(f"curr_dist = {curr_dist}") 
            dist = min(dist, curr_dist) 
            print(f"min dist = {dist}")
            print("\n")

    return dist if dist < float("inf") else -1

# this version doesn't store all indices only the current
def minCardPickup(cards: list[int]) -> int:
    card_map = defaultdict(int)
    dist = float("inf")
    for i in range(len(cards)):
        # check if current card is in the dict and get
        # the previous index it was encountered
        if cards[i] in card_map:
            dist = min(dist, i - card_map[cards[i]] + 1)

        # insert the current card in the index
        card_map[cards[i]] = i

    return dist if dist < float("inf") else -1
    

cards = [1,2,6,2,1]
res1 = minConsecutiveCards(cards)
print(f"Res 1 = {res1}")
res2 = minCardPickup(cards)
print(f"Res 2 = {res2}")

