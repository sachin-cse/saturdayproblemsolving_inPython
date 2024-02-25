
# Given a non-empty string like "Code" return a string like "CCoCodCode".


def string_splosion(str):
  string = ''
  str_length = len(str)
  for i in range(str_length):
    for j in range(0,i+1):
      string+=str[j]
  return string


string_splosion('Code') # 'CCoCodCode'
string_splosion('abc') # 'aababc'
string_splosion('ab') # 'aab'