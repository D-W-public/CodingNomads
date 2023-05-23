#needed input
# distance , l/km, price/liter
distance = float(input("How far is your journey?: "))
usage = float(input("How efficient is your car? "))
price = float(input("Current fuel price? "))

result = distance*usage*price

print(f"Your {distance}km journey will cost {result}€")