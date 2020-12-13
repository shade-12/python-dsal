import math

def buy_and_sell_stock_once(prices):
    buy, sell = 0, 0
    max_profit = -math.inf
    for i in range(len(prices)):
        profit = prices[sell] - prices[buy]
        max_profit = max(max_profit, profit)
        if prices[i] < prices[buy]:
            buy = i
        sell += 1

    return max_profit