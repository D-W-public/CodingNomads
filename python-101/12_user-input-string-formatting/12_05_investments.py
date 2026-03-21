# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

capital = float(input("Please enter how much you want to invest: "))
intrest_rate = float(input("Please enter the p.a. interest: "))
time = int(input("How long to you want to invest?: "))

intrest = intrest_rate / 100

future_value = capital * (1 + intrest) ** time

print(f"After {time} years you will have {round(future_value, 2)} moneys.")

