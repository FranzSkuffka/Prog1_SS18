def is_sorted(l: list) -> bool:
  """
  Check if a list is sorted
  l: list
  """
  return sorted(l) == l

def is_sorted_one(l: list) -> bool:
  """
  Check if a list is sorted
  l: list
  """
  if len(l) > 1:
    lower = l[0]
    for i in l:
      if lower > i:
        return False
      lower = i
  return True

def is_sorted_two(l: list) -> bool:
  """
  Check if a list is sorted
  l: list
  """
  if len(l) > 1:
    lower = l[0]
    for i in l:
      if i < lower:
        return False
      lower = i
  return True
