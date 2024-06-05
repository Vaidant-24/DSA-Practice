# Buy and sell stocks:-

prices = [7,5,3,2,1]

def maxProfit(prices):
    maxProf = 0
    minimum = float('inf')
    n = len(prices)
    for i in range(n):
        if minimum > prices[i]:
            minimum = prices[i]
        
        diff = prices[i] - minimum
        maxProf = max(diff, maxProf)
    return maxProf
print(maxProfit(prices))