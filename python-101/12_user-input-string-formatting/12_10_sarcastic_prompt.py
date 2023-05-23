# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.
st_1 = input("Please input a string here : ")
result = ""

odd=True
for c in st_1:
  if odd:
    result = result + c.upper()
  else:
    result = result + c.lower()
  odd = not odd
print(result)