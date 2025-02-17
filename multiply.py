def multiply(x, y):
    """
    Input: two integers, x and y, where y >= 0
    Output: Their product
    
    """
    if y == 0:
        return 0
    z = multiply(x, y // 2) # y // 2 is floor division
    if y % 2 == 0:
        return 2*z
    else:
        return x + 2*z
    
print(multiply(3, 5))