# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

target = int(input("Enter a number between 0 and 1,000,000,000: "))
low = 0
high = 1000000000

while low <= high:
    mid = (low + high) // 2

    if mid == target:
        print(f"Found the number: {mid}")
        break
    elif mid < target:
        low = mid + 1
    else:
        high = mid - 1
