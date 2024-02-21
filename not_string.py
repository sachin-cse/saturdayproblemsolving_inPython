# Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged. 

def not_string(str):
  str1 = str.split()
  
  if str1[0] == 'not':
    return str
  return 'not'+ ' ' + str
