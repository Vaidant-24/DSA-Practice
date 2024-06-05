m = 69
n = 4

ans = m ** 1/n
newAns = abs(round(ans) - ans)
if newAns < 1e-10:
    print(n)
else:
    print('-1')