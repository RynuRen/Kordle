from word_split import *
import answer

def help():
    print('6개의 자모(자음 혹은 모음)으로 이루어진 단어를 맞추세요!')
    print('=====예제=====')
    print('ㄲ: ㄱ,ㄱ')
    print('ㅐ: ㅏ,ㅣ')
    print('새: ㅅ,ㅏ,ㅣ')
    print('싹: ㅅ,ㅅ,ㅏ,ㄱ')
    print('==============')
    print()

def inputer():
    while True:
        string = input('입력: ')
        trans = word_split(string)
        if trans:
            break
    return trans

def checker(ans, iput):
    ch = 0
    print(*iput, sep='\t')
    for idx, cha in enumerate(iput):
        if cha in ans:
            if cha == ans[idx]:
                print('◎', end='\t')
                ch += 1
            else:
                print('△', end='\t')
        else:
            print('Ｘ', end='\t')
    print()
    if ch == 6:
        return True
    else:
        return False

if __name__ == "__main__":

    ans_trans = word_split(answer.ANSWER)
    
    help()
    for _ in range(6):
        input_trans = inputer()
        if checker(ans_trans, input_trans):
            print('=====Succes!!=====')
            break
    else:
        print('=====Game Over=====')