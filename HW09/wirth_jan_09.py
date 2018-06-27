import re

def max_count(counts: dict) -> str:
  """
  Take a count dict and return the most frequently seen string
  """
  max = (None, 0)
  for key, val in counts.items():
    if val > max[1]: max = (key, val)
  return max[0]

def counts(items: [str]) -> dict:
  """
  Take a list of strings and return a dict with occurence counts for each string in the list
  Unseen strings are not included in the results.
  """
  res = {}
  for item in items:
    try:
      if res[item]: res[item] = res[item] + 1
    except KeyError:
      res[item] = 1
  return res

def intersect(a: set, b: set) -> set:
  """
  return intersection between two sets
  """
  return a.intersection(b)

def my_sort(l: [], rev = False) -> []:
  """
  sort, use 'rev' param to reverse result
  """
  if rev:
    return list(reversed(sorted(l)))
  else:
    return list(sorted(l))

class StringTooLong(Exception):
  """
  Custom error for strings that are too long
  """
  def __init(self, message, errors):
    super(Exception, self).__init__(message)
    self.errors = errors

def field():
  """
  new chess playing field
  a-g x 1-8
  """
  f = {}
  for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
    f[letter] = [ None for i in range(8)]
  return f

def naive_diminuitive(word):
  """
  take a word, turn the last of 'a', 'o' or 'u' into its umlaut equivalent
  and add 'chen' to the end of the string
  """
  umlaut_map = { 'a': 'ä', 'o': 'ö', 'u': 'ü' }
  res = ""
  rev = "".join(reversed(word))
  pos = len(word) - 1 - re.search("[aou]", rev).start()
  uml = umlaut_map[word[pos]]
  return word[0: pos] + uml + word[pos + 1:] + 'chen'

if __name__ == '__main__':

    print(counts(["Arthur", "Arthur", "Bedevere"]))
    print(max_count(counts(["Arthur", "Arthur", "Bedevere"])))

    print(my_sort([2, 34, 5, 32, 2, 34, 234, 2, 5, 234, 1]))
    print(my_sort([2, 34, 5, 32, 2, 34, 234, 2, 5, 234, 1], rev=True))

    print(intersect(set([1,2,3]), set([2,3,4])))

    try:
      raise StringTooLong("aiaiaiiaia")
    except StringTooLong:
      print("ooops string too long")

    currentField = field()
    currentField['b'][2] = 'Black Knight'
    currentField['g'][2] = 'White Pawn'
    currentField['g'][3] = 'White Pawn'
    currentField['g'][5] = 'Black Pawn'
    currentField['h'][5] = 'Black Pawn'
    currentField['e'][5] = 'Black King'
    currentField['b'][5] = 'White Pawn'
    currentField['c'][6] = 'White King'
    currentField['d'][7] = 'White Knight'

    print(naive_diminuitive("boiiiiii"))
    print(naive_diminuitive("amanakoi"))
    print(naive_diminuitive("Ungeheuer"))
