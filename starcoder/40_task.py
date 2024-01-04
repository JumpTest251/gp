def max_profit(prices):
    """
    You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
    On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
    Find and return the maximum profit you can achieve.

    Example:
    [7,1,5,3,6,4] = 7
    [1,2,3,4,5] = 4
    """
    # O(n) time | O(1) space
    maxProfit = 0
    minPrice = float("inf")
    for price in prices:
        minPrice = min(minPrice, price)
        profit = price - minPrice
        maxProfit = max(maxProfit, profit)
    return maxProfit
    