# python买卖股票的最佳时机

"""
贪心算法
"""


def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    profit = 0
    for day in range(len(prices)-1):
        differ = prices[day+1] - prices[day]
        if differ > 0:
            profit += differ
    return profit


"""
动态规划
"""


def maxProfit2(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    minelement = prices[0]
    profit = 0
    for i in range(len(prices)):
        minelement = min(prices[i], minelement)

        profit += differ
    return profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
