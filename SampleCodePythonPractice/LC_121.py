def maxProfit(prices):
    buy_price = prices[0]
    profit = 0
    for price in prices:
        if buy_price > price:
            buy_price = price

        profit = max(profit, price - buy_price)

    return profit


if __name__ == '__main__':
    prices_test1 = [7,1,5,3,6,4]
    print(maxProfit(prices_test1))
    prices_test2 = [7, 6, 4, 3, 1]
    print(maxProfit(prices_test2))

