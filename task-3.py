def average_closing_price(stock_data, symbol):
    total_price = 0
    count = 0
    for stock_symbol, _, closing_price in stock_data:
        if stock_symbol == symbol:
            total_price += closing_price
            count += 1
    if count > 0:
        average_price = total_price / count
        return average_price
    else:
        return "No data for the specified stock symbol"


stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
]

print(average_closing_price(stock_data, "AAPL"))  
print(average_closing_price(stock_data, "GOOGL"))