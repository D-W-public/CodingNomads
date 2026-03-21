distance = float(input("How far do you want to drive?: "))
usage = float(input("How many liters does your vehicle burn per km: "))
price = float(input("Whats the current fuel price per liter?: "))

result = (distance / usage) * price

print(f"Your trip will cost you {result} moneys.")
