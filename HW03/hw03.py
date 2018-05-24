"""
An interactive and personalized star generator 
"""

def main():
  """
  the main routine. Welcome and say goodbye to the user. Call the actual star generator
  """
  username = _input("What is your name:")
  _print("Hello " + username)
  interactive_star_generator()
  _print("Goodbye " + username)

def interactive_star_generator():
  """
  A recursive function for interactively generating stars for as long as we want
  """
  print_stars(_input("How many "))
  if _input("Wanna more? ")[0].lower() == "y":
    interactive_star_generator()

def print_stars(count_str: str):
  """
  try to parse a string input as number and print the according number of stars
  """
  try:
    _print("*" * int(count_str))
  except ValueError:
    _print('Sorry, I did not understand')


def _input(msg: str):
  """
  a wrapper for `input`
  """
  return input(msg)

def _print(msg: str):
  """
  a wrapper for `print`
  """
  return print(msg)

def main_2():
  """
  A headless (non-personalizesd star generator)
  """
  interactive_star_generator()

if __name__ == "__main__":
  print('main')
  main()
