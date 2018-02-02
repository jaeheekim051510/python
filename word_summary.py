
sentence = raw_input('Please enter a sentence: ')

i = sentence
word_in_sentence = i.split(' ')
print word_in_sentence
dic = {}
for j in word_in_sentence:
    dic[j] = j.count(j)
print dic