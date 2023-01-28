# 참고: https://github.com/acidsound/korean_wordlist

def dict_check(word):
    if word in dict_word:
        return True
    else:
        return False

with open('.\data\wordslistUnique.txt', 'r', encoding='utf-8') as f:
    dict_word = f.readlines()
dict_word = [line.rstrip('\n') for line in dict_word]