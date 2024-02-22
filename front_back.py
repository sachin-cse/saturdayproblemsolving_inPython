# Given a string, return a new string where the first and last chars have been exchanged.
def front_back(str):
  if len(str) <= 1:
    return str
  first = str[0]
  last = str[-1]
  return last + str[1:-1] + first