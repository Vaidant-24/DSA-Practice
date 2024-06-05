def fun(n):
    if n == 1:
        return 1
    return fun(n-1) + n

print(fun(5))