from tkinter import *
import tkinter.messagebox as msgbox
import sys, os, time

from word_join import *
from word_split import *
from wordlist import *
import answer


#### 함수 정의 ####
def insert():
    if len(input_lst) != 6:
        msgbox.showwarning('경고', '입력이 부족합니다.')
        return
    if tr == 0:
        global start
        start = time.time()
    checker(input_lst)
    input_lst.clear()
    input_lst_str = ''.join(input_lst)
    disp_text.set(f'[{input_lst_str}]')

def clear():
    if len(input_lst) == 0:
        msgbox.showwarning('경고', '삭제할 입력이 없습니다.')
        return
    input_lst.pop()
    input_lst_str = ''.join(input_lst)
    disp_text.set(f'[{input_lst_str}]')

def add_key(cha):
    if len(input_lst) >= 6:
        msgbox.showwarning('경고', '더이상 추가할 수 없습니다.')
        return
    else:
        input_lst.append(cha)
    input_lst_str = ''.join(input_lst)
    disp_text.set(f'[{input_lst_str}]')

def label_changer(tr, idx, cha, c):
    # 레이블 색 변경
    color = ['gray', 'orange', 'green']
    globals()[f'try{tr}_{idx+1}_text'].set(cha)
    globals()[f'try{tr}_{idx+1}'].configure(bg=color[c])
    # 키버튼 색 변경
    if cha in fst_floor:
        i = fst_floor.index(cha)
        if globals()[f'btnfst{i+1}'].cget('bg') == 'green':
            return
        elif globals()[f'btnfst{i+1}'].cget('bg') == 'orange' and c < 2:
            return
        globals()[f'btnfst{i+1}'].configure(bg=color[c])
    elif cha in snd_floor:
        i = snd_floor.index(cha)
        if globals()[f'btnsnd{i+1}'].cget('bg') == 'green':
            return
        elif globals()[f'btnsnd{i+1}'].cget('bg') == 'orange' and c < 2:
            return
        globals()[f'btnsnd{i+1}'].configure(bg=color[c])
    else:
        i = trd_floor.index(cha)
        if globals()[f'btntrd{i+1}'].cget('bg') == 'green':
            return
        elif globals()[f'btntrd{i+1}'].cget('bg') == 'orange' and c < 2:
            return
        globals()[f'btntrd{i+1}'].configure(bg=color[c])

def checker(lst):
    # 단어 체크
    word = joiner(lst)
    if word == False:
        msgbox.showerror('오류', '입력 오류!!')
        return
    if not dict_check(word):
        msgbox.showwarning('경고', '사전에 없는 단어입니다.')
        return
    # 자리 체크
    global tr
    tr += 1
    for idx, cha in enumerate(lst):
        if cha in ans:
            if cha == ans[idx]:
                label_changer(tr, idx, cha, 2)
                success[idx] = 1
            else:
                label_changer(tr, idx, cha, 1)
        else:
            label_changer(tr, idx, cha, 0)
    # 성공/실패 체크
    if success == [1] * 6:
        complete()
    if tr == 6 and success != [1] * 6:
        fail()

def complete():
    msgbox.showinfo('성공', f'시도 횟수: {tr}\n걸린 시간: {time.time()-start:.3f}초\n성공했습니다!')
    root.destroy()

def fail():
    response = msgbox.askretrycancel('실패', '실패했습니다! 재시도 하시겠습니까?')
    if response == 1:
        python = sys.executable
        os.execl(python, python, * sys.argv)
    elif response == 0:
        root.destroy()

#### 전역 파라미터 ####
input_lst = []
tr = 0
start = 0
success = [0] * 6
ans = word_split(answer.ANSWER)

#### GUI 구성 ####
root = Tk()
root.geometry("480x640")
root.title('꼬들_SeSAC')

#### TRY FRAME ####
try_frame = Frame(root, width=480, height=420)
try_frame.pack(side="top", fill="none", expand=True)
for i in range(6):
    globals()[f'try{i+1}'] = Frame(try_frame, height=10)
    globals()[f'try{i+1}'].grid(row=i, pady=3)
    for j in range(6):
        globals()[f'try{i+1}_{j+1}_text'] = StringVar()
        globals()[f'try{i+1}_{j+1}'] = Label(globals()[f'try{i+1}'], textvariable=globals()[f'try{i+1}_{j+1}_text'], font=('',20), relief='groove', width=4, height=2)
        globals()[f'try{i+1}_{j+1}'].grid(row=i, column=j, sticky=N+E+W+S, padx=3, pady=3)

#### DISPLAY FRAME ####
disp_frame = Frame(root, width=480)
disp_frame.pack(fill='none', expand=True)
disp_text = StringVar()
disp_text.set('[ ]')
disp = Label(disp_frame, textvariable=disp_text, font=('',20))
disp.pack()

#### BUTTON FRAME ####
bottom_frame = Frame(root, width=480, height=210)
bottom_frame.pack(side="top", fill="none", expand=True)
for i in range(3):
    globals()[f'key_frame{i+1}'] = Frame(bottom_frame, height=7)
    globals()[f'key_frame{i+1}'].pack(fill='none', expand=True)

fst_floor = ['ㅂ', 'ㅈ', 'ㄷ', 'ㄱ', 'ㅅ', 'ㅛ', 'ㅕ', 'ㅑ']
for i in range(8):
    globals()[f'btnfst{i+1}'] = Button(globals()['key_frame1'], text=fst_floor[i], width=3, height=2, command=lambda i=i:add_key(fst_floor[i]))
    globals()[f'btnfst{i+1}'].grid(row=0, column=i, sticky=N+E+W+S, padx=3, pady=3)

snd_floor = ['ㅁ', 'ㄴ', 'ㅇ', 'ㄹ', 'ㅎ', 'ㅗ', 'ㅓ', 'ㅏ', 'ㅣ', ]
for i in range(9):
    globals()[f'btnsnd{i+1}'] = Button(globals()['key_frame2'], text=snd_floor[i], width=3, height=2, command=lambda i=i:add_key(snd_floor[i]))
    globals()[f'btnsnd{i+1}'].grid(row=1, column=i, sticky=N+E+W+S, padx=3, pady=3)

trd_floor = ['입력', 'ㅋ', 'ㅌ', 'ㅊ', 'ㅍ', 'ㅠ', 'ㅜ', 'ㅡ', '삭제']
for i in range(1, 8):
    globals()[f'btntrd{i+1}'] = Button(globals()['key_frame3'], text=trd_floor[i], width=3, height=2, command=lambda i=i:add_key(trd_floor[i]))
    globals()[f'btntrd{i+1}'].grid(row=2, column=i, sticky=N+E+W+S, padx=3, pady=3)
btnInput = Button(globals()['key_frame3'], text='입력', width=7, height=2, command=insert)
btnDel = Button(globals()['key_frame3'], text='삭제', width=7, height=2, command=clear)
btnInput.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btnDel.grid(row=2, column=8, sticky=N+E+W+S, padx=3, pady=3)

root.resizable(False, False)
root.mainloop()