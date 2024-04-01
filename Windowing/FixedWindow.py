# fixed window to track data
def f(arr: list[int], k: int) -> int
    curr = some data to track window

    # build the first window
    for (int i = 0; i < k; i++):
        do something with curr or other vars to build first window

    # answer variable
    ans = answer var, usually equal to curr here or some property
    for (int i = k; i < arr.len; i++):
        add arr[i] to window
        remove arr[i-k] from window
        update ans

    return ans


