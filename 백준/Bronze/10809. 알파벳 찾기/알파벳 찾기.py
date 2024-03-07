alphabet_num = []
for i in range(0,26):
    alphabet_num.append(-1)

#ord(i) = 유니코드
#ord(a) = 97
#ord(a)-97 = 0

word = list(input())
for i in range(0,len(word)):
    word[i] = ord(word[i])-97
    if (alphabet_num[word[i]] == -1) :
        alphabet_num[word[i]] = i

print(' '.join(str(e) for e in alphabet_num))