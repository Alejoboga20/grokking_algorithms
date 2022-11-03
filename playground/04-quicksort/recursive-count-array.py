def recursive_count(array = []):
  """Return the number of items in array using recursion"""
  count = 1
  #Base case
  if len(array) == 0:
    return 0

  # Recursive Case
  return 1 + recursive_count(array[1:])

assert recursive_count([1, 1, 1]) == 3
assert recursive_count([1]) == 1
assert recursive_count([]) == 0