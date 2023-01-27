import re
# 참고: https://github.com/neotune/python-korean-handler

# 유니코드 한글 시작 : 44032, 끝 : 55199
BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28

# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
D_CHO = [1, 4, 8, 10, 13]

# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
S_JUNG = [0, 2, 4, 6, 8, 12, 13, 17, 18, 20]
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
S_JONG = [0, 1, 4, 7, 8, 16, 17, 19, 21, 22, 23, 24, 25, 26, 27]

def spliter(word):
    words = []
    if re.search('[가-힣]{2}', word) and len(word) < 4:
        for chs in word:
            chs_code = ord(chs) - BASE_CODE
            ch1 = chs_code//CHOSUNG
            if ch1 in D_CHO:
                words.append(CHOSUNG_LIST[ch1-1])
                words.append(CHOSUNG_LIST[ch1-1])
            else:
                words.append(CHOSUNG_LIST[ch1])
            ch2 = (chs_code - CHOSUNG*ch1)//JUNGSUNG
            if ch2 in S_JUNG:
                words.append(JUNGSUNG_LIST[ch2])
            else:
                if JUNGSUNG_LIST[ch2] == 'ㅐ':
                    words.append('ㅏ')
                    words.append('ㅣ')
                elif JUNGSUNG_LIST[ch2] == 'ㅒ':
                    words.append('ㅑ')
                    words.append('ㅣ')
                elif JUNGSUNG_LIST[ch2] == 'ㅔ':
                    words.append('ㅓ')
                    words.append('ㅣ')
                elif JUNGSUNG_LIST[ch2] == 'ㅖ':
                    words.append('ㅕ')
                    words.append('ㅣ')
                elif JUNGSUNG_LIST[ch2] == 'ㅘ':
                    words.append('ㅗ')
                    words.append('ㅏ')
                elif JUNGSUNG_LIST[ch2] == 'ㅙ':
                    words.append('ㅗ')
                    words.append('ㅐ')
                elif JUNGSUNG_LIST[ch2] == 'ㅚ':
                    words.append('ㅗ')
                    words.append('ㅣ')
                elif JUNGSUNG_LIST[ch2] == 'ㅝ':
                    words.append('ㅜ')
                    words.append('ㅓ')
                elif JUNGSUNG_LIST[ch2] == 'ㅞ':
                    words.append('ㅜ')
                    words.append('ㅔ')
                elif JUNGSUNG_LIST[ch2] == 'ㅟ':
                    words.append('ㅜ')
                    words.append('ㅣ')
                elif JUNGSUNG_LIST[ch2] == 'ㅢ':
                    words.append('ㅡ')
                    words.append('ㅣ')
            ch3 = chs_code - CHOSUNG*ch1 - JUNGSUNG*ch2
            if ch3 in S_JONG:
                words.append(JONGSUNG_LIST[ch3])
            elif JONGSUNG_LIST[ch3] == 'ㄲ':
                words.append('ㄱ')
                words.append('ㄱ')
            elif JONGSUNG_LIST[ch3] == 'ㄳ':
                words.append('ㄱ')
                words.append('ㅅ')
            elif JONGSUNG_LIST[ch3] == 'ㄵ':
                words.append('ㄴ')
                words.append('ㅈ')
            elif JONGSUNG_LIST[ch3] == 'ㄶ':
                words.append('ㄴ')
                words.append('ㅎ')
            elif JONGSUNG_LIST[ch3] == 'ㄺ':
                words.append('ㄹ')
                words.append('ㄱ')
            elif JONGSUNG_LIST[ch3] == 'ㄻ':
                words.append('ㄹ')
                words.append('ㅁ')
            elif JONGSUNG_LIST[ch3] == 'ㄼ':
                words.append('ㄹ')
                words.append('ㅂ')
            elif JONGSUNG_LIST[ch3] == 'ㄽ':
                words.append('ㄹ')
                words.append('ㅅ')
            elif JONGSUNG_LIST[ch3] == 'ㄾ':
                words.append('ㄹ')
                words.append('ㅌ')
            elif JONGSUNG_LIST[ch3] == 'ㄿ':
                words.append('ㄹ')
                words.append('ㅍ')
            elif JONGSUNG_LIST[ch3] == 'ㅀ':
                words.append('ㄹ')
                words.append('ㅎ')
            elif JONGSUNG_LIST[ch3] == 'ㅄ':
                words.append('ㅂ')
                words.append('ㅅ')
            elif JONGSUNG_LIST[ch3] == 'ㅆ':
                words.append('ㅅ')
                words.append('ㅅ')
        words = [i for i in words if i != ' ']
        if len(words) != 6:
            print(f'입력길이({len(words)})', *words)
            raise ValueError
        return words
    else:
        raise ValueError

def word_split(word):
    try:
        return spliter(word)
    except:
        print('잘못된 입력!')
        return False

if __name__ == "__main__":
    try:
        words = word_split('새싹')
    except ValueError:
        print('잘못된 입력!')
