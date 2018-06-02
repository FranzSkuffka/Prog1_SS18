"""
interactive corpus analysis utilities
"""
import analyze
import file_handler

def get_word_count_from_user(word = None) -> dict:
  """
  Count a user-defined word in the text of dummy_file.txt
  """
  # for testing
  if word == None:
    word = input("Which word? ")
  count =  analyze.get_word_count(file_handler.get_text('dummy_file.txt'), word)
  # Raise an error when nothing was found
  if count == 0:
    raise LookupError(word + " not found in the text")
  res = {
    word: count
  }
  return res

if __name__ == "__main__":
  get_word_count_from_user()
