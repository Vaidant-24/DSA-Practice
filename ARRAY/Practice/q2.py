# Find the missing number 

ls = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]


def find_missing(ls):
    sum1 = sum(ls)
    n = len(ls) + 1
    sum2 = n * (n+1)/2
    return (sum2 - sum1)

print("{} is missing element".format(find_missing(ls)))