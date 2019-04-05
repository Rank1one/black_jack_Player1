
# coding: utf-8

# # Black Jack Game

# Import needed packages

# In[2]:


#from IPython.display import clear_output
from os import system
from random import shuffle

def clear_output():
    _ = system('cls')



# Table View for single Player

# In[3]:


#function for Table display
def table_display(dealer,player_1):
    ''' This fuction takes 2 class object dealer and player in squence
    and display the table for black jack 21'''
    clear_output()
    print(dealer.show())
    print("[{}]".format(dealer.value()).center(113))
    print('-'*113)
    print('Black jack 3:2'.center(113))
    print('INSURANCE  *  2:1 ** Normal Hand * 1:1'.center(113))
    print('-'*113)
    print(player_1.show())
    print("[{}]".format(player_1.value()).center(113))
    print(" Bet {} Insurance: {}".format(player_1.plr_bets,player_1.plr_ins ).center(113))
    print('''1:DOUBLE DOWN                                                                                             3:HIT


2:SPLIT                                                                                                   4:STAND

                                                  5:INSURANCE
*****************************************************************************************************************''')
    print(f"Availabe Bal : {player_1.plr_bal}")


# Classes required for Black jack game

# #Class Deck

# In[4]:


class deck():
    ''' Input is the number of decks going to use for black jack
    creates list of cards as per the number of deck
    Note: number of decks should be +ve Integer'''

    symbols = ['♠', '♥', '♦', '♣']
    values = {'2 ':2,'3 ':3,'4 ':4,'5 ':5,'6 ':6,'7 ':7,'8 ':8,'9 ':9,'10':10,'j ':10,'K ':10,'Q ':10,'A ':11}

    def __init__(self,no_deck = 1):
        self.grand_deck = []
        for i in self.symbols:
            for j in self.values.keys():
                self.grand_deck.append((i,j))
        self.grand_deck = self.grand_deck * no_deck

    def value_cards(self,cards):
        '''This fubnction return the numerical value of given list of cards
         args = self,cards
         cards is the list of given cards'''
        smy = list(map(lambda x : x[1],cards))
        ret_value = 0
        if 'A ' in smy:
            ace_cnt = smy.count('A ')
            for i in smy:
                ret_value += self.values[i]
            while ret_value > 21:
                ret_value -= 10
                ace_cnt -= 1
                if ace_cnt == 0:
                    break
        else:
            for i in smy:
                ret_value += self.values[i]

        return ret_value


    def card_view(self,card,split_f = False,dealer_f = False):
        '''This function takes set of cards with split and dealer flag
        and return string as the card view of cards as per flags

        default args(self,*card,split_f = False,dealer_f = False)
        *card is list of cards or list of list of cards with split_f = True
        split_f & dealer_f will change according to black jack game play
        '''
        line = ['']*7
        if (not split_f) and (not dealer_f):
            no_crds = len(card)
            line[0] = ['┌───────┐']*no_crds
            line[1] = [f'│{i}     │' for (j,i) in card]
            line[2] = ['│       │']*no_crds
            line[3] = [f'│   {j}   │' for (j,i) in card]
            line[4] = ['│       │']*no_crds
            line[5] = [f'│     {i}│' for (j,i) in card]
            line[6] = ['└───────┘']*no_crds
        if dealer_f:
            no_crds = len(card)
            line[0] = ['┌───────┐']*(no_crds - 1) + ['┌───────┐']
            line[1] = [f'│{i}     │' for (j,i) in card[:-1]] + ['│░░░░░░░│']
            line[2] = ['│       │']*(no_crds -1) + ['│░░░░░░░│']
            line[3] = [f'│   {j}   │' for (j,i) in card[:-1]] + ['│░░░░░░░│']
            line[4] = ['│       │']*(no_crds -1) + ['│░░░░░░░│']
            line[5] = [f'│     {i}│' for (j,i) in card[:-1]] + ['│░░░░░░░│']
            line[6] = ['└───────┘']*(no_crds -1) + ['└───────┘']
        if split_f and (not dealer_f):
            no_crds = list(map(len,card))
            t_crds = len(card)
            line[0] = ['┌───────┐']*no_crds[0]
            for x in range(1,t_crds):
                line[0] = line[0] + ['    '] + ['┌───────┐']*no_crds[x]
            line[1] = [f'│{i}     │' for (j,i) in card[0]]
            for x in range(1,t_crds):
                line[1] = line[1] + ['    '] + [f'│{i}     │' for (j,i) in card[x]]
            line[2] = ['│       │']*no_crds[0]
            for x in range(1,t_crds):
                line[2] = line[2] + ['    '] + ['│       │']*no_crds[x]
            line[3] = [f'│   {j}   │' for (j,i) in card[0]]
            for x in range(1,t_crds):
                line[3] = line[3] + ['    '] +[f'│   {j}   │' for (j,i) in card[x]]
            line[4] = ['│       │']*no_crds[0]
            for x in range(1,t_crds):
                line[4] = line[4] + ['    '] + ['│       │']*no_crds[x]
            line[5] = [f'│     {i}│' for (j,i) in card[0]]
            for x in range(1,t_crds):
                line[5] = line[5] + ['    '] + [f'│     {i}│' for (j,i) in card[x]]
            line[6] = ['└───────┘']*no_crds[0]
            for x in range(1,t_crds):
                line[6] = line[6] + ['    '] + ['└───────┘']*no_crds[x]

        for i in range(len(line)):
            line[i] = ''.join(line[i]).center(113)

        ret_str = '\n'.join(line)

        return ret_str



# #Class Dealer

# In[5]:


class dealer():
    '''This create a dealer object'''
    def __init__(self,no_deck = 1):
        self.obj_deck = deck(no_deck)
        self.ply_deck = self.obj_deck.grand_deck
        self.sfl_deck = list()
        self.drl_cards = list()
        self.dealer_f = True


    def card_shuffle(self):
        shuffle(self.ply_deck)
        self.sfl_deck = self.ply_deck.copy()

    def give_card(self):
        try:
            return self.sfl_deck.pop()
        except IndexError:
            self.card_shuffle()
            return self.sfl_deck.pop()

    def hit(self,*card):
        self.drl_cards += card

    def show(self):
        if len(self.drl_cards) == 0:
            return '\n'*6
        if self.dealer_f:
            return self.obj_deck.card_view(self.drl_cards,dealer_f = self.dealer_f)
        else:
            return self.obj_deck.card_view(self.drl_cards)

    def value(self):
        if self.dealer_f:
            return self.obj_deck.value_cards(self.drl_cards[:-1])
        else:
            return self.obj_deck.value_cards(self.drl_cards)

    def drl_reset(self):
        self.drl_cards.clear()





# #Class Player

# In[6]:


class player():
    '''This create a player object'''
    def __init__(self):
        self.obj_deck = deck(0)
        self.plr_bal = 0
        self.plr_ins = 0
        self.plr_cards =list()
        self.plr_bets = list()
        self.split_f = False
        self.eva_list = list()
        self.busted_list = list()
        self.cur_bet = 0


    def bet(self,amount):
        while True:
            if amount <= self.plr_bal and amount != 0:
                break
            else:
                try:
                    amount = int(input('You wana reduce the amount or press enter to add more balance >> '))
                except:
                    try:
                        x = int(input('Insufficient balance!!!\nEnter deposite amount or press Enter EXIT >> '))
                    except:
                        return False
                    else:
                        self.add_bal(x)

        self.plr_bets.append(amount)
        self.cur_bet = self.plr_bal
        self.plr_bal -= amount
        return True



    def add_bal(self,amount):
        self.plr_bal += amount
        self.cur_bet += amount


    def split(self,drl_obj):
        bet = self.plr_bets[-1]
        if self.split_f:
            if len(self.plr_cards[-1]) == 2 and (self.obj_deck.value_cards([self.plr_cards[-1][0]]) == self.obj_deck.value_cards([self.plr_cards[-1][1]])):
                flag = True
            else:
                flag = False
        else:
            if len(self.plr_cards) == 2 and (self.obj_deck.value_cards([self.plr_cards[0]]) == self.obj_deck.value_cards([self.plr_cards[1]])):
                flag = True
            else:
                flag = False

        if flag:
                while True:
                        if bet > self.plr_bal:
                            try:
                                x = int(input('Insufficient balance!!!\nEnter deposite amount or press Enter to choose another option >> '))
                            except:
                                return False
                            else:
                                self.add_bal(x)
                        else:
                            self.plr_bal -= bet
                            self.plr_bets.append(bet)
                            break

                if self.split_f:
                    self.plr_cards.append([self.plr_cards[-1].pop()])

                if (not self.split_f) and len(self.plr_bets) == 2:
                    self.plr_cards.append([self.plr_cards.pop(-2)])
                    self.plr_cards.append([self.plr_cards.pop(-2)])

                self.plr_cards[-1].append(drl_obj.give_card())
                self.plr_cards[-2].append(drl_obj.give_card())
                self.split_f = True
               # print(self.plr_cards)

                return True
        else:
            input('Option is not available now choose another')
            return False


    def hit(self,*card):
        if self.split_f:
            self.plr_cards[-1]  += card
        else:
            self.plr_cards += card

    def stand(self):
        if self.split_f:
            val = self.plr_cards.pop()
            bet = self.plr_bets.pop()
            self.eva_list.append((val,bet))
        else:
            val = self.plr_cards
            bet = self.plr_bets.pop()
            self.eva_list.append((val,bet))
            return True
        if self.split_f and len(self.plr_cards) == 0:
            return True
        else:
            return False


    def double_down(self,drl_obj):
        bet = self.plr_bets[-1]
        if self.split_f:
            if len(self.plr_cards[-1]) == 2:
                flag = True
            else:
                flag = False
        else:
            if len(self.plr_cards) == 2:
                flag = True
            else:
                flag = False

        if flag:
                while True:
                        if bet > self.plr_bal:
                            try:
                                x = int(input('Insufficient balance!!!\nEnter deposite amount or press Enter to choose another option >> '))
                            except:
                                return False
                            else:
                                self.add_bal(x)

                        else:
                            self.plr_bal -= self.plr_bets[-1]
                            self.plr_bets[-1] += self.plr_bets[-1]
                            self.hit(drl_obj.give_card())
                            break
                return True
        else:
            input('Option is not available now choose another')
            return False

    def insurance(self,drl_obj):
        if drl_obj.drl_cards[0][1] == 'A ' and len(drl_obj.drl_cards) == 2 and (not self.split_f) and len(self.plr_cards) == 2:
            try:
                x  = int(input('Enter insurance amount >> '))
            except:
                print('Exception occoured choose another option')
                return False
            else:
                while True:
                        if x > self.plr_bal:
                            try:
                                y = int(input('Insufficient balance!!!\nEnter deposite amount or press Enter to choose another option >> '))
                            except:
                                return False
                            else:
                                self.add_bal(y)
                        else:
                            self.plr_ins = x
                            self.plr_bal -= self.plr_ins
                            break
                return True
        else:
            input('Option is not available now choose another')
            return False


    def show(self):
        if len(self.plr_cards) == 0:
            return '\n'*6
        if self.split_f:
            return self.obj_deck.card_view(self.plr_cards,split_f = self.split_f)
        else:
            return self.obj_deck.card_view(self.plr_cards)


    def value(self):
        if self.split_f:
            ret_val = [self.obj_deck.value_cards(i) for i in self.plr_cards]
            return ret_val
        else:
            return self.obj_deck.value_cards(self.plr_cards)

    def plr_reset(self):
        self.plr_cards.clear()
        self.plr_bets.clear()
        self.split_f = False
        self.eva_list.clear()
        self.busted_list.clear()
        self.cur_bet = 0
        self.plr_ins = 0

    def bust_check(self):
        bust_f = False
        if self.split_f:
            if self.obj_deck.value_cards(self.plr_cards[-1]) > 21:
                bust_f = True
        else:
            if self.obj_deck.value_cards(self.plr_cards) > 21:
                bust_f = True
        return bust_f

    def plr_bust(self):
        if self.bust_check:
            if self.split_f:
                self.busted_list.append((self.plr_cards.pop(),self.plr_bets.pop()))

                if len(self.plr_cards) == 0:
                    return True
                else:
                    return False
            else:
                self.busted_list.append((self.plr_cards.copy(),self.plr_bets.pop()))
                self.plr_cards.clear()
                self.plr_bets.clear()
                return True
        else:
            return False


    def eva_money(self,drl_cards):
        if len(self.eva_list) != 0:
            t_mny = 0
            t_bet = 0
            for i in self.eva_list:
                if len(i[0]) == 2 and self.obj_deck.value_cards(i[0]) == 21 and self.obj_deck.value_cards(drl_cards[:3]) < 21:
                    t_mny += round(i[1]*1.5)
                    t_bet += i[1]
                else:
                    if self.obj_deck.value_cards(drl_cards) > 21 :
                        t_mny += i[1]
                        t_bet += i[1]
                    if self.obj_deck.value_cards(i[0]) > self.obj_deck.value_cards(drl_cards):
                        t_mny += i[1]
                        t_bet += i[1]
                    if self.obj_deck.value_cards(i[0]) == self.obj_deck.value_cards(drl_cards):
                        t_mny += 0
                        t_bet += i[1]
        else:
            t_mny = 0
            t_bet = 0

        if self.plr_ins != 0 and self.obj_deck.value_cards(drl_cards[:3]) == 21:
            t_mny += self.plr_ins*2
            t_bet += self.plr_ins
        self.cur_bet -= self.plr_bal
        print('Total money win : {}  Total bet : {}'.format(t_mny+t_bet,self.cur_bet ))
        self.add_bal(t_mny + t_bet)
        print("\nEvaluating bets : (cards' value, bet)\n")
        print(list(map(lambda x :(self.obj_deck.value_cards(x[0]),x[1]),self.eva_list)))
        print("\nBusted bets : (cards' value, bet)\n")
        print(list(map(lambda x :(self.obj_deck.value_cards(x[0]),x[1]),self.busted_list)))



# #Driving function Utilities

# In[7]:


#take input Function
def ask_input():
    while True:
        try:
            x = int(input("Enter your Option >> "))
        except:
            print("Invalid input!!! Try Again")
        else:
            if 0 < x < 6:
                break
            else:
                print("Invalid input!!! Try Again")
    return x


# In[8]:


#add balance
try:
    bal = int(input('Add balance to Play >> '))
except:
    print('It is not money!!@#$% \nKicked Out ')
    start_f = False
else:
    d = dealer(1)
    d.card_shuffle()
    p = player()
    p.add_bal(bal)
    start_f = True
#enter to the table loop also main loop
while start_f:
    #place bet loop
    while True:
        table_display(d,p)
        try:
            amount = int(input('Place the bet >> '))
        except:
            x = input('Invalid Input!!! \nPress enter to Continue or X to leave the Table >>')
            if x.lower() == 'x':
                start_f = False
                break
        else:
            if p.bet(amount):
                break
            else:
                input('Bet not placed')
                start_f = False
                break
    if not start_f:
        clear_output()
        print('**Terminated**')
        break
    p.hit(d.give_card())
    p.hit(d.give_card())
    d.hit(d.give_card())
    d.hit(d.give_card())
    d.dealer_f = True

    #playing loop
    table_display(d,p)
    while True:
        #bust_f = False


        p_ip = ask_input()

        if p_ip == 1:
            if p.double_down(d):
                if p.bust_check():
                    pass
                else:
                    p_ip = 4

        if p_ip == 2:
            p.split(d)
        if p_ip == 3:
            p.hit(d.give_card())
        if p_ip == 5:
            p.insurance(d)

        ############bust_f evaluation##############
        #print(p_ip == 4 and ((p.split_f and len(p.plr_cards) == 1) or (not p.split_f)))
        #print(len(p.eva_list) == 0 and (((p.split_f and len(p.plr_cards) == 1) and p.bust_check()) or (not p.split_f and p.bust_check() )))
        if p_ip == 4 and ((p.split_f and len(p.plr_cards) == 1) or (not p.split_f)):

            bust_f = False
            d.dealer_f = False
            while d.value() < 17:
                d.hit(d.give_card())
        elif len(p.eva_list) == 0 and (((p.split_f and len(p.plr_cards) == 1) and p.bust_check()) or (not p.split_f and p.bust_check() )) :
            bust_f = True
            d.dealer_f = False
        elif len(p.eva_list) != 0 and (((p.split_f and len(p.plr_cards) == 1) and p.bust_check()) or (not p.split_f and p.bust_check() )) :
            bust_f = False
            d.dealer_f = False
            while d.value() < 17:
                d.hit(d.give_card())

            #else:
            #    bust_f = False
            #    d.dealer_f = False
            #    while d.value() < 17:
            #        d.hit(d.give_card())

        #################END#######################

        table_display(d,p)
        if p.split_f and p_ip == 4:
            input('Enter for next split hand')
        ###***stand***###
        if p_ip == 4:
            if p.stand():
                break
        #########END########
        #check for bust_player
        if p.bust_check() and p.split_f :
            input('Enter for next split hand')
            if p.plr_bust():
                break

        if p.bust_check() and (not p.split_f) :
            #bust_f = True
            p.plr_bust()
            break


    #Final result
  #  table_display(d,p)
  #  p.plr_bust()
    p.eva_money(d.drl_cards)
    if bust_f:
        print('Bet busted')

    last_chs = input('You wana bet again press enter or Exit >> ')

    if last_chs.lower() == 'exit':
        start_f = False
        print('**Terminated**')
    else:
        d.drl_reset()
        p.plr_reset()
