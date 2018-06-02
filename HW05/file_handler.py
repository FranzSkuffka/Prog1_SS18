"""
utilities for reading contents of file
"""

def get_text(filepath):
  """
  read a file by path and return its content as multiline string
  """
  with open(filepath) as f: return f.read()

def get_lines(filepath):
  """
  read a file by path and return its content as list of lines
  """
  return get_text(filepath).splitlines()
