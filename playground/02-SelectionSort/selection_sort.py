test_array = [20, 23, 33, 4, 5, 1, 3, 1, 3, 0, -1]

def find_smallest(array):
  """Return the index for the smallest number in array"""
  smallest = array[0]
  smallest_index = 0

  for i in range(1, len(array)):
    if array[i] < smallest:
      smallest = array[i]
      smallest_index = i
  return smallest_index

assert find_smallest(test_array) == 10

def selection_sort(array):
  """Sort Array finding the smallest"""
  sorted_array = []
  for i in range(0, len(array)):
    smallest_index = find_smallest(array)
    smallest_number = array.pop(smallest_index)
    sorted_array.append(smallest_number)
  return sorted_array

assert selection_sort(test_array) == [-1, 0, 1, 1, 3, 3, 4, 5, 20, 23, 33]
