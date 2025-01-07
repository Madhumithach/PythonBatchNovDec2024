print("SuperMarket".center(40))
print("Srinivasa Kirana Store".center(40))
print("B.N Reddy".center(40))
print("+91 5831936811".center(40))
print(''.ljust(40, "-"))
cashier_label = "Cashier:"
cashier_value = "#1"
manager_label = "Manager:"
manager_name = "Harry"
total_width = 40
line1 = f"{cashier_label:<20}{cashier_value:>{total_width - 20}}"
line2 = f"{manager_label:<20}{manager_name:>{total_width - 20}}"
print(line1)
print(line2)
print(''.ljust(40, "-"))
Name = "Name"
QTY = "QTY"
Price = "Price"
print(f"{Name:<20}{QTY:<10}{Price:>10}")
products = [
    {"name": "Chocolate", "qty": 5, "price": 30},
    {"name": "Biscuits", "qty": 3, "price": 45},
    {"name": "Milk", "qty": 2, "price": 50},
    {"name": "Rice Bag", "qty": 1, "price": 1200},
]
for product in products:
    name = product["name"]
    qty = product["qty"]
    price = product["price"]
    print(f"{name:<20}{qty:<10}{price:>10}")
print(''.ljust(40, "-"))
subtotal = sum(product["qty"] * product["price"] for product in products)
cash = 2000
change = cash - subtotal

print(f"{'Sub Total:':<30}{subtotal:>10}")
print(f"{'CASH:':<30}{cash:>10}")
print(f"{'CHANGE:':<30}{change:>10}")

# Footer
print(''.ljust(40, "-"))
print("THANK YOU!".center(40))
print("Glad to see you again!".center(40))
