def binary_search (list = [], item = 0):
  low = 0
  high = len(list) - 1

  while low <= high:
    mid = ( low + high ) // 2
    guess = list[mid]

    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else:
      low = mid + 1

  return None

ordered_list = [0, 3, 4, 5, 6, 7, 8, 8, 11, 12, 13, 15, 16]

print('Index of 11 is: ', binary_search(ordered_list, 11))