# find the two sum indices using hashmaps
def twoSumHash(nums: list[int], target: int) -> list[int]:
    dic = {}
    for i in range(len(nums)):
        num = nums[i]
        comp = target - num
        if comp in dic: # check for elem is O(1)
            # if we just wanted boolean then use Set 
            return [i, dic[comp]]

        dic[num] = i

    return [-1, -1]

