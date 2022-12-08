import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

words = []

for _ in range(2500000):
    word_len = random.randint(3,15)
    word = ''
    for i in range(word_len):
        # print(word, word_len)
        word += random.choice(letters)
    words.append(word)

with open('input2500k.txt', 'w') as f:
    f.write('mercy' + '\n')
    for s in words:
        f.write(str(s) + '\n')