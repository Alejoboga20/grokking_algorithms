test_array = [2, 2, 3413, 32, 423131, 4124, 4, 4124, 4, 0, 12, 23, 415789765, 554]

def quicksort(array = []):
  """Sort array using quicksort"""
  if len(array) < 2:
    return array
  else:
    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]

    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort(test_array))