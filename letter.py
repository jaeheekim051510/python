
letter = (raw_input('Please enter a word: '))

i = letter
# print i
# count = {x:i.count(x) for x in i}
# print count

# str.count()

# splitletter = list(i)
# print splitletter
dic = {}
for j in letter:
    dic[j] = letter.count(j)
print dic

# body.count(elements in body)