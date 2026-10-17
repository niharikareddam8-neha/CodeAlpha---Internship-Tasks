print("📈 Stock Portfolio Tracker")

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 400
}

stock = input("Enter stock name (AAPL/TSLA/GOOGL/MSFT): ").upper()
quantity = int(input("Enter quantity: "))

if stock in stock_prices:
    total = stock_prices[stock] * quantity
    print("Stock Price:", stock_prices[stock])
    print("Quantity:", quantity)
    print("Total Investment:", total)
else:
    print("Stock not available.")