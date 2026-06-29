stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150
}

total = 0

while True:
    name = input("Enter Stock Name (or done): ")

    if name == "done":
        break

    qty = int(input("Enter Quantity: "))

    if name in stocks:
        total = total + stocks[name] * qty
    else:
        print("Stock Not Found")

print("Total Investment =", total)