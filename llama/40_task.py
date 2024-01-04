def max_profit(prices):
    """
    You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
    On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
    Find and return the maximum profit you can achieve.

    Example:
    [7,1,5,3,6,4] = 7
    [1,2,3,4,5] = 4
    """
    # Time: O(n)
    # Space: O(1)
    # DP
    if not prices:
        return 0
    profit = 0
    min_price = prices[0]
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > profit:
            profit = price - min_price
    return profit

    