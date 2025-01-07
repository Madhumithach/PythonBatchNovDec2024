print("SuperMarket".center(30))
print("Srinivasa Kirana Store".center(30))
print("B.N Reddy".center(30))
print("+91 5831936811".center(30))
print(''.ljust(30,"-"))
print(''.rjust(30,"-"))
cashier_label = "cashier:"
cashier_value = "#1"
manager_label = "Manager:"
manager_name = "Harry"
total_width = 40
line1 = f"{cashier_label:<20}{cashier_value:>{total_width - 20}}"
line2 = f"{manager_label:<20}{manager_name:>{total_width - 20}}"
print(line1)
print(line2)
print(''.ljust(30,"-"))
print(''.rjust(30,"-"))
Name="Name"
QTY="QTY"
Price="Price"
print(f"{Name:<15}{QTY.center(4)}{Price:>{total_width-20}}")
product1="chocolate"
qty1=5
price1=30
print(f"{product1:<15}{qty1.center(4)}{price1:>{total_width-20}}")
