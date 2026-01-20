stock_levels = [15, 3, 0, 22, 8, 1]

for stock in stock_levels:
    if stock == 0:
        print("Out of Stock")
    elif 1 <= stock <= 5:
        print("Restock Immediately")