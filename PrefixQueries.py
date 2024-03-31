# use prefix sums to solve subarray problems
def answer_queries(nums, queries, limit):
    # create the prefix array containing sums 
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i] + prefix[-1])
    print("Prefix:")
    print(prefix)
    print("\n")

    # create the sums using the algorithm
    # prefix[j] - prefix[i] + nums[i] or prefix[j] - prefix[i-1]
    subsum = [] 
    boosum = [] 
    for x,y in queries:
        sums = prefix[y] - prefix[x] + nums[x] 
        subsum.append(sums)
        boosum.append(sums < limit) 
   
    # output from the boolean and sums arr
    print("Output:")
    print(subsum)
    print(boosum)
    print("\n")

nums = [1,6,3,2,7,2]
queries = [[0,3], [2,5], [2,4]]
answer_queries(nums, queries, 13)

