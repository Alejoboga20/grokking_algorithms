test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def recursive_array_sum(array = []):

  if len(array) == 0:
    return 0

  return array[0] + recursive_array_sum(array[1:])

assert recursive_array_sum() == 0
assert recursive_array_sum(test_array) == 55
assert recursive_array_sum([1]) == 1