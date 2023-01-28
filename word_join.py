from collections import deque

# 유니코드 한글 시작 : 44032, 끝 : 55199
BASE_CODE, CHOSUNG, JUNGSUNG = 44032, 588, 28

# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
D_CHO = {(0, 0):1, (3, 3):4, (7, 7):8, (9, 9):10, (12, 12):13}
# D_CHO = [1, 4, 8, 10, 13]

# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
D_JUNG = {(0, 20):1, (2, 20):3, (4, 20):5, (6, 20):7, (8, 0):9, (8, 1):10, (8, 20):11, (13, 4):14, (13, 5):15, (13, 20):16, (18, 20):19}
# S_JUNG = [0, 2, 4, 6, 8, 12, 13, 17, 18, 20]

# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
D_JONG = {(1, 1):2, (1, 19):3, (5, 22):6, (5, 27):7, (8, 1):9, (8, 16):10, (8, 17):11, (8, 19):20, (8, 25):13, (8, 26):14, (8, 27):15, (17, 19):18, (19, 19):20}
# S_JONG = [0, 1, 4, 7, 8, 16, 17, 19, 21, 22, 23, 24, 25, 26, 27]

def joiner(lst):
    try:
        rst = []
        deq = deque(lst)
        while True:
            tmp = []
            if len(deq) == 0:
                break
            tmp.append(deq.popleft())
            tmp.append(deq.popleft())
            while len(deq) != 0:
                if deq[0] in JUNGSUNG_LIST:
                        tmp.append(deq.popleft())
                try:
                    if deq[1] in JUNGSUNG_LIST:
                        break
                except IndexError:
                    tmp.append(deq.popleft())
                    break
                tmp.append(deq.popleft())
            # print(tmp)
            rst.append(jamo2char(tmp))
        rst = ''.join(i for i in rst)
        return rst
    except:
        return False

def jamo2char(lst):
    # 쌍자음 확인
    if lst[1] in CHOSUNG_LIST:
        lst[0] = CHOSUNG_LIST[D_CHO[(CHOSUNG_LIST.index(lst[0]), CHOSUNG_LIST.index(lst[1]))]]
        lst.pop(1)

    # 모음 합성
    if len(lst) == 4:
        if lst[3] in JUNGSUNG_LIST:
            lst[2] = JUNGSUNG_LIST[D_JUNG[(JUNGSUNG_LIST.index(lst[2]), JUNGSUNG_LIST.index(lst[3]))]]
            lst.pop(3)
            lst[1] = JUNGSUNG_LIST[D_JUNG[(JUNGSUNG_LIST.index(lst[1]), JUNGSUNG_LIST.index(lst[2]))]]
            lst.pop(2)
        else:
            lst[1] = JUNGSUNG_LIST[D_JUNG[(JUNGSUNG_LIST.index(lst[1]), JUNGSUNG_LIST.index(lst[2]))]]
            lst.pop(2)
    if len(lst) == 3:
        if lst[2] in JUNGSUNG_LIST:
            lst[1] = JUNGSUNG_LIST[D_JUNG[(JUNGSUNG_LIST.index(lst[1]), JUNGSUNG_LIST.index(lst[2]))]]
            lst.pop(2)
    
    # 종성 처리
    if len(lst) == 4:
        lst[2] = JONGSUNG_LIST[D_JONG[(JONGSUNG_LIST.index(lst[2]), JONGSUNG_LIST.index(lst[3]))]]
        jong = JONGSUNG_LIST.index(lst[2])
    elif len(lst) == 3:
        jong = JONGSUNG_LIST.index(lst[2])
    else:
        jong = 0
    
    char_num = BASE_CODE + (CHOSUNG_LIST.index(lst[0])*21 + JUNGSUNG_LIST.index(lst[1]))*28 + jong
    return chr(char_num)

if __name__ == "__main__":
    words = joiner('ㅇㅜㅣㅅㅈㅣㅂ')
    print(words)