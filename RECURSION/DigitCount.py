def digitCount(n):
    if n < 10:
        return 1
    return digitCount(n//10) + 1

print(digitCount(1))