def commonLetters(str1, str2):
    l = []
    for i in str1:
        for j in str2:
            if i==j:
                l.append(i)
    return set(l)

print(commonLetters('Naina', 'Reena'))