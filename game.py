import random
from enum import Enum

class Dir(Enum):
    RIGHT='►'
    LEFT='◄'
    UP='▲'
    DOWN='▼'


class mob :
    def __init__(self , skin):
        self.skin = skin
        self.selectrandomblock()

    def selectrandomblock(self):
        while True:
            i = random.randint(1, h - 2)
            j = random.randint(1, w - 2)
            if ground[i][j] == EMPTY:
                self.i = i
                self.j = j
                ground[i][j] = self.skin
                break

    def _isvailble(self , i , j ):
        if ground[i][j] == EMPTY:
            return True
        return False
#i == self.i - 1
    def move(self , i , j ) :
        if self._isvailble(i , j) :
            ground[self.i][self.j] = EMPTY

            self.i = i
            self.j = j

            ground[self.i][self.j] = self.skin



    def random_move(self):
        r = random.randint(1 , 4 )

        if r == 1 :
            self.move(self.i - 1 , self.j  )
        elif r == 2 :
            self.move(self.i + 1 , self.j)
        elif r == 3 :
            self.move(self.i  , self.j - 1)
        elif r == 4 :
            self.move(self.i , self.j + 1)

EMPTY = ' '
PLAYER = '!'
WALL = '■'
DIRT = '0'
ground = []
pl=Dir.LEFT
mobs = []


def randomplayerplace():
    while True:
        i = random.randint(1 , h - 2)
        j = random.randint(1 , w - 2)
        if ground[i][j] == EMPTY :
             return i , j


def chooserandomblock() :

    t = random.randint(1 , 100)

    if t > 0 and t <= 10 :
        return WALL

    elif t>10 and t<60 :
        return EMPTY
    else:
        return DIRT


arr = []

def creatground():

    for i in range(w):
        r = []
        for j in range(h) :
            if i == 0 or i == w - 1 or j == 0 or j == h - 1 :
                r.append(WALL)

            else :
                r.append(chooserandomblock())


        ground.append(r)

def show () :
    for i in range(w):
        for j in range(h):
            if i == pl_i and j == pl_j :
                print(pl.value , end=' ')
            elif i == goal_i and j == goal_j :
                print('G' , end=' ')
            else :
                print(ground[i][j],end=' ')
        print()


def ismob (i , j) :
    if ground[i][j] == 'M' :
        return True

def isAvailble(i,j):
    if ground[i][j]==EMPTY:
        return True
    return False

w=int(input("Enter Width: "))
h=int(input("Enter height: "))

creatground()
chooserandomblock()
pl_i,pl_j=randomplayerplace()
goal_i , goal_j = randomplayerplace()

show()
input()
global flag
flag = 0
def digInPlayerDir():
    flag = 0
    a = h - pl_i
    b = w - pl_j
    x = 1
    while(x < a or x < b) :
        global score
        if pl==Dir.RIGHT:
            if ground[pl_i][pl_j+x]==DIRT:
                ground[pl_i][pl_j+x]=EMPTY
                score += 1
                flag = 1
                break
        elif pl==Dir.LEFT:
            if ground[pl_i][pl_j-x]==DIRT:
                ground[pl_i][pl_j-x]=EMPTY
                score += 1
                flag = 1
                break
        elif pl==Dir.UP:
            if ground[pl_i-x][pl_j]==DIRT:
                ground[pl_i-x][pl_j]=EMPTY
                score += 1
                flag = 1
                break
        elif pl==Dir.DOWN:
            if ground[pl_i+x][pl_j]==DIRT:
                ground[pl_i+x][pl_j]=EMPTY
                score += 1
                flag = 1
                break
        x += 1

def diginplayermob() :

    a = h - pl_i
    b = w - pl_j
    x = 1
    while(x < a or x < b) :
        global score
        if pl==Dir.RIGHT:
            if ground[pl_i][pl_j+x]=='M':
                ground[pl_i][pl_j+x]=EMPTY
                score += 5
                break
        elif pl==Dir.LEFT:
            if ground[pl_i][pl_j-x]=='M':
                ground[pl_i][pl_j-x]=EMPTY
                score += 5
                break
        elif pl==Dir.UP:
            if ground[pl_i-x][pl_j]=='M':
                ground[pl_i-x][pl_j]=EMPTY
                score += 5
                break
        elif pl==Dir.DOWN:
            if ground[pl_i+x][pl_j]=='M':
                ground[pl_i+x][pl_j]=EMPTY
                score += 5
                break
        x += 1



score = 0
for i in range(5):
    mobs.append(mob('M'))


while True:
        if (score >= 20) :
            print("you win")
            break
        if (pl_i == goal_i and pl_j == goal_j):
         print("you win")
         break
    #print_char(0,0,'p')
        show()
        for x in mobs :
            x.random_move()
        print(score)
        print(Dir.RIGHT.value)
        key=input()
        if key=='d':
            pl=Dir.RIGHT
            if isAvailble(pl_i,pl_j+1): pl_j+=1
            if ismob(pl_i, pl_j + 1):
                print("you lose :) nigga")
                break
        elif key=='s':
            pl=Dir.DOWN
            if isAvailble(pl_i+1,pl_j): pl_i+=1
            if ismob(pl_i + 1, pl_j):
                print("you lose :) nigga")
                break
        elif key=='a':
            pl=Dir.LEFT
            if isAvailble(pl_i,pl_j-1): pl_j-=1
            if ismob(pl_i, pl_j - 1):
                print("you lose :) nigga")
                break
        elif key=='w':
            pl=Dir.UP
            if isAvailble(pl_i-1,pl_j): pl_i-=1
            if ismob(pl_i - 1, pl_j):
                print("you lose :) nigga")
                break
        elif key=='e':
            digInPlayerDir()
            if (flag == 0) :
              diginplayermob()
        elif key=='q':
            break



