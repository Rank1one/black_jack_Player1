
# coding: utf-8

# Display Board Fuction
# ___

# In[ ]:


from os import system
def clear_output():
    _=system('cls')

def board_dpy(brd = [' ',' ',' ',' ',' ',' ',' ',' ',' ']):
    clear_output()
    print(f'''     *     *
  {brd[0]}  *  {brd[1]}  *  {brd[2]}
     *     *
*****************
     *     *
  {brd[3]}  *  {brd[4]}  *  {brd[5]}
     *     *
*****************
     *     *
  {brd[6]}  *  {brd[7]}  *  {brd[8]}
     *     *    ''')


# Players input to Board
# _____

# In[ ]:


#input check
def input_chk(x,brd):
    if not(x in list(range(1,10))) :
        return False
    if x >= 7:
        x -= 7
    elif x >= 4 and x <= 6:
        x -= 1
    elif x >= 1 and x <= 3:
        x += 5
    if brd[x] == ' ':
        return True
    else:
        return False




# In[ ]:


def Player_ip(name,M,brd):
    try:
        x = int(input(f'{name} Enter your position >>> '))
    except ValueError:
        x = 10
    while True:
        if not(input_chk(x,brd)):
            board_dpy(brd)
            print('Invalid input!!!')
            try:
                x = int(input(f'{name} Enter your position >>> '))
            except ValueError:
                x = 10
        else:
            if x == 7:
                brd[0] = M
                break;
            elif x == 8:
                brd[1] = M
                break;
            elif x == 9:
                brd[2] = M
                break;
            elif x == 4:
                brd[3] = M
                break;
            elif x == 5:
                brd[4] = M
                break;
            elif x == 6:
                brd[5] = M
                break;
            elif x == 1:
                brd[6] = M
                break;
            elif x == 2:
                brd[7] = M
                break;
            elif x == 3:
                brd[8] = M
                break;
    return brd


# Win Check
# __________

# In[ ]:


def win_check(brd):
    if brd[0] == brd[1] == brd[2] and brd[0] != ' ':
        return brd[0]
    if brd[3] == brd[4] == brd[5] and brd[3] != ' ':
        return brd[3]
    if brd[6] == brd[7] == brd[8] and brd[6] != ' ':
        return brd[6]
    if brd[0] == brd[3] == brd[6] and brd[0] != ' ':
        return brd[0]
    if brd[1] == brd[4] == brd[7] and brd[1] != ' ':
        return brd[1]
    if brd[2] == brd[5] == brd[8] and brd[2] != ' ':
        return brd[2]
    if brd[0] == brd[4] == brd[8] and brd[0] != ' ':
        return brd[0]
    if brd[2] == brd[4] == brd[6] and brd[2] != ' ':
        return brd[2]
    if not(' ' in brd) :
        return 'Draw'
    else:
        return 'Cnt'


# Result
# ___
#

# In[ ]:


def Result(brd,p1_name,p2_name,p1_M,p2_M):
    result = win_check(brd)
    if  result == 'Draw' :
        print('**DRAW***')
        return True
    elif result == p1_M:
        print(f'{p1_name} wins')
        return True
    elif result == p2_M:
        print(f'{p2_name} wins')
        return True
    else:
        return False


# Select Mark
# ____

# In[ ]:


def select_M(name):
    while True:
        p_M = input(f'{name} please select your mark between X or O  >> ')
        ch_set = {'X','O'}
        if p_M in ch_set :
            ch_set-={p_M}
            return (p_M,list(ch_set)[0])
        else:
            clear_output()
            print('Invalid input!!!')



# # **CPU**
#   {brd[0]}  *  {brd[1]}  *  {brd[2]}
#
#   {brd[3]}  *  {brd[4]}  *  {brd[5]}
#
#   {brd[6]}  *  {brd[7]}  *  {brd[8]}
#

# In[ ]:


#Detect a cross
def det_crs(m,brd):
    l_crs = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in l_crs:
        l_sym = [brd[i[0]],brd[i[1]],brd[i[2]]]
        if l_sym.count(m) == 2 and ' ' in l_sym:
            return i[l_sym.index(' ')]
    else:
        return 'NA'



# In[ ]:


#position of marks
def pos_mrks(p_m,c_m,brd):
    a = list()
    b = list()
    cnt = 0
    for i in brd:
        if i == p_m:
            a.append(cnt)
            cnt+=1
        elif i == c_m:
            b.append(cnt)
            cnt+=1
        else:
            cnt+=1
    return (a,b)



# In[ ]:


from random import choice
def CPU(c_m,p_m,brd):
    if brd.count(' ') == 9:
        brd[7] = c_m
        return brd
    if brd.count(' ') == 7:
        p,c = pos_mrks(p_m,c_m,brd)
        if p[0] == 1:
            brd[3] = c_m
            return brd
        if p[0] in [0,3,4]:
            brd[6] = c_m
            return brd
        if p[0] in [2,5]:
            brd[8] = c_m
            return brd
        if p[0] in [6,8]:
            brd[4] = c_m
            return brd
    if brd.count(' ') == 5:
        x = det_crs(p_m,brd)
        y = det_crs(c_m,brd)
        p,c = pos_mrks(p_m,c_m,brd)
        if y != 'NA':
            brd[y] = c_m
            return brd
        if x == 'NA':
            if c[0] == 3 and 1 in p:
                brd[brd.index(' ')] = c_m
                return brd
            if c[0] != 3 and c[0] != 4:
                brd[4] = c_m
                return brd
            if c[0] == 4:
                brd[brd.index(' ')] = c_m
                return brd
        else:
            brd[x] = c_m
            return brd
    if brd.count(' ') == 8:
        if brd.index(p_m) in [0,2,6,8]:
            brd[4] = c_m
            return brd
        if brd.index(p_m) == 4:
            brd[6] = c_m
            return brd
        if brd.index(p_m) in [1,3,5,7]:
            if brd.index(p_m) in [1,3]:
                brd[0] = c_m
                return brd
            if brd.index(p_m) in [5,7]:
                brd[8] = c_m
                return brd
    if brd.count(' ') == 6:
        x = det_crs(p_m,brd)
        y = det_crs(c_m,brd)
        if y != 'NA':
            brd[y] = c_m
            return brd
        if x == 'NA':
            p,c = pos_mrks(p_m,c_m,brd)
            if len(c) == 1 and c[0] == 6:
                brd[8] = c_m
                return brd
            if len(c) == 1 and c[0] == 4:
                if p in [[1,6],[2,3]]:
                    brd[0] = c_m
                    return brd
                if p in [[1,8],[0,5]]:
                    brd[2] = c_m
                    return brd
                if p in [[2,6],[0,8]]:
                    brd[choice([1,3,5,7])] = c_m
                    return brd
                if p in [[3,8],[0,7]]:
                    brd[6] = c_m
                    return brd
                if p in [[5,6],[2,7]]:
                    brd[8] = c_m
                    return brd
            if len(c) == 1 and c[0] in [0,8]:
                if brd[c[0]] == brd[0]:
                    z =list(set(p)-{1,3})
                    if len(z) == 0:
                        brd[4] = c_m
                        return brd
                    else:
                        if z[0] == 2 and 3 in p:
                            brd[4] = c_m
                            return brd
                        elif z[0] == 6 and 1 in p:
                            brd[4] = c_m
                            return brd
                        else:
                            if 1 in p:
                                brd[6] = c_m
                                return brd
                            if 3 in p:
                                brd[2] = c_m
                                return brd
                if brd[c[0]] == brd[8]:
                    z =list(set(p)-{5,7})
                    if len(z) == 0:
                        brd[4] = c_m
                        return brd
                    else:
                        if z[0] == 2 and 7 in p:
                            brd[4] = c_m
                            return brd
                        elif z[0] == 6 and 5 in p:
                            brd[4] = c_m
                            return brd
                        else:
                            if 5 in p:
                                brd[6] = c_m
                                return brd
                            if 7 in p:
                                brd[2] = c_m
                                return brd
        else:
            brd[x] = c_m
            return brd
    if brd.count(' ') < 5:
        x = det_crs(p_m,brd)
        y = det_crs(c_m,brd)
        if y != 'NA':
            brd[y] = c_m
            return brd
        if x == 'NA':
            if brd[4] == ' ':
                brd[4] = c_m
                return brd
            else:
                brd[brd.index(' ')] = c_m
                return brd
        else:
            brd[x] = c_m
            return brd





# # **Drive Code**
# ___

# In[ ]:


#from random import choice
#board_dpy()
while True:

    p1_name = input('Player1 Input your name >> ')
    p2_name = 'CPU'
    T_won = choice([p1_name,p2_name])
    print(f'{T_won} WON the First turn')

    if T_won == p1_name :
        p1_M,p2_M = select_M(p1_name)

    else:
        p2_M,p1_M = ('O','X')

    brd =list('         ')
    board_dpy(brd)
    while True:
        if T_won == p1_name:
            brd = Player_ip(p1_name,p1_M,brd)
            board_dpy(brd)
            if Result(brd,p1_name,p2_name,p1_M,p2_M):
                break
            brd = CPU(p2_M,p1_M,brd)
            board_dpy(brd)
            if Result(brd,p1_name,p2_name,p1_M,p2_M):
                break
        if T_won == p2_name:
            brd = CPU(p2_M,p1_M,brd)
            board_dpy(brd)
            if Result(brd,p1_name,p2_name,p1_M,p2_M):
                break
            brd = Player_ip(p1_name,p1_M,brd)
            board_dpy(brd)
            if Result(brd,p1_name,p2_name,p1_M,p2_M):
                break

    Y=input('press Y for rematch or any key to quit >> ')
    if Y in ('Y','y'):
        clear_output()
    else:
        clear_output()
        print('***Terminated***')
        break
