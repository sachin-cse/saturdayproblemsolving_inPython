# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

def string_bits(str):
  string = ''
  str_length = len(str)
  for i in range(str_length):
    if(i%2 == 0):
      string+=str[i]
  return string

string_bits('Hello') # 'Hlo'
string_bits('Hi') # 'H'
string_bits('Heeololeo') # 'Hello'