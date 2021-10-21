price=0.0
Price_list = [10.00,12.00,15.00,10.00,25.00,45.00,50.00,25.00,10.00,12.00]
FT = int(input("Enter food type"))
while FT != -1:
 IQ = int(input("Enter item quantity:"))
 price = price+Price_list[FT]*IQ
 FT = int(input("Enter food type:"))
print(price)
