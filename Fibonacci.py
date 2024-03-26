# fibonacci recursive function
function F(n):
    if n <= 1:
        # F(0) = 0
        # F(1) = 1
        return n

    oneBack = F(n-1)
    twoBack = F(n-2)
    return oneBack + twoBack
