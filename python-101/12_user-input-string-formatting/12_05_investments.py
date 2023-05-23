# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

#collect data
a_0 = float(input("How much would you like to invest?: "))

r = float(input("How much is the interest rate?: "))

t = float(input("For how long will you be investing? "))

#fromula

fv = a_0*((1)+(0.01*r))**t

print((round(fv,2)))