"""
corpus analysis utils
"""

def get_word_count(text: str, word: str) -> int:
  """
  count occurences of a token in a string
  tokens are delimited by whitespace
  """
  matches = list(filter(lambda token: token == word, text.split()))
  return len(matches)
