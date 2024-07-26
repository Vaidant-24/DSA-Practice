def help(divident, divisor):
    x = 0
    while ((divisor<<x) <= divident):
        x += 1
    return x - 1

def divide(divident, divisor):
    if (divisor == 0):
        raise ZeroDivisionError("Divisor cannot be zero")
    
    sign = -1 if ((divident < 0) ^  (divisor < 0)) else 1
    
    divident = abs(divident)
    divisor = abs(divisor)
    
    if divident < divisor:
        return 0
    
    cnt = help(divident, divisor)
    
    rem = divident - (divisor << cnt)
    
    ans = (1 << cnt)
    ans += divide(rem, divisor)
    
    ans = sign * ans
    
    if ans > 2**31 - 1:
        return 2**31 - 1
    elif ans < -2**31:
        return -2**31
    else:
        return ans

print(divide(42, 3))  # Output: 7
