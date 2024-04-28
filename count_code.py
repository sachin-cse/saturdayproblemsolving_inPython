
# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.


# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2

def count_code(string):
    count = 0
    index = 0
    while index < len(string):
        if string[index:index+2] == 'co' and index + 3 < len(string) and string[index+3] == 'e':
            count += 1
            index += 4
        else:
            index += 1
    return count