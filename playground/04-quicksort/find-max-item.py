def max_number(array = []):
  """Find the biggest number in array using recursion"""
  if len(array) == 0:
    return None

  if len(array) == 1:
    return array[0]

  sub_max = max_number(array[1:])
  return array[0] if array[0] > sub_max else sub_max