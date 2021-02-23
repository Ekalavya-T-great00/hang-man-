import random 
import time


def make_choices(n):
    '''THIS FUNCTION MAKES THE CHOICES OF THE WORDS FOR THE GAME TAKING THE INPUT OF THE LEVLE'''
    l1 = ['name' , 'this','cover','chair','glass']
    l2 = ['gesture','nation','clever','silver','ecstacy']
    l3 = ['extrodinary','benovalent','assistant','solitude','sincerity']
    if n==2:
        m = random.choice(l1)
    elif n==3:
        m = random.choice(l2)
    elif n==5:
        m = random.choice(l3)
    return m

def make_sp(m,n):
    '''THIS FUNCTION REPLACES SOME CHARACTERS WITH UNDERSCORE TO CREATE PUZZLE OUT OF WORD'''
    l = [x for x in range(len(m))]
    temp = m
    ind_li = random.sample(l,k=n)
    for i in m:
        new_wd = list(temp)
        for j in ind_li:
            new_wd[j] = '-'
    temP = ''
    for i in new_wd:
        temP+=i
    temp = temP
    return temp,m


def exam(n):
    '''THIS FUNCTION EXAMINES AND RETURNS THE INDEXES OF UNDERSCORES'''
    l = []
    for i in range(len(n)):
        if n[i]=='-':
            l.append(i)
    return l

def fill(l,m):
    '''THIS FUNCTION FILLS THE SPACES WITH THE LIST OF GIVEN USER INPUTS'''
    n = exam(l)
    for i,j in zip(n,m):
        l[i]=j
    st = ''
    for i in l:
        st+=i 
    return st


def take_input(n):
    '''THIS FUNCTION TAKES THE USER INPUTS'''
    l = []
    for i in range(1,n+1):
        n = input(f'enter response {i} : ')
        l.append(n)
    return l

def take_level():
    '''THIS FUNCTION GIVES USER THE OPTIONS FOR THE LEVEL'''
    print('CHOOSE LEVEL')
    print('1 FOR EASY')
    print('2 FOR MEDIUM')
    print('3 FOR HARD')
    n = int(input('enter response :'))
    while True:
        if n==1:
            return 2
        elif n==2:
            return 3
        elif n==3:
            return 5
        else :
            print('please choose inputs from the options')
            take_level()

def animate(n):
    '''THIS FUNCTION ANIMATES ACCORDING TO DESIRED OUTPUT'''
    if n==5:
        print('[-] SUSPECT IS ORDERED FOR PROSECUTION !!')
        print('DO NOT MAKE MISTAKES , THE OUTCOME COULD BE HEAVY')
        print('|````````````')
        print('|            ')
        print('|           ')
        print('|           ')
        print('|           ')
        print('|     O     O      ')
        print('|    /|     |\    ')
        print('|____/|_____|\_____')
    elif n==4:
        print('[-] THE STATGE IS NOW READY FOR PROSECUTION !!')
        print('')
        print('|```````````|')
        print('|          [ ]')
        print('|           ')
        print('|           ')
        print('|           ')
        print('|           ')
        print('|             ')
        print('|_____________')

    elif n==3:
        print('[-] THE ROPE IS NOW HUNG !!')
        print('|```````````!`')
        print('|           !')
        print('|           !')
        print('|           !')
        print('|           !')
        print('|           O')
        print('|             ')
        print('|_____________')
    elif n==2:
        print('[-] THE SUSPECT HAS COME TO STAGE NOW !!')
        print('|```````````!`')
        print('|           !')
        print('|           !')
        print('|           !')
        print('|           !')
        print('|           O o ')
        print('|             |\ ')
        print('|_____________\ ')
    elif n==1:
        print('[-] THE SUSPECT IS HANGING NOW   !!')
        print('|```````````!`')
        print('|           !')
        print('|           !')
        print('|           0')
        print('|          /|\ ')
        print('|          / \ ')
        print('|              ')
        print('|_____________  ')
    if n==6:
        print('|`````````````')
        print('|           ')
        print('|           ')
        print('|           ')
        print('|           ')
        print('|           ')
        print('|             ')
        print('|_____________')



def find_chances(l):
    '''THIS FUNCTION DEFINES THE NUMBER OF CHANCES ACCORDING TO DIFFICULTY'''
    if l==2 :
        c = 5
    if l==3:
        c = 4
    if l==5:
        c = 3
    return c


def main():
    '''THIS IS THE MAIN FUNCTION OF THE GAME'''
    print('WELCOME TO HANGMAN GAME!!')
    time.sleep(0.5)
    l = take_level()
    word = make_choices(l)
    incomp,comp = make_sp(word,l)
    animate(6)
    time.sleep(0.5)
    print('THE EXECUTION IS ABOUT TO HAPPEN . YOU HAVE TO SOLVE THE FOLLOWING WORD RIDDLE IN ORDER TO SAVE THE MAN')
    time.sleep(0.5)
    print('_______________________________________________________________________________________________________')
    time.sleep(0.5)
    ch = find_chances(l)
    while ch:
        print(f'you have {ch} chances to find the answer'.upper())
        print((incomp).upper())
        time.sleep(0.5)
        res = take_input(l)
        if comp==fill(list(incomp),res):
            print('HELL YEAH ! YOU SAVED THE MAN ')
            print('YOU WON !')
            return True
        else:
            ch-=1
            animate(ch)
    if ch==0:
        animate(0)
        print('THE EXCUTION IS MADE ! AN INNOCENT MAN IS HANGED')
        print('YOU LOST !!!!')
        return True

def game_loop():
    '''THIS FUNCTION DEFINES THE LOOP FOR THE MAIN FUNCTION'''
    n = input('DO YOU WANT TO PLAY ? (y/n) :')
    if n=='y':
        main()
        game_loop()
    elif n=='n':
         exit()
    else:
        print('ENTER A VALID REPLY !! ')
        game_loop()

game_loop()



    



