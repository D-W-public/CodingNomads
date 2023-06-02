# Write a function named `stats()` that takes in a list of numbers
# and finds the maximum, minimum, average and sum of the numbers.
# Print these values to the console you call the function.

example_list = [1, 2, 3, 4, 5, 6, 7]


def stats(numbers):

# define the function here
  """Takes alist of numbers and finds the smallest and largest number.
    Also calculates the sum of the list

    Args:
      Takes lists

    Returns:
      f-string with results
    """
  largest = max(numbers)
  smallest = min(numbers)
  sum_ = sum(numbers)

  result = f"""
  The largest number is  : {largest}
  The smallest number is : {smallest}
  The sum is             : {sum_}"""
  
  return result


# call the function below here

print(stats(example_list))