"""Mini-game by CAN YILDIRIM · Hugging Games."""
import random
import math

def reply(state, message):
    return state, message

def finish(state, message):
    state["done"] = True
    return state, message + "\n🏁 Oyun bitti. Yeniden başlat ile tekrar oyna."

def _view(b):return '\n'.join(' '.join('·' if c=='.' else c for c in row) for row in b)+'\n1 2 3 4 5 6 7'
def _winner(b,c):
    for y in range(6):
        for x in range(7):
            for dx,dy in ((1,0),(0,1),(1,1),(1,-1)):
                if all(0<=x+dx*k<7 and 0<=y+dy*k<6 and b[y+dy*k][x+dx*k]==c for k in range(4)):return True
    return False
def _drop(b,x,c):
    for y in range(5,-1,-1):
        if b[y][x]=='.':b[y][x]=c;return True
    return False
def new_game():
    s={'board':[['.']*7 for _ in range(6)],'done':False};return s,'1-7 sütun seç. Sen X.\n'+_view(s['board'])
def play(s,action):
    if s['done']:return reply(s,'Yeni oyun başlat.')
    try:x=int(action)-1
    except ValueError:return reply(s,'1-7 yaz.')
    b=s['board']
    if x not in range(7) or b[0][x]!='.':return reply(s,'Geçerli boş sütun seç.')
    _drop(b,x,'X')
    if _winner(b,'X'):return finish(s,'🎉 Sen kazandın!\n'+_view(b))
    if all(c!='.' for c in b[0]):return finish(s,'Berabere!\n'+_view(b))
    cpu=random.choice([i for i in range(7) if b[0][i]=='.']);_drop(b,cpu,'O')
    if _winner(b,'O'):return finish(s,'Bilgisayar kazandı!\n'+_view(b))
    return reply(s,_view(b))
