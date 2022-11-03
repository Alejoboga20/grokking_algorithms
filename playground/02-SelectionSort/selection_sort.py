def find_smallest(array):
  """Return the index for the smallest number in array"""
  smallest = array[0]
  smallest_index = 0

  for i in range(1, len(array)):
    if array[i] < smallest:
      smallest = array[i]
      smallest_index = i
  return smallest_index

test_array = [20, 23, 33, 4, 5, 1, 3, 1, 3, 0]
assert find_smallest(test_array) == 9