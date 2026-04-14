import csv

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 300
}

total_investment = 0

# Header sirf ek baar likho
with open("result.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Stock", "Quantity", "Price", "Total"])

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        price = stock_prices[stock_name]
        total = price * quantity
        total_investment += total

        print(f"{stock_name} total: {total}")

        # Append mode use karo
        with open("result.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([stock_name, quantity, price, total])

print("Total Investment:", total_investment)