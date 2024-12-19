# Ex 2 Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the Price?: "))
quantity = int(input("How many/much of the item would you like to buy?: "))

total = price * quantity

print(f"you have bought {quantity} x {item}/s")
print(f"your bill will be ${total}")
