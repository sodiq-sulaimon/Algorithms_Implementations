def divide(x, y):
    """
    Input: two integers, x and y, where y >= 1
    Output: The quotient and remainder of x divided by y
    
    """
    if x == 0:
        return (0, 0)
    
    (q, r) = divide(x // 2, y)
    q = 2 * q
    r = 2 * r

    if x % 2 == 1:
        r += 1
    if r >= y:
        r -= y  
        q += 1
    
    return (q, r)
    
print(divide(20, 3))